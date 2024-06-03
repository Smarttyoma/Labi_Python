import numpy as np
import matplotlib.pyplot as plt
from scipy.special import legendre

# Задаю массив значений x
x = np.linspace(-1, 1, 100)

# Задаю степени полиномов Лежандра
degrees = [1, 2, 3, 4, 5, 6, 7]

# Создаю новый график
plt.figure()

# Для каждой степени полинома Лежандра
for degree in degrees:
    # Вычисляю значения полинома Лежандра заданной степени
    y = legendre(degree)(x)

    # Построение график полинома с указанием степени в легенде
    plt.plot(x, y, label=f'n = {degree}')

# Задаю заголовок графика
plt.title('Полиномы Лежандра')

# Добавление легенду
plt.legend()

# График
plt.show()