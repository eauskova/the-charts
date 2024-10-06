import numpy as np
import matplotlib.pyplot as plt
from fractions import Fraction

#ax = plt.subplots()
# Функция для отображения точек пересечения
def plot_intersection_points():
    # Пересечения прямых с осями координат
    x1_intercept_ineq1 = 4  # 4x1-x2=16 при x2 = 0
    x2_intercept_ineq1 = -16  # 4x1-x2=16 при x1 = 0
    
    x1_intercept_ineq2 = 3  # x1 + x2 = 3 при x2 = 0
    x2_intercept_ineq2 = 3  # x1 + x2 = 3 при x1 = 0

    # Точка пересечения прямых
    #x2_intersection = Fraction(8, 3)
    #x1_intersection = 4 - x2_intersection

    # Отображаем точки пересечения прямых с осями
    plt.scatter([x1_intercept_ineq1, x1_intercept_ineq2], [0,0], color='black', zorder=5)
    plt.scatter([0,0], [x2_intercept_ineq1, x2_intercept_ineq2], color='black', zorder=5)

    # Отображаем точку пересечения двух прямых
    #plt.scatter(float(x1_intersection), float(x2_intersection), color='MediumBlue', zorder=5)

    # Подписываем точки пересечения
    plt.text(x1_intercept_ineq1, 0, f'{x1_intercept_ineq1}', fontsize=14, verticalalignment='bottom')
    plt.text(x1_intercept_ineq2, 0, f'{x1_intercept_ineq2}', fontsize=14, verticalalignment='bottom')
    plt.text(-0.2, int(x2_intercept_ineq1), f'{int(x2_intercept_ineq1)}', fontsize=14, horizontalalignment='right')
    plt.text(-0.2, int(x2_intercept_ineq2), f'{int(x2_intercept_ineq2)}', fontsize=14, horizontalalignment='right')

    #Подпись точек максимума и минимума
    #plt.scatter(2, 3, color='Fuchsia', zorder=5)
    #plt.text(1.3, 3.1, f'{2, 3}', fontsize=15, verticalalignment='bottom', color='Fuchsia')
    plt.scatter(0, 0, color='Purple', zorder=5)
    plt.text(0.1, -0.8, f'{0,0}', fontsize=16, verticalalignment='bottom', color='Purple')
    #plt.text(-1.7, -0.6, f'т. min', fontsize=13, verticalalignment='bottom', color='Purple')
    #plt.text(-0.5, 2.2, f'т. max', fontsize=13, verticalalignment='bottom', color='MediumBlue')


    #Строим градиент
    # plt.arrow(0, 0, 2, 3, head_lenght = 0.2, fc = 'purple', ec = 'purple')
    #plt.quiver(0, 0, 2, 3, angles = 'xy', scale_units='xy', scale=1, color='Fuchsia')
    plt.text(0.7, 0.7, f'grad f', fontsize=13, verticalalignment='bottom', color='black')
    

    
    #проведем перепендикуляр к 0
    m_parallel = - 2 / 3  # Наклон параллельной прямой
    x_parallel = np.linspace(-10, 10, 400)
    y_parallel = m_parallel * x_parallel  # Уравнение параллельной прямой
    #plt.plot(x_parallel, y_parallel, linestyle='--', color='Purple', label='Линия уровня Цел. ф-ции в т.min')


    #Проведем перпендикуляр к точке (4/3, 8/3)
    def line_eq(x, k, x0, y0):
        return k * (x - x0) + y0

    # Коэффициент наклона прямой (параллельно исходной)
    k = - 2 / 3

    # Координаты точки, через которую проходит прямая
    x0 = 4 / 3
    y0 = 8 / 3

    # Создаем диапазон значений для оси x
    x_vals = np.linspace(-10, 10, 500)

    # Находим соответствующие значения для оси y для новой прямой
    y_vals = line_eq(x_vals, k, x0, y0)
    #plt.plot(x_vals, y_vals, label=r'Линия уровня Цел. ф-ции в т.max', linestyle='--', color='MediumBlue')


    # Подписываем точку пересечения двух прямых
    #plt.text(float(x1_intersection) + 0.3, float(x2_intersection) - 0.4, f'({x1_intersection}, {x2_intersection})', fontsize=16, color='MediumBlue')

