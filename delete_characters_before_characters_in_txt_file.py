# Укажите путь к исходному файлу
input_file = 'input.txt'

# Укажите путь к файлу, в который будет записан результат
output_file = 'output2.txt'

# Читаем содержимое исходного файла
with open(input_file, 'r', encoding='utf-8') as file:
    lines = file.readlines()

characters = 'hello world'

# Удаляем символы до characters в каждой строке
modified_lines = []
for line in lines:
    if characters in line:
        modified_line = characters + line.split(characters)[-1]
        modified_lines.append(modified_line)
    else:
        modified_lines.append(line)

# Записываем измененные строки в новый файл
with open(output_file, 'w', encoding='utf-8') as file:
    file.writelines(modified_lines)

print(f"Символы удалены. Результат записан в файл: {output_file}")
