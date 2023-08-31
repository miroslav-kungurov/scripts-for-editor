import requests
from bs4 import BeautifulSoup

keywords = ['google.com']

with open('urls.txt', 'r', encoding='utf-8') as f:
    urls = f.readlines()

result_file = open('result.txt', 'w', encoding='utf-8')

for url in urls:
    url = url.strip()
    try:
        response = requests.get(url)
        if response.status_code == 200 and response.text:
            soup = BeautifulSoup(response.text, 'html.parser')
            links = soup.find_all('a')
            if links:
                for link in links:
                    link_text = link.get('href')
                    if link_text:
                        for keyword in keywords:
                            if keyword in link_text:
                                print(f"Найдено: {keyword}, Ссылка: {link_text}")
                                result_file.write(f"{link_text}\n")

    except UnicodeEncodeError as e:
        print(f"Encoding error on page {url}: {e}")

result_file.close()
