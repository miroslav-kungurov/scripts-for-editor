import os
import ffmpeg

def change_video_speed(input_video, output_dir, speed_factor):
    """
    speed_factor (float): Коэффициент скорости воспроизведения.
        Значение > 1.0 ускоряет видео и аудио, значение < 1.0 замедляет видео и аудио.
    """

    # Создание папки "change video speed", если она не существует
    if not os.path.exists("change video speed"):
        os.makedirs("change video speed")

    # Получаем имя файла и расширение
    filename, ext = os.path.splitext(os.path.basename(input_video))

    # Формируем имя для выходного видеофайла
    output_filename = f"{filename}_{speed_factor:.1f}{ext}"
    output_video = os.path.join(output_dir, output_filename)

    # Создаем входной поток
    input_stream = ffmpeg.input(input_video)

    # Разделяем видео- и аудиопотоки
    video_stream = input_stream.video
    audio_stream = input_stream.audio

    # Применяем коэффициент скорости к видео
    video_stream = ffmpeg.filter(video_stream, 'setpts', f'PTS/{speed_factor}')

    # Применяем коэффициент скорости к аудио
    audio_stream = ffmpeg.filter(audio_stream, 'atempo', speed_factor)

    # Объединяем видео- и аудиопотоки
    output_stream = ffmpeg.output(video_stream, audio_stream, output_video)

    # Сохраняем обработанное видео
    ffmpeg.run(output_stream, overwrite_output=True)

    print(f"Обработанный видеофайл сохранен как: {output_video}")

# Пример использования
input_video = "downloads/video.mp4"
output_dir = "change video speed"
speed_factor = 0.5  # Ускорить видео и аудио в 1.5 раза

change_video_speed(input_video, output_dir, speed_factor)