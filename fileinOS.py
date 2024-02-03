import time

import os


path = 'C:\\Users\\m9139\\OneDrive\\Изображения'

for dirpath, dirnames, filenames in os.walk(path):
    print('*' * 10)
    print(dirpath, dirnames, filenames)
    print(os.path.dirname(dirpath))
    for file in filenames:
        full_file_path = os.path.join(dirpath, file)
        full_name_path = dirpath + '\\' + file
        secs = os.path.getmtime(full_name_path)
        file_time = time.gmtime(secs)
        size = [(os.stat(os.path.join(path)).st_size)
                for f in filenames]
        print(full_name_path, secs)

        print(f'Обнаружен файл: {file}, Путь: {full_file_path}, размер: {size}, время изменения: {file_time}, Родительская директория: {dirpath}')