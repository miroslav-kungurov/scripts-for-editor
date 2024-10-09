# -*- coding: utf-8 -*-
import cv2
import os
from datetime import datetime


def extract_frames(video_path):
    # Получаем имя видеофайла без расширения
    video_name = os.path.splitext(os.path.basename(video_path))[0]

    # Получаем текущую дату и время
    now = datetime.now()
    folder_name = f"{video_name}_{now.minute:02d}_{now.hour:02d}_{now.day:02d}_{now.month:02d}_{now.year}"

    # Создаем папку для сохранения кадров
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

    # Открываем видеофайл
    video = cv2.VideoCapture(video_path)

    # Проверяем, успешно ли открыт файл
    if not video.isOpened():
        print("Ошибка при открытии видеофайла")
        return

    # Счетчик кадров
    frame_count = 0

    while True:
        # Читаем кадр
        success, frame = video.read()

        # Если кадры закончились, выходим из цикла
        if not success:
            break

        # Сохраняем кадр
        frame_name = os.path.join(folder_name, f"frame_{frame_count:04d}.png")
        cv2.imwrite(frame_name, frame)

        frame_count += 1

    # Закрываем видеофайл
    video.release()

    print(f"Извлечено {frame_count} кадров. Сохранены в папку: {folder_name}")


# Пример использования
video_path = r""
extract_frames(video_path)
