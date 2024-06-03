# Задание 1
def count(numbers):
    uniq_numbers = set(numbers)
    return len(uniq_numbers)


# Ввод значений и преобразование в список целых чисел
input_string = input("Введите числа через запятую: ")
numbers = list(map(int, input_string.split(',')))

# Подсчет количества различных чисел
uniq_count = count(numbers)

print(f"Выходные значения: {uniq_count}")

# Задание 2
def is_subset(set1, set2):
    # Проверяем, является ли set1 подмножеством set2 и что множества не совпадают
    return set1.issubset(set2) and set1 != set2


# Ввод первого множества с клавиатуры
input_set1 = input("Введите первое множество чисел через запятую: ")
set1 = set(map(int, input_set1.split(',')))

# Ввод второго множества с клавиатуры
input_set2 = input("Введите второе множество чисел через запятую: ")
set2 = set(map(int, input_set2.split(',')))

# Проверка, является ли первое множество подмножеством второго
result = is_subset(set1, set2)

# Вывод результата
print(result)

# Задание 3

# Ввод количества городов
n = int(input("Введите максимальное количество названных городов: "))

# Множество для хранения названных городов
cities = set()

for i in range(n):
    city = input("Введите название города: ").strip()

    # Проверка, был ли город уже назван
    if city in cities:
        print("REPEAT")
    else:
        print("OK")
        cities.add(city)

# Задание 4

# Ввод строки текста с клавиатуры
text = input("Введите строку текста: ")

# Разделение текста на слова
words = text.split()

# Словарь для хранения количества вхождений каждого слова
word_count = {}

# Список для хранения результатов
results = []

for word in words:
    # Получаю текущее количество вхождений слова
    count = word_count.get(word, 0)

    # Добавляю текущее количество в результаты
    results.append(count)

    # Увеличиваю количество вхождений слова на 1
    word_count[word] = count + 1

# Вывод результатов
print(" ".join(map(str, results)))

# Задание 5

# Ввод количества записей о покупках
n = int(input("Введите количество записей о покупках: "))

# Словарь для хранения списка покупок каждого покупателя
sl = {}

# Цикл для ввода записей о покупках
for i in range(n):
    entry = input("Введите запись о покупке в формате 'ID Покупателя Товар Количество': ")
    customer_id, item, quantity = entry.split()
    customer_id = int(customer_id)
    quantity = int(quantity)

    # Если покупатель уже есть в словаре, добавляем покупку к его списку
    if customer_id in sl:
        sl[customer_id].append((item, quantity))
    else:
        # Если покупателя еще нет в словаре, создаем новую запись
        sl[customer_id] = [(item, quantity)]

# Вывод списка покупок для каждого покупателя
for customer_id, items in sl.items():
    print(f"Покупатель {customer_id}:")
    for item, quantity in items:
        print(f"{item}: {quantity}")

# Задание 6

# Ввод строки текста с клавиатуры
text = input("Введите текст: ")

# Разделение текста на слова и подсчет их вхождений
word_count = {}
words = text.split()
for word in words:
    word_count[word] = word_count.get(word, 0) + 1

# Сортировка слов по убыванию их количества появления, а при равенстве - в лексикографическом порядке
sorted_words = sorted(word_count.items(), key=lambda x: (-x[1], x[0]))

# Вывод отсортированных слов
for word, count in sorted_words:
    print(word)