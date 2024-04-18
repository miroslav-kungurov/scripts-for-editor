# -*- coding: utf-8 -*-
import os
import re
from pytube import YouTube

def download_video(url, download_path):
    try:
        # Создаем объект YouTube
        video = YouTube(url)

        # Получаем название видео
        title = video.title

        # Удаляем знаки препинания и оставляем только буквы и числа
        title = re.sub(r'[^a-zA-Zа-яА-Я0-9\s]', '', title)

        # Заменяем пробелы на подчеркивания
        title = title.replace(' ', '_')

        # Получаем поток с наилучшим качеством
        stream = video.streams.get_highest_resolution()

        # Скачиваем видео в указанную папку
        print(f"Скачивание видео: {title}")
        stream.download(output_path=download_path, filename=f"{title}.mp4")
        print("Видео успешно скачано!")

    except Exception as e:
        print(f"Ошибка при скачивании видео: {str(e)}")

# Список URL видео на YouTube
video_urls = [
    "https://www.youtube.com/watch?v=wjZofJX0v4M",
]

# Путь к папке "downloads"
download_folder = "downloads"

# Создаем папку "downloads", если она не существует
if not os.path.exists(download_folder):
    os.makedirs(download_folder)

# Скачиваем каждое видео из списка и сохраняем в папку "downloads"
for url in video_urls:
    download_video(url, download_folder)