# Создаем сетку значений для x1 и x2
x1 = np.linspace(-17, 5, 400)
x2 = np.linspace(-17, 5, 400)

# Создаем сетку для расчета значений
X1, X2 = np.meshgrid(x1, x2)

# Неравенства системы
ineq1 = 4 * X1 - X2 <= 16  # x1 + 4 * x2 <= 12
ineq2 = X1 + X2 <= 3        # x1 + x2 <= 4

# Добавляем дополнительное условие для положительной четверти
positive_quadrant = (X1 >= 0) & (X2 >= 0)

# График
plt.figure(figsize=(8, 8))

# Закрашиваем область пересечения
#plt.imshow(ineq1 & ineq2 & positive_quadrant, extent=(-3.2, 14.5, -3.2, 14.5), origin="lower", cmap="Oranges", alpha=0.6)

# Закрашиваем область ниже первой прямой (1)
#plt.imshow(X2 < (12 - X1) / 4, extent=(-3, 14, -3, 14), origin="lower", cmap="Reds", alpha=0.3)

# Закрашиваем область ниже второй прямой (2)
#plt.imshow(X2 < 4 - X1, extent=(-3, 14, -3, 14), origin="lower", cmap="Greens", alpha=0.3)

# Строим границы неравенств
plt.plot(x1, - (16 - x1/4), label=r'$x_1 + 4x_2 \leq 12$ (1)', color='red')  # x1 + 4 * x2 <= 12
plt.plot(x1, 3 - x1, label=r'$x_1 + x_2 \leq 4$ (2)', color='green')
#plt.plot(label=r'ОДР', color='orange')         # x1 + x2 <= 4

# Вызов функции для отображения точек пересечения
#plot_intersection_points()

# Добавляем подписи рядом с прямыми
#plt.text(5, (12 - 5) / 4, '(1)', color='red', fontsize=15)   # Подпись для первой прямой
#plt.text(6, -2, '(2)', color='green', fontsize=15)        # Подпись для второй прямой

# Подписи и границы
plt.xlim(-3, 14)
plt.ylim(-17, 5)

# Установка шагов сетки
plt.xticks(np.arange(-3, 14, 1))  # Шаг 1 для оси x
plt.yticks(np.arange(-17, 5, 1))  # Шаг 1 для оси y

# Отображение осей в центре
plt.axhline(0, color='black', linewidth=1.5)
plt.axvline(0, color='black', linewidth=1.5)


# Задаем координаты области для заливки 
#x_coords = [0, 0, 4/3, 4]  # Координаты по оси x
#y_coords = [0, 3, 8/3, 0]  # Координаты по оси y

# Рисуем границы области
#plt.plot(x_coords + [x_coords[0]], y_coords + [y_coords[0]], color='orange')

# Закрашиваем область
#plt.fill(x_coords, y_coords, 'orange', alpha=0.6, label='ОДР')

# Легенда
plt.legend(loc='upper right')
#plt.title('Закрашенная область с заданными координатами')


# Легенда
plt.legend(prop={'size': 14})
#plt.title('График Области Допустимых Решений (ОДР)')

plt.quiver(0, 0, 14, 0, angles='xy', scale_units='xy', scale=1, color='black', clip_on=False, headwidth=8, headlength=8)
plt.quiver(0, 0, 0, 5, angles='xy', scale_units='xy', scale=1, color='black', clip_on=False, headwidth=8, headlength=8)

plt.text(13.5, 0.6, 'x1', fontsize=14, ha='center')
plt.text(-1.1, 13.5, 'x2', fontsize=14, va='center')



# Показываем график
plt.grid(True)
plt.show()

