import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Создаю данные
x = np.linspace(0, 10, 100)
y = np.linspace(0, 10, 100)
X, Y = np.meshgrid(x, y)
Z = np.sin(X) + np.cos(Y)  # Пример функции для отрисовки

# Вычисление среднеквадратичного отклонения (MSE)
mse = np.sqrt(np.mean(Z**2))

# Создание двух трехмерных графиков
fig = plt.figure(figsize=(12, 6))

# График 1: обычный масштаб
ax1 = fig.add_subplot(121, projection='3d')
ax1.plot_surface(X, Y, Z, cmap='viridis')
ax1.set_title('MSE - Обычный масштаб')

# График 2: логарифмический масштаб по оси Z
Z_abs = np.abs(Z)  # Применение абсолютного значения к Z
Z_abs[Z_abs == 0] = 1e-10  # Замена нулей небольшими положительными значениями для избежания логарифма от нуля
ax2 = fig.add_subplot(122, projection='3d')
ax2.plot_surface(X, Y, np.log(Z_abs), cmap='viridis')  # Применение логарифма к Z_abs
ax2.set_title('MSE - Логарифмический масштаб по оси Z')

plt.show()