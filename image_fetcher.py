import requests
import decouple
import argparse
import datetime
from utils import download_image, get_extension


def fetch_spacex(path, id):
    url = f"https://api.spacexdata.com/v5/launches/{id}"

    response = requests.get(url)
    response.raise_for_status()

    api_response = response.json()
    images = api_response['links']['flickr']['original']
    for index, image in enumerate(images):
        download_image(path, f'spacex_{index}{get_extension(image)}', image)


def fetch_apod(path, payload):
    url = 'https://api.nasa.gov/planetary/apod'

    response = requests.get(url, params=payload)
    response.raise_for_status()

    api_response = response.json()
    for index, image_url in enumerate(api_response):
        image_url = image_url['url']
        download_image(path, f"APOD_{index}{get_extension(image_url)}", image_url)


def fetch_epic(path, payload):
    response = requests.get(
        'https://epic.gsfc.nasa.gov/api/natural', params=payload
        )
    response.raise_for_status()

    api_resonse = response.json()
    for index, image in enumerate(api_resonse):
        image_id = image['image']
        date = image['date']
        date = datetime.datetime.fromisoformat(date)
        date = date.strftime('%Y/%m/%d')
        image_response = requests.get(f"https://epic.gsfc.nasa.gov/archive/natural/{date}/png/{image_id}.png")
        download_image(path, f'EPIC_{index}.png', image_response.url)


def main():
    parser = argparse.ArgumentParser(
        description="Утилита для скачивания фотографий от SpaceX и NASA"
    )
    parser.add_argument('option', type=str,
                        choices=['spacex', 'apod', 'epic'],
                        help='Выберите, откуда будут браться файлы')
    parser.add_argument('--path', type=str, default='images',
                        help="Путь по которому нужно сохранить файлы, по стандарту images")
    parser.add_argument('--count', type=int, default=1,
                        help='Кол-во файлов которое требуется сохранить(только APOD)')
    parser.add_argument('--id', type=str, default='latest',
                        help='Идентификатор запуска SpaceX, по стандарту сохраняет фотографии с последнего запуска.')
    args = parser.parse_args()

    payload = {
        'api_key': decouple.config('NASA_API_TOKEN'),
        'count': args.count,
    }
    option = args.option.lower()

    match option:
        case 'spacex':
            fetch_spacex(args.path, args.id)
        case 'apod':
            fetch_apod(args.path, payload)
        case 'epic':
            fetch_epic(args.path, payload)


if __name__ == '__main__':
    main()
