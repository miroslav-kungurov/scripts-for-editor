# -*- coding: utf-8 -*-
import os
from moviepy.editor import VideoFileClip, vfx


def change_video_speed(input_video, output_dir, speed_factor):
    """
    speed_factor (float): Коэффициент скорости воспроизведения.
        Значение > 1.0 ускоряет видео, значение < 1.0 замедляет видео.
    """

    # Создание папки "change video speed", если она не существует
    if not os.path.exists("change video speed"):
        os.makedirs("change video speed")


    # Получаем имя файла и расширение
    filename, ext = os.path.splitext(os.path.basename(input_video))

    # Формируем имя для выходного видеофайла
    output_filename = f"{filename}_{speed_factor:.1f}{ext}"
    output_video = os.path.join(output_dir, output_filename)

    # Загружаем видео
    clip = VideoFileClip(input_video)

    # Применяем коэффициент скорости
    processed_clip = clip.fx(vfx.speedx, speed_factor)

    # Сохраняем обработанное видео
    processed_clip.write_videofile(output_video)

    # Закрываем клипы
    clip.close()
    processed_clip.close()

    print(f"Обработанный видеофайл сохранен как: {output_video}")


# Пример использования
input_video = "downloads/video.mp4"
output_dir = "change video speed"
speed_factor = 0.5  # Ускорить видео в 1.5 раза

change_video_speed(input_video, output_dir, speed_factor)