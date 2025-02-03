import os
import subprocess

input_folder = r"D:\folder"
output_folder = os.path.join(input_folder, "cut")
os.makedirs(output_folder, exist_ok=True)

# Ввод временных параметров
start_minute = int(input("Введите начальную минуту куска: "))
start_second = int(input("Введите начальную секунду куска: "))
end_minute = int(input("Введите конечную минуту куска: "))
end_second = int(input("Введите конечную секунду куска: "))

# Конвертация времени
start_total = start_minute * 60 + start_second
end_total = end_minute * 60 + end_second


def to_time_str(total_seconds):
    hours = total_seconds // 3600
    minutes = (total_seconds % 3600) // 60
    seconds = total_seconds % 60
    return f"{hours:02}:{minutes:02}:{seconds:02}"


start_time = to_time_str(start_total)
end_time = to_time_str(end_total)

video_files = [f for f in os.listdir(input_folder) if f.lower().endswith(".mp4")]

for filename in video_files:
    input_path = os.path.join(input_folder, filename)
    base_name = os.path.splitext(filename)[0]

    output_filename = (
        f"{base_name}_m{start_minute}_s{start_second}_"
        f"m{end_minute}_s{end_second}.mp4"
    )
    output_path = os.path.join(output_folder, output_filename)

    # Команда с GPU-ускорением (NVIDIA NVENC)
    cmd = [
        'ffmpeg',
        '-y',
        '-hwaccel', 'cuda',  # Аппаратное ускорение декодирования
        '-i', input_path,
        '-ss', start_time,
        '-to', end_time,
        '-c:v', 'h264_nvenc',  # NVIDIA GPU-кодек
        '-preset', 'p6',  # Оптимизированный пресет для NVENC
        '-tune', 'hq',  # Настройка на качество
        '-cq', '23',  # Constant Quality (0-51, меньше - лучше)
        '-rc', 'vbr',  # Переменный битрейт
        '-c:a', 'aac',  # Аудиокодек
        '-b:a', '128k',  # Битрейт аудио
        output_path
    ]

    try:
        subprocess.run(cmd, check=True, stderr=subprocess.PIPE, text=True)
        print(f"Успешно: {output_path}")
    except subprocess.CalledProcessError as e:
        print(f"Ошибка в {filename}: {e.stderr}")
    except Exception as e:
        print(f"Общая ошибка: {str(e)}")
