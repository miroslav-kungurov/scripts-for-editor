# -*- coding: utf-8 -*-
import os
import re
import yt_dlp


def clean_filename(filename):
    # Удаляем знаки препинания и оставляем только буквы, числа и пробелы
    cleaned = re.sub(r'[^a-zA-Zа-яА-Я0-9\s]', '', filename)
    # Заменяем пробелы на подчеркивания
    return cleaned.replace(' ', '_')


def download_video(url, download_path):
    try:
        ydl_opts = {
            'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
            'outtmpl': os.path.join(download_path, '%(title)s.%(ext)s'),
            'restrictfilenames': True,
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            if 'title' in info:
                title = clean_filename(info['title'])
            else:
                title = 'video_' + info['id']

            filename = f"{title}.mp4"
            ydl_opts['outtmpl'] = os.path.join(download_path, filename)

            print(f"Скачивание видео: {title}")
            ydl.download([url])
            print("Видео успешно скачано!")

    except Exception as e:
        print(f"Ошибка при скачивании видео: {str(e)}")
        print("Попытка скачать видео с альтернативными настройками...")
        try:
            ydl_opts = {
                'format': 'best',
                'outtmpl': os.path.join(download_path, '%(title)s.%(ext)s'),
            }
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
            print("Видео успешно скачано с альтернативными настройками!")
        except Exception as e:
            print(f"Не удалось скачать видео: {str(e)}")


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
