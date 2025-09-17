import telegram
import decouple
import os
import random
import argparse
import time


def send_picture(bot, chat_id, path, image):
    with open(f'{path}/{image}', 'rb') as file:
        bot.send_document(
            chat_id, document=file
            )


def main():
    parser = argparse.ArgumentParser(
        description='Бот для загрузки сообщений в телеграм'
    )
    parser.add_argument('--image', type=str, default=None,
                        help="Путь к файлу который вы хотите отправить"
                        )
    args = parser.parse_args()
    image = args.image

    bot = telegram.Bot(token=decouple.config('TG_BOT'))
    chat_id = decouple.config('TG_CHANNEL')
    path = 'images'

    if image is None:
        images = os.listdir(path)
        image = random.choice(images)

    while True:
        send_picture(bot, chat_id, path, image)
        images = os.listdir(path)
        image = random.choice(images)
        time.sleep(int(decouple.config('REST')))


if __name__ == '__main__':
    main()
