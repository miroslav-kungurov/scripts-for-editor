import os
from PIL import Image

input_folder = "img to compress"
output_folder = "img to compress/compressed/png"
compression_level = 5  # от 0 до 9, чем меньше - тем сильнее сжатие

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

for filename in os.listdir(input_folder):
    if filename.lower().endswith(".png"):
        image_path = os.path.join(input_folder, filename)
        image = Image.open(image_path)

        name_without_extension = os.path.splitext(filename)[0]
        new_filename = f"{name_without_extension}_compressed.png"

        output_path = os.path.join(output_folder, new_filename)

        image.save(output_path, optimize=True, quality=compression_level)

        print(f"Изображение {filename} сжато и сохранено как {new_filename}")
