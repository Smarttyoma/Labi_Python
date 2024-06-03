import csv
import os
import random

class CSVProcessor:
    def __init__(self, filename):
        self.filename = filename
        self.data = self.load_data()

    def load_data(self):
        with open(self.filename, 'r', newline='') as file:
            reader = csv.reader(file)
            data = list(reader)
        return data

    def show(self, display_type='top', num_rows=5, separator=','):
        if display_type == 'top':
            rows = self.data[:num_rows]
        elif display_type == 'bottom':
            rows = self.data[-num_rows:]
        elif display_type == 'random':
            rows = random.sample(self.data[1:], min(num_rows, len(self.data[1:])))
        else:
            print("Неверный тип отображения. Допустимые значения: 'top', 'bottom', 'random'")
            return

        for row in rows:
            print(separator.join(row))

    def info(self):
        num_rows = len(self.data) - 1  # Вычитаем заголовок
        num_columns = len(self.data[0])

        print(f"Количество строк с данными: {num_rows}, количество колонок в таблице: {num_columns}")

        header = self.data[0]
        data_types = ['string'] * num_columns  # По умолчанию все типы данных - строки
        for row in self.data[1:]:
            for i, value in enumerate(row):
                if value.strip():  # Проверяем, не пустое ли значение
                    if data_types[i] == 'string' and value.isdigit():
                        data_types[i] = 'int'
        print("\nСписок имен полей данных с количеством не пустых значений и типом значений:")
        for name, data_type in zip(header, data_types):
            print(f"{name:10} {num_rows:4} {data_type}")

    def del_nan(self):
        cleaned_data = [row for row in self.data if all(row)]
        return cleaned_data

    def make_ds(self):
        random.shuffle(self.data)
        num_rows = len(self.data)
        train_size = int(0.7 * num_rows)

        train_data = self.data[:train_size]
        test_data = self.data[train_size:]

        # Создаем папки Learning и Testing в месте расположения файла программы
        base_dir = os.path.dirname(os.path.abspath(__file__))
        learning_dir = os.path.join(base_dir, 'workdata', 'Learning')
        testing_dir = os.path.join(base_dir, 'workdata', 'Testing')
        os.makedirs(learning_dir, exist_ok=True)
        os.makedirs(testing_dir, exist_ok=True)

        # Записываем файлы train.csv и test.csv
        with open(os.path.join(learning_dir, 'train.csv'), 'w', newline='') as train_file:
            writer = csv.writer(train_file)
            writer.writerows(train_data)

        with open(os.path.join(testing_dir, 'test.csv'), 'w', newline='') as test_file:
            writer = csv.writer(test_file)
            writer.writerows(test_data)

# Пример использования
csv_processor = CSVProcessor('Titanic.csv')
csv_processor.show(display_type='random', num_rows=3, separator=' | ')
csv_processor.info()
cleaned_data = csv_processor.del_nan()
print(cleaned_data)
csv_processor.make_ds()
