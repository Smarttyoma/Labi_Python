# Задание 1

import numpy as np

# Сохранение текста в файл
text = """3,4,17,-3
          5,11,-1,6
          0,2,-5,8"""

with open("input1.txt", "w") as file:
    file.write(text)

# Чтение матрицы из файла
matrix = np.loadtxt("input1.txt", delimiter=",")

# Вывод матрицы
print("Матрица:")
print(matrix)

# Нахождение суммы всех элементов
sum_all = np.sum(matrix)

# Нахождение максимального и минимального элементов
max_element = np.max(matrix)
min_element = np.min(matrix)

# Вывод результатов
print("\nСумма всех элементов:", sum_all)
print("Максимальный элемент:", max_element)
print("Минимальный элемент:", min_element)

# Задание 2


def run_length_encoding(x):
    if len(x) == 0:
        return (np.array([]), np.array([]))

    values = [x[0]]
    counts = [1]

    for i in range(1, len(x)):
        if x[i] == x[i - 1]:
            counts[-1] += 1
        else:
            values.append(x[i])
            counts.append(1)

    return (np.array(values), np.array(counts))


# Пример использования
x = np.array([2, 2, 2, 3, 3, 3, 5])
encoded = run_length_encoding(x)

print(f"Оригинальный вектор: {x}")
print(f"Закодированный вектор: {encoded}")

# Задание 3

# Генерация массива случайных чисел нормального распределения размера 10x4
np.random.seed(0)  # Установка начального значения для воспроизводимости результатов
array = np.random.randn(10, 4)

# Нахождение минимального, максимального, средних значений и стандартного отклонения
min_value = np.min(array)
max_value = np.max(array)
mean_value = np.mean(array)
std_deviation = np.std(array)

# Сохранение первых 5 строк в отдельную переменную
first_five_rows = array[:5]

# Вывод результатов
print("Сгенерированный массив:\n", array)
print("Минимальное значение:", min_value)
print("Максимальное значение:", max_value)
print("Среднее значение:", mean_value)
print("Стандартное отклонение:", std_deviation)
print("Первые 5 строк массива:\n", first_five_rows)

# Задание 4

def max_element_after_zero(x):
    # Нахожу индексы всех нулевых элементов
    zero_indices = np.where(x == 0)[0]

    # Переменная для хранения максимального значения
    max_value = float('-inf')

    # Прохожу по индексам нулевых элементов
    for index in zero_indices:
        # Проверяю, что нулевой элемент не является последним
        if index + 1 < len(x):
            # Обновляю максимальное значение, если текущий элемент больше
            max_value = max(max_value, x[index + 1])

    # Если не было найдено ни одного элемента после нуля, возвращаю None
    if max_value == float('-inf'):
        return None
    else:
        return max_value


# Пример использования
x = np.array([6, 2, 0, 3, 0, 0, 5, 7, 0])
result = max_element_after_zero(x)

print(f"Максимальный элемент после нуля в векторе {x} -> {result}")

# Задание 5


def multivariate_normal_logpdf(X, m, C):
    # Размерность данных
    N, D = X.shape

    # Вычисление обратной матрицы и определителя ковариационной матрицы
    C_inv = np.linalg.inv(C)
    C_det = np.linalg.det(C)

    # Вычисление частей экспоненты
    exponent = -0.5 * np.sum((X - m) @ C_inv * (X - m), axis=1)

    # Вычисление логарифма плотности
    log_density = -0.5 * D * np.log(2 * np.pi) - 0.5 * np.log(C_det) + exponent

    return log_density


# Пример использования
X = np.array([[1, 2], [2, 3], [3, 4]])
m = np.array([2, 3])
C = np.array([[2, 1], [1, 2]])
result = multivariate_normal_logpdf(X, m, C)
print("Логарифм плотности многомерного нормального распределения:", result)

from scipy.stats import multivariate_normal
import time

# Генерация тестовых данных
N = 1000
D = 10
X = np.random.randn(N, D)
m = np.random.randn(D)
C = np.random.randn(D, D)
C = np.dot(C, C.T)  # Сделаем матрицу ковариации положительно определенной

# Замер времени выполнения вашей функции
start_time = time.time()
result_custom = multivariate_normal_logpdf(X, m, C)
custom_duration = time.time() - start_time

# Замер времени выполнения scipy функции
start_time = time.time()
result_scipy = multivariate_normal(m, C).logpdf(X)
scipy_duration = time.time() - start_time

# Проверка результатов
print("Сравнение результатов:")
print("Количество различий в результатах:", np.sum(np.abs(result_custom - result_scipy) > 1e-8))
print("Среднее абсолютное различие в результатах:", np.mean(np.abs(result_custom - result_scipy)))
print("Время выполнения моей функции:", custom_duration)
print("Время выполнения scipy функции:", scipy_duration)

# Задание 5

# Создание массива a
a = np.arange(16).reshape(4, 4)

# Вывод массива до замены строк
print("Массив до замены строк:")
print(a)

# Меняю местами строки 1 и 3
a[[1, 3]] = a[[3, 1]]

# Вывод массива после замены строк
print("\nМассив после замены строк:")
print(a)

# Задание 7

# Загрузка данных
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
iris = np.genfromtxt(url, delimiter=',', dtype='object')

# Получение столбца species
species_column = iris[:, 4]

# Нахождение уникальных значений и их количество
unique_values, counts = np.unique(species_column, return_counts=True)

# Вывод результатов
print("Уникальные значения в столбце 'species':", unique_values)
print("Количество каждого уникального значения:", counts)

# Задание 8

import numpy as np

# Исходный массив
arr = [0, 1, 2, 0, 0, 4, 0, 6, 9]

# Находим индексы ненулевых элементов
nonzero_indices = np.nonzero(arr)[0]

# Вывод результатов
print("Индексы ненулевых элементов:", nonzero_indices)