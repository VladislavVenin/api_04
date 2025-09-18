import os
import urllib.parse
import requests


def get_extension(url):
    path = urllib.parse.urlsplit(url).path
    file = os.path.split(path)[-1]
    extension = os.path.splitext(file)[-1]
    return extension


def download_image(path, filename, image_link):
    os.makedirs(path, exist_ok=True)

    response = requests.get(image_link)
    response.raise_for_status()

    with open(f'{path}/{filename}', 'wb') as file:
        file.write(response.content)

