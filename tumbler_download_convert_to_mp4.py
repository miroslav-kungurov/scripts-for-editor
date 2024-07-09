import requests
from moviepy.editor import VideoFileClip
import random
import string

def download_gif(url):
    # Отправляем GET запрос
    response = requests.get(url)

    # Проверяем успешность запроса
    if response.status_code == 200:
        # Сохраняем видео в файл
        with open("video.gifv", "wb") as file:
            file.write(response.content)
        print("Видео успешно скачано и сохранено как video.gifv")
    else:
        print(f"Не удалось скачать видео. Статус код: {response.status_code}")



def generate_file_name():
    lowercase_chars = string.ascii_lowercase
    digits = string.digits
    name = ''

    for _ in range(20):
        char_type = random.randint(0, 1)
        if char_type == 0:
            name += random.choice(lowercase_chars)
        else:
            name += random.choice(digits)

    return name


def convert_gif_to_mp4(name):
    # Путь к исходному файлу .gifv
    input_path = "video.gifv"

    # Путь к выходному файлу .mp4
    output_path = name + ".mp4"

    # Загрузка видео
    clip = VideoFileClip(input_path)

    # Сохранение видео в формате .mp4
    clip.write_videofile(output_path, codec="libx264")

    print(f"Конвертация завершена. Видео сохранено как {name}.mp4")



url = "https://media.tumblr.com/___/____.gifv"
download_gif(url)
name = generate_file_name()
convert_gif_to_mp4(name)