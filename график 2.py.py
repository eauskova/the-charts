import numpy as np
import matplotlib.pyplot as plt

# Определяем функцию для уравнения прямой
def line_eq(x, k, b):
    return k * x + b

x1 = np.linspace(-17, 5, 400)
x2 = np.linspace(-17, 5, 400)


# Создаем диапазон значений для оси x
x_vals = np.linspace(-10, 17, 500)

# Определяем границы неравенств
# Неравенство 1: 4*x1 - x2 <= 16 -> x2 >= 4*x1 - 16
y_vals_ineq1 = 4 * x_vals - 16

# Неравенство 2: x1 + x2 >= 3 -> x2 >= 3 - x1
y_vals_ineq2 = 3 - x_vals

# Строим график
plt.figure(figsize=(8, 8))

X1, X2 = np.meshgrid(x1, x2)

# Неравенства системы
ineq1 = 4 * X1 - X2 <= 16  # x1 + 4 * x2 <= 12
ineq2 = X1 + X2 <= 3        # x1 + x2 <= 4

# Добавляем дополнительное условие для положительной четверти
positive_quadrant = (X1 >= 0) & (X2 >= 0)
# Заштриховываем область первого неравенства (все точки ниже прямой)
plt.fill_between(x_vals, y_vals_ineq1, 10, where=(y_vals_ineq1 < 10), color='red', alpha=0.6)

# Заштриховываем область второго неравенства (все точки выше прямой)
plt.fill_between(x_vals, 5, y_vals_ineq2, where=(y_vals_ineq2 < 5), color='green', alpha=0.6)

# Строим прямые, которые соответствуют границам неравенств
plt.plot(x_vals, y_vals_ineq1, label=r'$4x_1 - x_2 = 16$ (1)', color='red')
plt.plot(x_vals, y_vals_ineq2, label=r'$x_1 + x_2 = 3$ (2)', color='green')

plt.scatter([3, 4], [0,0], color='black', zorder=5)
plt.scatter([0], [ 3], color='black', zorder=5)

# Точки пересечения прямых с осями
# Для первой прямой (x2 = 0): 4*x1 = 16 -> x1 = 4
plt.scatter(4, 0, color='black')
plt.text(4.1, 0.1, '4', fontsize=15, verticalalignment='bottom', color='Black')

# Для второй прямой (x2 = 0): x1 + 0 = 3 -> x1 = 3
plt.scatter(3, 0, color='black')
plt.text(3.1, 0.1, '3', fontsize=15, verticalalignment='bottom', color='Black')

# Для второй прямой (x1 = 0): 0 + x2 = 3 -> x2 = 3
plt.scatter(0, 3, color='black')
plt.text(-0.8, 2.7, '3', fontsize=15, verticalalignment='bottom', color='Black')

# Задаем координаты области для заливки 
x_coords = [0, 3, 3.98, 5.22, 0]  # Координаты по оси x
y_coords = [3, 0, 0, 5, 5]  # Координаты по оси y

# Рисуем границы области
plt.plot(x_coords + [x_coords[0]], y_coords + [y_coords[0]], color='orange')

# Закрашиваем область
plt.fill(x_coords, y_coords, 'orange', alpha=0.6, label='ОДР')

#Подпись точек максимума и минимума
plt.scatter(1, 3, color='purple', zorder=5)
plt.text(0.2, 3.1, f'{1, 3}', fontsize=15, verticalalignment='bottom', color='purple')
plt.scatter(0, 0 , color='Black', zorder=1)
plt.text(0.1, -1, f'{0}', fontsize=16, verticalalignment='bottom', color='black')
plt.text(1.7, -1, f'т. min', fontsize=13, verticalalignment='bottom', color='MediumBlue')
plt.scatter(0, -16, color='black', zorder=5)
plt.text(0.3, -16.5, f'{-16}', fontsize=16, verticalalignment='bottom', color='black')
plt.scatter(3, 0 , color='MediumBlue', zorder=5)

# Функция для отображения прямой через точку (3,0), перпендикулярной вектору (1,3)
def plot_perpendicular_line():
    # Угловой коэффициент для перпендикулярной прямой
    k_perpendicular = -13/30
    
    # Прямая через точку (3, 0) с угловым коэффициентом k = -1/3
    x_vals = np.linspace(-5, 17, 400)
    y_vals = k_perpendicular * (x_vals - 3)  # Прямая вида y = k(x - 3)

    # Отображаем перпендикулярную прямую
    plt.plot(x_vals, y_vals, linestyle='--', color='blue', label='Линия уровня Цел. ф-ции в т.min')

    # Прямая через точку (3, 0), перпендикулярная вектору
plot_perpendicular_line()





# Добавляем подписи рядом с прямыми
plt.text(3, -5, '(1)', color='red', fontsize=15)   # Подпись для первой прямой
plt.text(6, -4.5, '(2)', color='green', fontsize=15)   

#Строим градиент
# plt.arrow(0, 0, 2, 3, head_lenght = 0.2, fc = 'purple', ec = 'purple')
plt.quiver(0, 0, 1, 3, angles = 'xy', scale_units='xy', scale=1, color='purple')
plt.text(1, 2, f'grad f', fontsize=13, verticalalignment='bottom', color='black')

# Отображаем оси с помощью стрелок
plt.quiver(0, 0, 17, 0, angles='xy', scale_units='xy', scale=1, color='black', clip_on=False, headwidth=4, headlength=6)
plt.quiver(0, 0, 0, 5, angles='xy', scale_units='xy', scale=1, color='black', clip_on=False, headwidth=4, headlength=6)

plt.text(16, 0.5, 'x1', fontsize=14, ha='center')
plt.text(-1.3, 4.5, 'x2', fontsize=14, va='center')

plt.xticks(np.arange(-7, 17, 1))  # Шаг 1 для оси x
plt.yticks(np.arange(-17, 5, 1))  # Шаг 1 для оси y

plt.axhline(0, color='black', linewidth=1.5)
plt.axvline(0, color='black', linewidth=1.5)
# Настройка сетки и легенды
plt.grid(True)
plt.legend(loc='upper right')
plt.xlim(-3, 17)
plt.ylim(-17, 5)

plt.legend(prop={'size': 10})

# Заголовок и оси
plt.title('График Области Допустимых Решений (ОДР)')


# Показываем график
plt.show()
