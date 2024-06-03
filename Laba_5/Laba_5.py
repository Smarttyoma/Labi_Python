# Задание 1

with open("input.txt", "r") as file:
    numbers = [int(num) for num in file.readline().split()]

# Вычисление произведения чисел
proiz = 1
for num in numbers:
    proiz *= num

# Запись произведения в файл output.txt
with open("output.txt", "w") as file:
    file.write(str(proiz))

# Задание 2

with open("input2.txt", "r") as file:
    numbers = [int(line.strip()) for line in file]

# Сортировка чисел по возрастанию цифр
sorted_numbers = sorted(numbers, key=lambda x: sorted(str(x)))

# Запись отсортированных чисел в файл output2.txt
with open("output2.txt", "w") as file:
    for number in sorted_numbers:
        file.write(str(number) + "\n")

# Задание 3

# Чтение данных о детях из файла input3.txt
with open("input3.txt", "r") as file:
    children_data = [line.strip() for line in file]

# Преобразование возраста ребенка из последнего символа строки
children_ages = []
for child_info in children_data:
    age = int(child_info[-1])
    children_ages.append(age)

# Нахождение индекса самого старшего и самого младшего ребенка
samiy_st = children_ages.index(max(children_ages))
samiy_ml = children_ages.index(min(children_ages))

# Запись данных о самом старшем ребенке в файл samiy_st.txt
with open("samiy_st.txt", "w") as file:
    file.write(children_data[samiy_st])

# Запись данных о самом младшем ребенке в файл samiy_ml.txt
with open("samiy_ml.txt", "w") as file:
    file.write(children_data[samiy_ml])

# Задание 4

import json
import csv
import os
import sys

def json_to_csv(json_file):
    # Определяем имя для CSV-файла на основе имени JSON-файла
    csv_file_name = os.path.splitext(json_file)[0] + '.csv'

    # Открываем JSON-файл для чтения
    with open(json_file, 'r') as jfile:
        data = json.load(jfile)

    # Проверяем, является ли корневой элемент словарем
    if not isinstance(data, dict):
        print("Ошибка: Корневой элемент JSON не является словарем.")
        return

    # Открываем CSV-файл для записи
    with open(csv_file_name, 'w', newline='', encoding='utf-8') as cfile:
        writer = csv.DictWriter(cfile, fieldnames=data.keys())

        # Записываем заголовки в CSV-файл
        writer.writeheader()

        # Записываем данные из JSON-файла в CSV-файл
        writer.writerow(data)

    print(f"Файл {csv_file_name} успешно создан.")

def main():
    # Имя JSON-файла известно заранее: Sample-employee-JSON-data.json
    json_file = "Sample-employee-JSON-data.json"

    # Преобразуем JSON в CSV
    json_to_csv(json_file)

if __name__ == "__main__":
    main()