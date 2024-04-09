import re
from pytube import YouTube

def download_video(url):
    try:
        # Создаем объект YouTube
        video = YouTube(url)

        # Получаем название видео
        title = video.title

        # Удаляем знаки препинания и оставляем только буквы и числа
        title = re.sub(r'[^a-zA-Z0-9 ]', '', title)

        # Заменяем пробелы на подчеркивания
        title = title.replace(' ', '_')

        # Получаем поток с наилучшим качеством
        stream = video.streams.get_highest_resolution()

        # Скачиваем видео
        print(f"Скачивание видео: {title}")
        stream.download(filename=f"{title}.mp4")
        print("Видео успешно скачано!")

    except Exception as e:
        print(f"Ошибка при скачивании видео: {str(e)}")

# URL видео на YouTube
video_url = "https://youtu.be/wjZofJX0v4M?si=cigxsRgfz9o8iYij"

# Скачиваем видео
download_video(video_url)
