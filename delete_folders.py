import os
import shutil

def delete_selected_folders(folders):
    """
    Удаляет выбранные папки со всем их содержимым.

    :param folders: Список путей к папкам для удаления.
    """
    for folder in folders:
        if os.path.exists(folder):
            shutil.rmtree(folder)
            print(f"Папка {folder} и все её содержимое были удалены.")
        else:
            print(f"Папка {folder} не существует.")


if __name__ == "__main__":
    # Список папок для удаления
    folders_to_delete = [
        "path/to/folder1",
        "path/to/folder2",
        "path/to/folder3"
    ]
    
    delete_selected_folders(folders_to_delete)
