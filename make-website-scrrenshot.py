import os
from datetime import datetime
from urllib.parse import urlparse
from playwright.sync_api import sync_playwright

def take_screenshot(url, output_dir):
    # Извлекаем имя сайта из URL
    parsed_url = urlparse(url)
    website_name = parsed_url.netloc.split(".")[-2]

    # Генерируем имя файла
    file_name = website_name + ".jpg"
    counter = 1
    while os.path.exists(os.path.join(output_dir, file_name)):
        file_name = f"{website_name}{counter}.jpg"
        counter += 1

    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(viewport={"width": 1920, "height": 1080})
        page.goto(url)
        page.screenshot(path=os.path.join(output_dir, file_name), type="jpeg", quality=100)
        browser.close()

    print(f"Screenshot saved as {file_name}")

def process_urls_from_file(file_path, output_dir):
    with open(file_path, "r") as file:
        urls = file.readlines()

    for url in urls:
        url = url.strip()
        if url:
            take_screenshot(url, output_dir)

def create_output_directory():
    # Получаем текущую дату
    current_date = datetime.now().strftime("%d-%m-%Y")

    # Создаем имя папки с текущей датой
    output_dir = current_date

    # Создаем папку, если она не существует
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    return output_dir

# Запуск
file_path = "urls.txt"
output_dir = create_output_directory()
process_urls_from_file(file_path, output_dir)
