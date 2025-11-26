#!/usr/bin/env python3
import json
import sys

class JsonFileHandler:

    @staticmethod
    def load(file_path):
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            print(f"Ошибка: файл '{file_path}' не найден.")
            sys.exit(1)
        except json.JSONDecodeError as e:
            print(f"Ошибка: некорректный JSON")
            sys.exit(1)

    @staticmethod
    def save(data, file_path):
        try:
            with open(file_path, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
        except Exception as e:
            print(f"Ошибка при сохранении файла ")
            sys.exit(1)

def build_values_map(values_data):
    """Создает словарь для быстрого поиска значений по id"""
    return {item['id']: item['value'] for item in values_data.get('values', [])}

def fill_values(test_item, values_map):
    """Рекурсивно заполняет значения в структуре теста"""
    if isinstance(test_item, dict):
        if 'id' in test_item and test_item['id'] in values_map:
            test_item['value'] = values_map[test_item['id']]
        if 'values' in test_item:
            test_item['values'] = fill_values(test_item['values'], values_map)
        return test_item
    elif isinstance(test_item, list):
        return [fill_values(item, values_map) for item in test_item]
    return test_item

def main():
    if len(sys.argv) != 4:
        sys.exit(1)

    test_file, values_file, report_file = sys.argv[1], sys.argv[2], sys.argv[3]

    tests = JsonFileHandler.load(test_file)
    values = JsonFileHandler.load(values_file)


    values_map = build_values_map(values)

    
    report = tests.copy()
    if 'tests' in report:
        report['tests'] = fill_values(report['tests'], values_map)

    JsonFileHandler.save(report, report_file)

if __name__ == "__main__":
    main()
