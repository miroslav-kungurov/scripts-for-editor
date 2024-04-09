# Укажите путь к исходному файлу
input_file = 'input.txt'

# Укажите путь к файлу, в который будет записан результат
output_file = 'output.txt'

# Читаем содержимое исходного файла
with open(input_file, 'r', encoding='utf-8') as file:
    lines = file.readlines()

# Удаляем дубликаты строк
unique_lines = list(set(lines))

# Записываем уникальные строки в новый файл
with open(output_file, 'w', encoding='utf-8') as file:
    file.writelines(unique_lines)

print(f"Дубликаты удалены. Результат записан в файл: {output_file}")
