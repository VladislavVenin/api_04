import requests
import decouple
from dl_by_ext import download_image, get_extension


def fetch_spacex_last_launch(path, id='latest'):
    url = f"https://api.spacexdata.com/v5/launches/{id}"
    response = requests.get(url)
    api_response = response.json()
    images = api_response['links']['flickr']['original']
    for index, image in enumerate(images):
        download_image(path, f'spacex_{index}{get_extension(image)}', image)


def fetch_APOD(path, payload):
    url = 'https://api.nasa.gov/planetary/apod'
    response = requests.get(url, params=payload)
    api_response = response.json()
    for index, image_url in enumerate(api_response):
        download_image(
            path, f"APOD_{index}{get_extension(image_url['url'])}", image_url['url']
            )


def fetch_EPIC(path, payload):
    response = requests.get(
        'https://epic.gsfc.nasa.gov/api/natural', params=payload
        )
    api_resonse = response.json()
    for index, image in enumerate(api_resonse):
        image_id = image['image']
        date = image['date']
        date = date.split(' ')
        date = date[0].replace('-', '/')
        image_response = requests.get(
            f"https://epic.gsfc.nasa.gov/archive/natural/{date}/png/{image_id}.png"
        )
        download_image(path, f'EPIC_{index}.png', image_response.url)


path = 'images'
payload = {
    'api_key': decouple.config('NASA_API_TOKEN'),
    'count': 30,
}
