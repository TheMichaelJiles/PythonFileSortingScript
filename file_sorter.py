import os
import shutil

'''PATH TO DIRECTORY TO BE SORTED BELOW'''
directory = 'A:\TestFolder\\'

def path_is_directory(path):
    return os.path.isdir(path)

def get_file_extension(filename):
    extension = ""
    for char in reversed(filename):
        if not char == ".":
            extension = char + extension
        else:
            break
    return extension

for filename in os.listdir(directory):
    current_path = directory + filename

    if(not path_is_directory(current_path)):
        new_directory = get_file_extension(filename).upper()
        new_directory_path = directory + new_directory

        if not os.path.exists(new_directory_path):
            os.mkdir(new_directory_path)
        
        shutil.move(current_path, new_directory_path)
