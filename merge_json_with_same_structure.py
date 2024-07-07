import json
import os

def merge_json_files(file_list, output_file):
    merged_data = []

    for file_name in file_list:
        try:
            with open(file_name, 'r', encoding='utf-8') as file:
                data = json.load(file)
                merged_data.extend(data)
        except json.JSONDecodeError as e:
            print(f"Ошибка декодирования JSON в файле {file_name}: {e}")
        except Exception as e:
            print(f"Произошла ошибка при обработке файла {file_name}: {e}")

    with open(output_file, 'w', encoding='utf-8') as output:
        json.dump(merged_data, output, ensure_ascii=False, indent=4)


if __name__ == "__main__":
    # Список JSON файлов для объединения
    json_files = ["file1.json", "file2.json"]
    # Имя выходного файла
    output_json = "merged.json"

    merge_json_files(json_files, output_json)
    print(f"Файлы успешно объединены в {output_json}")
