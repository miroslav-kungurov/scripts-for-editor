import os
from PIL import Image

# Папка с исходными изображениями
input_folder = "img to compress"

# Папка для сохранения сжатых изображений
output_folder = "img to compress/compressed"

# Процент сжатия (например, 97%)
compression_percent = 50

# Создаем папку для сохранения сжатых изображений, если она не существует
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Проходимся по всем файлам в папке с исходными изображениями
for filename in os.listdir(input_folder):
    if filename.lower().endswith(".jpeg") or filename.lower().endswith(".jpg"):
        # Открываем изображение
        image_path = os.path.join(input_folder, filename)
        image = Image.open(image_path)

        # Получаем имя файла без расширения
        name_without_extension = os.path.splitext(filename)[0]

        # Формируем новое имя файла с указанием процента сжатия
        new_filename = f"{name_without_extension}_{100 - compression_percent}per.jpg"

        # Формируем путь для сохранения сжатого изображения
        output_path = os.path.join(output_folder, new_filename)

        # Сохраняем изображение с указанным качеством/размером
        image.save(output_path, "JPEG", quality=compression_percent)

        print(f"Изображение {filename} сжато и сохранено как {new_filename}")
