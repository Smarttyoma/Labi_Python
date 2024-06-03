import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Функция, которая обновляет график для каждого кадра анимации
def update(frame):
    freq_ratio = frame / 100  # Изменяю соотношение частот от 0 до 1
    t = np.linspace(0, 2*np.pi, 1000)
    x = np.sin(3*t)
    y = np.sin(freq_ratio*t)
    line.set_data(x, y)
    return line,

# Создаю новый график
fig, ax = plt.subplots()
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)
ax.set_aspect('equal', adjustable='box')
ax.grid(True)

# Создаю линию для фигуры Лиссажу
line, = ax.plot([], [], lw=2)

# Создаю анимацию
ani = FuncAnimation(fig, update, frames=100, interval=50, blit=True)

plt.title('Lissajous Figure Animation (3:1)')
plt.xlabel('X')
plt.ylabel('Y')

# Отображение анимации
plt.show()