import moviepy.editor as mp
import os

def convert_mp4_to_gif(mp4_path, output_path, max_size_kb, resolution_percent):
    # Загрузка видео
    clip = mp.VideoFileClip(mp4_path)

    # Получение исходного разрешения видео
    original_width, original_height = clip.size

    # Вычисление нового разрешения на основе процента уменьшения
    new_width = int(original_width * (resolution_percent / 100))
    new_height = int(original_height * (resolution_percent / 100))

    # Изменение разрешения видео
    clip = clip.resize((new_width, new_height))

    # Определение начального качества GIF
    quality = 100

    # Флаг для отслеживания текущей итерации (True - изменение качества, False - изменение размера)
    quality_iteration = True

    while True:
        # Создание анимированного GIF с текущим качеством
        clip.write_gif(output_path, fps=15, program='ffmpeg', opt=f'optimizeplus -q {quality}')

        # Проверка размера полученного GIF
        gif_size = os.path.getsize(output_path) / 1024  # Размер в КБ

        if gif_size <= max_size_kb:
            break
        else:
            if quality_iteration:
                # Уменьшение качества GIF на текущей итерации
                quality -= 5
                quality_iteration = False
            else:
                # Уменьшение разрешения GIF на текущей итерации
                resolution_percent -= 10
                new_width = int(original_width * (resolution_percent / 100))
                new_height = int(original_height * (resolution_percent / 100))
                clip = clip.resize((new_width, new_height))
                quality_iteration = True

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

# Процент разрешения (например, 50% от исходного разрешения)
resolution_percent = 50

# Обработка всех файлов с расширением .mp4 в папке video
for filename in os.listdir(video_folder):
    if filename.endswith(".mp4"):
        mp4_path = os.path.join(video_folder, filename)
        gif_filename = os.path.splitext(filename)[0] + ".gif"
        output_path = os.path.join(gif_folder, gif_filename)

        convert_mp4_to_gif(mp4_path, output_path, max_size_kb, resolution_percent)
