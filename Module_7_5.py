import os
from datetime import datetime

directory = "."
# рабочая директория
current_dir = os.getcwd()

# список файлов из рабочей директории
files_in_dir = os.listdir(current_dir)

# печать полного пути к файлам из рабочей директории
for file_name in files_in_dir:
    if os.path.isfile(file_name):
        file_path = os.path.join(current_dir, file_name)
        mtime = os.path.getctime(file_name)
        mtime_readable = datetime.fromtimestamp(mtime)
        file_size = os.path.getsize(file_name)
        parent_dir = os.path.dirname(current_dir)
        print(f'Найден файл: {file_name}, Путь: {file_path}, Размер: {file_size} байт, Время создания { mtime_readable}'
              f'Родительская директория: {parent_dir}')
# обход всех директорий
# for files in os.walk(directory):
#     print(files)




