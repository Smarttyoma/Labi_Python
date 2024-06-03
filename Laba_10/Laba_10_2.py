import numpy as np
import matplotlib.pyplot as plt


# Функция для построения фигур Лиссажу с заданными соотношениями частот
def lf(freq_ratio):
    # Диапазон значений параметра t
    t = np.linspace(0, 2 * np.pi, 1000)

    # Вычисление значения для оси X и Y с разными частотами
    x = np.sin(3 * t)
    y = np.sin(freq_ratio * t)

    # Построение фигуру Лиссажу
    plt.plot(x, y)
    plt.title(f'Lissajous Figure (3:{freq_ratio})')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.grid(True)


# Создаю новый график с 2x2 подграфиками
plt.figure(figsize=(10, 8))

# Построение фигуры Лиссажу с разными соотношениями частот в каждом подграфике
plt.subplot(2, 2, 1)
lf(2)

plt.subplot(2, 2, 2)
lf(4)

plt.subplot(2, 2, 3)
lf(5)

plt.subplot(2, 2, 4)
lf(6)

# Отображение графика
plt.tight_layout()
plt.show()