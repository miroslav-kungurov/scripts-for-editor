import os
import requests
from bs4 import BeautifulSoup
from readability.readability import Document
from markdownify import markdownify
from urllib.parse import urlparse

def convert_to_markdown(url):
    # Получаем HTML-содержимое страницы
    response = requests.get(url)
    html_content = response.text

    # Используем библиотеку readability для извлечения основного содержимого статьи
    doc = Document(html_content)
    article_html = doc.summary()

    # Создаем объект BeautifulSoup для парсинга HTML
    soup = BeautifulSoup(article_html, 'html.parser')

    # Конвертируем HTML в Markdown
    markdown_content = markdownify(str(soup), strip=['img', 'iframe'])

    return markdown_content

def get_page_title(url):
    # Получаем HTML-содержимое страницы
    response = requests.get(url)
    html_content = response.text

    # Создаем объект BeautifulSoup для парсинга HTML
    soup = BeautifulSoup(html_content, 'html.parser')

    # Извлекаем заголовок страницы
    page_title = soup.title.string if soup.title else ''

    return page_title

def save_to_file(url, markdown_content):
    # Получаем название страницы из URL
    parsed_url = urlparse(url)
    page_name = parsed_url.path.split('/')[-1] or 'index'

    # Создаем папку "html to markdown", если она не существует
    os.makedirs('html to markdown', exist_ok=True)

    # Формируем путь к файлу
    file_path = os.path.join('html to markdown', f'{page_name}.md')

    # Сохраняем содержимое в файл
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(f'# {get_page_title(url)}\n\n')
        file.write(markdown_content)

    print(f'Файл сохранен: {file_path}')

# Пример использования
url = 'https://dev.to/glasskube/the-guide-to-git-i-never-had-1450'
markdown_output = convert_to_markdown(url)
save_to_file(url, markdown_output)
