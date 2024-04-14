import os
from PIL import Image

def resize_images(folder_path, percentage):
    # Создаем папку "resized", если она не существует
    resized_folder = os.path.join(folder_path, "resized percent")
    if not os.path.exists(resized_folder):
        os.makedirs(resized_folder)

    # Проходимся по всем файлам в папке
    for filename in os.listdir(folder_path):
        if filename.endswith(".jpg") or filename.endswith(".jpeg") or filename.endswith(".png"):
            # Открываем изображение
            image_path = os.path.join(folder_path, filename)
            image = Image.open(image_path)

            # Получаем текущие размеры изображения
            width, height = image.size

            # Вычисляем новые размеры изображения
            new_width = int(width * percentage / 100)
            new_height = int(height * percentage / 100)

            # Изменяем размер изображения
            resized_image = image.resize((new_width, new_height))

            # Формируем новое имя файла с добавлением процента уменьшения
            name, extension = os.path.splitext(filename)
            new_filename = f"{name}_{percentage}per{extension}"

            # Сохраняем измененное изображение в папку "resized"
            resized_image_path = os.path.join(resized_folder, new_filename)
            resized_image.save(resized_image_path)

            print(f"Изображение {filename} уменьшено на {percentage}% и сохранено как {new_filename}")

# Путь к папке с изображениями
folder_path = "img to resize"

# Запрашиваем у пользователя процент уменьшения
percentage = int(input("Введите процент уменьшения изображений: "))

# Вызываем функцию для изменения размера изображений
resize_images(folder_path, percentage)
