import ffmpeg

def convert_mp4_to_avi(mp4_path, avi_path):
    # Конвертация MP4 в AVI с помощью FFmpeg
    stream = ffmpeg.input(mp4_path)
    stream = ffmpeg.output(stream, avi_path, vcodec='mpeg4', acodec='mp3')
    ffmpeg.run(stream)

# Пример использования
mp4_file = 'video.mp4'
avi_file = 'video.avi'

convert_mp4_to_avi(mp4_file, avi_file)

