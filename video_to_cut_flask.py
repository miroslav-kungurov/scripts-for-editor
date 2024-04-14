from flask import Flask, render_template, request, redirect, url_for
from moviepy.editor import VideoFileClip
import os

app = Flask(__name__)

# Путь к папке с исходными видео
input_folder = "video to cut"

# Путь к папке для сохранения вырезанных кусков видео
output_folder = os.path.join(input_folder, "cut")

# Создаем папку для сохранения вырезанных кусков, если она не существует
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Получаем начало и конец кусков из формы
        start_times = [int(request.form[f'start_minute_{i}']) * 60 + int(request.form[f'start_second_{i}']) for i in range(len(request.form) // 4)]
        end_times = [int(request.form[f'end_minute_{i}']) * 60 + int(request.form[f'end_second_{i}']) for i in range(len(request.form) // 4)]

        # Получаем выбранные видео файлы
        selected_videos = request.form.getlist('video_file')

        # Количество вырезанных кусков
        cut_count = 0

        # Обрабатываем каждый выбранный видео файл
        for video_filename in selected_videos:
            # Полный путь к исходному видео файлу
            input_path = os.path.join(input_folder, video_filename)

            # Загружаем видео
            video = VideoFileClip(input_path)

            # Обрабатываем каждый кусок
            for i, (start_time, end_time) in enumerate(zip(start_times, end_times)):
                # Вырезаем кусок из видео
                cut_video = video.subclip(start_time, end_time)

                # Генерируем имя для вырезанного куска видео с временными метками
                cut_filename = f"{video_filename.split('.')[0]}_m{start_time//60}_s{start_time%60}_m{end_time//60}_s{end_time%60}.mp4"

                # Полный путь для сохранения вырезанного куска видео
                output_path = os.path.join(output_folder, cut_filename)

                # Сохраняем вырезанный кусок видео
                cut_video.write_videofile(output_path)

                print(f"Вырезанный кусок видео сохранен в {output_path}")
                cut_count += 1

        # Получаем список видео файлов в папке
        video_files = [f for f in os.listdir(input_folder) if f.endswith(".mp4")]

        return render_template('video_cut.html', video_files=video_files, cut_count=cut_count)

    # Получаем список видео файлов в папке
    video_files = [f for f in os.listdir(input_folder) if f.endswith(".mp4")]

    return render_template('video_cut.html', video_files=video_files, cut_count=0)

if __name__ == '__main__':
    app.run(debug=True)