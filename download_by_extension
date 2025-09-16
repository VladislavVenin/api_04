import os
import urllib.parse
import requests


def get_extension(url):
    extension = os.path.splitext(
        os.path.split(urllib.parse.urlsplit(url).path)[-1])[-1]
    return extension


def download_image(path, filename, image_link):
    if not os.path.exists(path):
        os.mkdir(path)

    response = requests.get(image_link)
    response.raise_for_status()

    with open(f'{path}/{filename}', 'wb') as file:
        file.write(response.content)
