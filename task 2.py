import json
import csv


INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    L = []
    with open(INPUT_FILENAME, 'r', encoding='utf-8') as f:
        file_csv = csv.DictReader(f)
        for i in file_csv:
            L.append(i)
        with open(OUTPUT_FILENAME, 'w', encoding='utf-8') as j:
            json_data = json.dumps(L, indent=4, ensure_ascii=False)
            j.write(json_data)

    # TODO считать содержимое csv файла

    # TODO Сериализовать в файл с отступами равными 4


if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
