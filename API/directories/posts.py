import os
from config import MEDIA_ROOT

async def create_dir(filename):
    file_dir_for_django = f"/post/main_images/"
    file_directory = f"{MEDIA_ROOT}{file_dir_for_django}"
    try:
        os.makedirs(file_directory)
        file_full_path = file_directory + filename
    except FileExistsError:
        file_full_path = file_directory + filename
    return {
        'file_dir': file_dir_for_django,
        'file_full_path': file_full_path}


async def create_post_images_dir(filename):
    file_dir_for_django = f"post/post_images/"
    file_directory = f"{MEDIA_ROOT}{file_dir_for_django}"
    try:
        os.makedirs(file_directory)
        file_full_path = file_directory + filename
    except FileExistsError:
        file_full_path = file_directory + filename
    return {
        'file_dir': file_dir_for_django,
        'file_full_path': file_full_path}
