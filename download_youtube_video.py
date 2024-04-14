import re
from pytube import YouTube

def download_video(url):
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

        # Скачиваем видео
        print(f"Скачивание видео: {title}")
        stream.download(filename=f"{title}.mp4")
        print("Видео успешно скачано!")

    except Exception as e:
        print(f"Ошибка при скачивании видео: {str(e)}")

# Список URL видео на YouTube
video_urls = [
    "https://www.youtube.com/watch?v=wjZofJX0v4M",
    "https://www.youtube.com/watch?v=wjZofJX0v4M",
    "https://www.youtube.com/watch?v=wjZofJX0v4M"
]

# Скачиваем каждое видео из списка
for url in video_urls:
    download_video(url)
