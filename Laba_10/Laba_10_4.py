import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
import ipywidgets as widgets
from IPython.display import display

# Создаение данных для волн
x = np.linspace(0, 2*np.pi, 1000)
wave1 = np.sin(x)
wave2 = np.sin(x + np.pi/2)  # Добавляем смещение в 90 градусов

# Создание интерактивных окон для задания исходных волн
fig1, ax1 = plt.subplots()
ax1.set_title('Исходная волна 1')
line1, = ax1.plot(x, wave1, color='blue', lw=2)  # Синяя линия толщиной 2

fig2, ax2 = plt.subplots()
ax2.set_title('Исходная волна 2')
line2, = ax2.plot(x, wave2, color='red', lw=2)   # Красная линия толщиной 2

# Создание окна для отображения результата сложения волн
fig3, ax3 = plt.subplots()
ax3.set_title('Результат сложения волн')
line3, = ax3.plot(x, wave1 + wave2, color='green', lw=2)  # Зеленая линия толщиной 2

# Создание слайдеров для регулировки частоты и амплитуды волн
freq_slider = widgets.FloatSlider(value=1.0, min=0.1, max=10.0, step=0.1, description='Частота:')
amp_slider = widgets.FloatSlider(value=1.0, min=0.1, max=5.0, step=0.1, description='Амплитуда:')

# Функция для обновления графиков при изменении слайдеров
def update_wave1(change):
    freq = freq_slider.value
    amp = amp_slider.value
    line1.set_ydata(amp * np.sin(freq * x))
    line3.set_ydata(line1.get_ydata() + line2.get_ydata())
    fig1.canvas.draw_idle()
    fig3.canvas.draw_idle()

def update_wave2(change):
    freq = freq_slider.value
    amp = amp_slider.value
    line2.set_ydata(amp * np.sin(freq * x + np.pi/2))  # Добавляем смещение в 90 градусов
    line3.set_ydata(line1.get_ydata() + line2.get_ydata())
    fig2.canvas.draw_idle()
    fig3.canvas.draw_idle()

freq_slider.observe(update_wave1, names='value')
amp_slider.observe(update_wave1, names='value')
freq_slider.observe(update_wave2, names='value')
amp_slider.observe(update_wave2, names='value')

# Отображаем слайдеры
display(widgets.VBox([freq_slider, amp_slider]))

plt.show()