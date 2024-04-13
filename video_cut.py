import os
from moviepy.editor import VideoFileClip

# Путь к папке с исходными видео
input_folder = "video to cut"

# Путь к папке для сохранения вырезанных кусков видео
output_folder = os.path.join(input_folder, "cut")

# Создаем папку для сохранения вырезанных кусков, если она не существует
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Запрашиваем у пользователя начало и конец куска в минутах и секундах
start_minute = int(input("Введите начальную минуту куска: "))
start_second = int(input("Введите начальную секунду куска: "))
end_minute = int(input("Введите конечную минуту куска: "))
end_second = int(input("Введите конечную секунду куска: "))

# Вычисляем начало и конец куска в секундах
start_time = start_minute * 60 + start_second
end_time = end_minute * 60 + end_second

# Получаем список файлов в папке с исходными видео
video_files = [f for f in os.listdir(input_folder) if f.endswith(".mp4")]

# Обрабатываем каждый видео файл
for filename in video_files:
    # Полный путь к исходному видео файлу
    input_path = os.path.join(input_folder, filename)

    # Загружаем видео
    video = VideoFileClip(input_path)

    # Вырезаем кусок из видео
    cut_video = video.subclip(start_time, end_time)

    # Получаем имя файла без расширения
    base_filename = os.path.splitext(filename)[0]

    # Генерируем имя для вырезанного куска видео с временными метками
    cut_filename = f"{base_filename}_m{start_minute}_s{start_second}_m{end_minute}_s{end_second}.mp4"

    # Полный путь для сохранения вырезанного куска видео
    output_path = os.path.join(output_folder, cut_filename)

    # Сохраняем вырезанный кусок видео
    cut_video.write_videofile(output_path)

    print(f"Вырезанный кусок видео сохранен в {output_path}")
