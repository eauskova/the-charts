import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon

# Создаем сетку
x = np.linspace(-12, 24, 400)
y = np.linspace(-12, 12, 400)
X, Y = np.meshgrid(x, y)

# Создаем фигуру и оси
fig, ax = plt.subplots()

# Определяем первую прямую: x1 - 5*x2 = 20
# Эта прямая проходит через (0, -4) и (20, 0)
x1_vals = np.linspace(-12, 24, 400)
y1_vals = (x1_vals - 20) / 5  # Уравнение первой прямой

# Определяем вторую прямую: -x1 + x2 = 9
# Эта прямая проходит через (0, 9) и (-9, 0)
y2_vals = x1_vals + 9  # Уравнение второй прямой

# Строим первую прямую
ax.plot(x1_vals, y1_vals, label='$x_1 - 5x_2 = 20$ (1)', color='red', lw=2)
# Строим вторую прямую
ax.plot(x1_vals, y2_vals, label='$-x_1 + x_2 = 9$ (2)', color='green', lw=2)

# Закрашиваем области
# Закрашиваем область ниже первой прямой (1)
ax.fill_between(x1_vals, y1_vals, -12, where=(y1_vals >= -12), color='red', alpha=0.3)
# Закрашиваем область выше второй прямой (2)
ax.fill_between(x1_vals, y2_vals, 12, where=(y2_vals <= 12), color='green', alpha=0.3)

# Найдем точки пересечения прямых с осями
# Первая прямая (1): точки (0, -4) и (20, 0)
plt.scatter(20, 0 , color='Black', zorder=5)
plt.scatter(0, -4 , color='Black', zorder=5)
plt.scatter(0, 9 , color='Black', zorder=5)
plt.scatter(-9, 0 , color='Black', zorder=5)
ax.text(19.5, 0.5, '20', color='black', fontsize=15)
ax.text(-1, -3.9, '-4', color='black', fontsize=15)
plt.scatter(5, 4 , color='blue', zorder=5)
plt.text(5.2, 3.8, f'{5, 4}', fontsize=15, verticalalignment='bottom', color='blue')

ax.text(-9.1, -1, '-9', color='black', fontsize=15)
ax.text(0.5, 8.7, '9', color='black', fontsize=15)
plt.scatter(0, 0 , color='Black', zorder=5)
plt.text(0.1, -1, f'{0}', fontsize=16, verticalalignment='bottom', color='black')

# Строим вектор
ax.quiver(0, 0, 5, 4, angles='xy', scale_units='xy', scale=1, color='blue')
plt.text(3, 1.5, f'grad f', fontsize=13, verticalalignment='bottom', color='black')

plt.text(3, -3, '(1)', color='red', fontsize=16)   # Подпись для первой прямой
plt.text(-4, 4.4, '(2)', color='green', fontsize=16)   


# Устанавливаем шаг сетки и диапазон
ax.set_xticks(np.arange(-12, 24, 1))
ax.set_yticks(np.arange(-12, 13, 1))
ax.set_xlim(-12, 23)
ax.set_ylim(-12, 12)
ax.grid(True)

# Добавляем координатные оси
ax.axhline(0, color='black', lw=1)  # Горизонтальная ось
ax.axvline(0, color='black', lw=1)  # Вертикальная ось
plt.quiver(0, 0, 23, 0, angles='xy', scale_units='xy', scale=1, color='black', clip_on=False, headwidth=4, headlength=6)
plt.quiver(0, 0, 0, 12, angles='xy', scale_units='xy', scale=1, color='black', clip_on=False, headwidth=4, headlength=6)

plt.text(22, -1.2, 'x1', fontsize=14, ha='center')
plt.text(-1.3, 11, 'x2', fontsize=14, va='center')





# Легенда
ax.legend()
plt.legend(prop={'size': 15})
plt.title('График Области Допустимых Решений (ОДР)')
# Показать график
plt.gca().set_aspect('equal', adjustable='box')
plt.show()
