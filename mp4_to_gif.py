import moviepy.editor as mp
import os

def convert_mp4_to_gif(mp4_path, output_path, max_size_kb, resolution_percent):
    # Загрузка видео
    clip = mp.VideoFileClip(mp4_path)

    # Получение исходного разрешения видео
    original_width, original_height = clip.size

    # Вычисление нового разрешения на основе процента уменьшения
    new_width = int(original_width * (1 - resolution_percent / 100))
    new_height = int(original_height * (1 - resolution_percent / 100))

    # Изменение разрешения видео
    clip = clip.resize((new_width, new_height))

    # Определение начального размера GIF
    size = 1.0

    while True:
        # Создание анимированного GIF с текущим размером
        clip.resize(size).write_gif(output_path, fps=15, program='ffmpeg')

        # Проверка размера полученного GIF
        gif_size = os.path.getsize(output_path) / 1024  # Размер в КБ

        if gif_size <= max_size_kb:
            break
        else:
            # Уменьшение размера GIF, если он превышает ограничение
            size -= 0.05

    print(f"Конвертация завершена. Размер GIF: {gif_size:.2f} КБ")

# Папка с исходными видео файлами
video_folder = "video"

# Папка для сохранения GIF файлов
gif_folder = "gif"

# Создание папки для GIF, если она не существует
if not os.path.exists(gif_folder):
    os.makedirs(gif_folder)

# Максимальный размер GIF в килобайтах
max_size_kb = 2500

# Процент уменьшения разрешения (например, 15%)
resolution_percent = 5

# Обработка всех файлов с расширением .mp4 в папке video
for filename in os.listdir(video_folder):
    if filename.endswith(".mp4"):
        mp4_path = os.path.join(video_folder, filename)
        gif_filename = os.path.splitext(filename)[0] + ".gif"
        output_path = os.path.join(gif_folder, gif_filename)

        convert_mp4_to_gif(mp4_path, output_path, max_size_kb, resolution_percent)
