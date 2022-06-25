__winc_id__ = "ae539110d03e49ea8738fd413ac44ba8"
__human_name__ = "files"

import os
import shutil
import zipfile
current_dir = os.getcwd() + "\\files"

def clean_cache():
    new_dir = os.path.join(current_dir, "cache")
    if not os.path.exists(new_dir):
        os.mkdir(new_dir)
    else:
        shutil.rmtree(new_dir, ignore_errors=True)
        os.mkdir(new_dir)
    return new_dir

def cache_zip(zip_file_path, cache_dir_path):
    with zipfile.ZipFile(zip_file_path, "r") as zip_obj:
        zip_obj.extractall(cache_dir_path)
        return zip_obj

def cached_files():
    list_of_cached_files = []
    abs_path = os.path.abspath(current_dir + ".\cache")
    i = os.scandir(abs_path)
    for entry in i:
        list_of_cached_files.append(entry.path)
    return list_of_cached_files

def find_password(file_list):
    for file in file_list:
        with open(file, "r") as f:
            file_contents = f.readlines()
            for line in file_contents:
                if "password" in line:
                    return (line.strip()[10:])

if __name__ == "__main__":
    print(current_dir)
    print(find_password(cached_files()))
