# Открываем файл urls.txt для чтения
with open('input.txt', 'r') as file:
    # Читаем все строки из файла
    urls = file.readlines()

# Создаем новый список для обновленных URL
updated_urls = []

# Итерируемся по каждой строке и добавляем префикс
characters = 'hello'
for url in urls:
    updated_url = characters + url.strip()
    updated_urls.append(updated_url)

# Открываем файл urls.txt для записи
with open('input.txt', 'w') as file:
    # Записываем обновленные URL в файл
    file.write('\n'.join(updated_urls))

print("Файл urls.txt успешно обновлен!")