import os
from PIL import Image

def resize_images(folder_path, output_folder, height=None, width=None):
    # Создаем папку "resizedXY", если она не существует
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Проходимся по всем файлам в папке "resize"
    for filename in os.listdir(folder_path):
        if filename.endswith(".jpg") or filename.endswith(".jpeg") or filename.endswith(".png"):
            # Открываем изображение
            image_path = os.path.join(folder_path, filename)
            image = Image.open(image_path)

            # Получаем текущие размеры изображения
            current_width, current_height = image.size

            if height is not None:
                # Вычисляем новую ширину на основе заданной высоты
                ratio = height / current_height
                new_width = int(current_width * ratio)
                new_height = height
            elif width is not None:
                # Вычисляем новую высоту на основе заданной ширины
                ratio = width / current_width
                new_width = width
                new_height = int(current_height * ratio)
            else:
                print("Необходимо указать либо высоту, либо ширину.")
                return

            # Изменяем размер изображения
            resized_image = image.resize((new_width, new_height))

            # Формируем путь для сохранения измененного изображения
            output_path = os.path.join(output_folder, filename)

            # Сохраняем измененное изображение
            resized_image.save(output_path)

            print(f"Изображение {filename} изменено и сохранено как {output_path}")

# Путь к папке с исходными изображениями
folder_path = "img to resize/"

# Путь к папке для сохранения измененных изображений
output_folder = "img to resize/resizedXY"

# Запрашиваем у пользователя высоту или ширину
choice = input("Введите 'h' для изменения высоты или 'w' для изменения ширины: ")

if choice.lower() == 'h':
    height = int(input("Введите желаемую высоту: "))
    resize_images(folder_path, output_folder, height=height)
elif choice.lower() == 'w':
    width = int(input("Введите желаемую ширину: "))
    resize_images(folder_path, output_folder, width=width)
else:
    print("Некорректный выбор. Пожалуйста, введите 'h' или 'w'.")
