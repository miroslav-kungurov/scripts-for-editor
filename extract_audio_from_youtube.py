from pytube import YouTube
from pydub import AudioSegment
import os
import re

# Указываем путь к папке "audio"
audio_folder = "audio"

def create_folder():
    # Проверяем, существует ли папка "audio"
    if not os.path.exists(audio_folder):
        # Если папка не существует, создаем ее
        os.makedirs(audio_folder)
        print(f"Папка '{audio_folder}' успешно создана.")
    else:
        print(f"Папка '{audio_folder}' уже существует.")


def download_video_from_yotube(video_url, audio_folder='audio'):
    # Скачиваем аудио из видео на YouTube
    yt = YouTube(video_url)
    audio_stream = yt.streams.filter(only_audio=True).first()
    video_title = yt.title

    # чистим имя файла
    audio_file_mp4 = clean_string(video_title)

    audio_file_mp4 += ".mp4"

    # Формируем путь для экспорта аудио в папку "audio"
    audio_path = os.path.join(audio_folder, audio_file_mp4)

    audio_stream.download(filename=audio_file_mp4)
    return audio_file_mp4, video_title


def convert_mp4_to_wav(video_url, audio_folder='audio'):
    # Указываем путь к папке "audio"
    audio_folder = "audio"
    # Конвертируем аудио в формат WAV
    audio_file_mp4, video_title = download_video_from_yotube(video_url)
    audio = AudioSegment.from_file(audio_file_mp4, format="mp4")
    audio = audio.set_frame_rate(16000).set_channels(1)

    # чистим имя файла
    audio_file_wav = clean_string(video_title)

    # имя текстового файла
    txt_file_name = clean_string(video_title)

    audio_file_wav += ".wav"

    # Формируем путь для экспорта аудио в папку "audio"
    audio_path = os.path.join(audio_folder, audio_file_wav)

    audio.export(audio_path, format="wav")
    os.remove(audio_file_mp4)
    return txt_file_name, audio_path


def clean_string(string):
    # Удаляем все символы, кроме букв, цифр и пробелов
    cleaned_string = re.sub(r'[^a-zA-Z0-9\s]', '', string)
    # Заменяем пробелы на нижнее подчеркивание
    cleaned_string = re.sub(r'\s', '_', cleaned_string)
    return cleaned_string

if __name__ == "__main__":
    yt_video_url = 'https://youtu.be/wjZofJX0v4M?si=cigxsRgfz9o8iYij'
    create_folder()
    convert_mp4_to_wav(video_url=yt_video_url)

