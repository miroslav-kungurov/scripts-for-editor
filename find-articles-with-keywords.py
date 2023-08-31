import requests
from bs4 import BeautifulSoup
import re

# Список ключевых слов для поиска
keywords = ['AI']

# Открываем файл urls.txt и читаем адреса страниц
with open('urls.txt', 'r', encoding='utf-8') as file:
    urls = file.readlines()

# Создаем или открываем файл result.txt для записи найденных ссылок
result_file = open('result.txt', 'w', encoding='utf-8')


# Проходим по каждому адресу страницы
for url in urls:
    url = url.strip()  # Удаляем лишние пробелы и символы новой строки
    response = requests.get(url)

    if response.status_code == 200:
        page_content = response.text

        soup = BeautifulSoup(page_content, 'html.parser')

        # Ищем текст на странице и проверяем наличие ключевых слов
        page_text = soup.get_text()
        for keyword in keywords:
            pattern = rf'(?<!\w){re.escape(keyword)}(?!\w)'
            if re.findall(pattern, page_text):
                print(f"Слово '{keyword}' найдено на странице: {url}")
                result_file.write(f"{keyword}  ——————  {url}\n")  # Записываем ссылку в файл result.txt



# Закрываем файл result.txt
result_file.close()
