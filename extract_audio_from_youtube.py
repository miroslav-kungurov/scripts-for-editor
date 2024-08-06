import yt_dlp
from pydub import AudioSegment
import os
import re

def youtube_to_wav(video_url, audio_folder='audio'):
    def create_folder():
        if not os.path.exists(audio_folder):
            os.makedirs(audio_folder)
            print(f"Папка '{audio_folder}' успешно создана.")
        else:
            print(f"Папка '{audio_folder}' уже существует.")

    def download_audio_from_youtube():
        ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
            }],
            'outtmpl': os.path.join(audio_folder, '%(title)s.%(ext)s'),
        }

        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(video_url, download=True)
                video_title = info['title']
                audio_file = os.path.join(audio_folder, f"{video_title}.mp3")
                print(f"Скачанный файл: {audio_file}")
                return audio_file, video_title
        except Exception as e:
            print(f"Ошибка при скачивании аудио: {str(e)}")
            return None, None

    def clean_string(string):
        cleaned_string = re.sub(r'[^a-zA-Z0-9\s]', '', string)
        cleaned_string = re.sub(r'\s', '_', cleaned_string)
        return cleaned_string

    def convert_mp3_to_wav(audio_file_mp3, video_title):
        try:
            print(f"Попытка конвертации файла: {audio_file_mp3}")
            if not os.path.exists(audio_file_mp3):
                print(f"Файл не найден: {audio_file_mp3}")
                return None, None

            audio = AudioSegment.from_mp3(audio_file_mp3)
            audio = audio.set_frame_rate(16000).set_channels(1)

            audio_file_wav = clean_string(video_title) + ".wav"
            audio_path = os.path.join(audio_folder, audio_file_wav)

            audio.export(audio_path, format="wav")
            print(f"Аудио успешно конвертировано в WAV: {audio_path}")
            os.remove(audio_file_mp3)
            print(f"Исходный MP3 файл удален: {audio_file_mp3}")
            
            txt_file_name = clean_string(video_title)

            return txt_file_name, audio_path
        except Exception as e:
            print(f"Ошибка при конвертации аудио: {str(e)}")
            return None, None

    # Основной процесс
    create_folder()
    audio_file_mp3, video_title = download_audio_from_youtube()
    
    if audio_file_mp3 is None:
        print("Не удалось скачать аудио. Конвертация невозможна.")
        return None, None

    txt_file_name, audio_path = convert_mp3_to_wav(audio_file_mp3, video_title)
    
    if txt_file_name and audio_path:
        print(f"Аудио успешно скачано и конвертировано: {audio_path}")
        print(f"Имя файла для текста: {txt_file_name}")
        return txt_file_name, audio_path
    else:
        print("Не удалось обработать видео.")
        return None, None

if __name__ == "__main__":
    yt_video_url = 'https://www.youtube.com/watch?v=LKCVKw9CzFo&t'
    result = youtube_to_wav(yt_video_url)
    if result:
        txt_file_name, audio_path = result
        print(f"Итоговый результат:")
        print(f"Имя файла для текста: {txt_file_name}")
        print(f"Путь к аудио файлу: {audio_path}")
    else:
        print("Обработка видео завершилась неудачно.")
