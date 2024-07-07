import json
import os

def merge_json_files(file_list, output_file):
    merged_data = []
    total_elements = 0
    initial_total_elements = 0

    for file_name in file_list:
        try:
            with open(file_name, 'r', encoding='utf-8') as file:
                data = json.load(file)
                num_elements = len(data)
                initial_total_elements += num_elements
                total_elements += num_elements
                merged_data.extend(data)
                print(f"Файл {file_name} содержит {num_elements} элементов.")
        except json.JSONDecodeError as e:
            print(f"Ошибка декодирования JSON в файле {file_name}: {e}")
        except Exception as e:
            print(f"Произошла ошибка при обработке файла {file_name}: {e}")

    with open(output_file, 'w', encoding='utf-8') as output:
        json.dump(merged_data, output, ensure_ascii=False, indent=4)

    print(f"Исходные файлы содержат всего {initial_total_elements} элементов.")
    print(f"Объединённый файл содержит {len(merged_data)} элементов.")

if __name__ == "__main__":
    # Список JSON файлов для объединения
    json_files = ["file1.json", "file2.json"]
    # Имя выходного файла
    output_json = "merged2.json"

    merge_json_files(json_files, output_json)
    print(f"Файлы успешно объединены в {output_json}")
