import telegram
import decouple
import os
import random
import argparse
import time


def send_picture(bot, chat_id, path, image):
    with open(f'{path}/{image}', 'rb') as file:
        bot.send_document(chat_id, document=file)


def main():
    parser = argparse.ArgumentParser(
        description='Бот для загрузки сообщений в телеграм'
    )
    path = 'images'
    images = os.listdir(path)

    parser.add_argument('--image', type=str, default=random.choice(images), help="Путь к файлу который вы хотите отправить")
    args = parser.parse_args()
    image = args.image

    bot = telegram.Bot(token=decouple.config('TG_BOT'))
    chat_id = decouple.config('TG_CHANNEL')
    rest = decouple.config('REST')

    while True:
        send_picture(bot, chat_id, path, image)
        image = random.choice(images)
        time.sleep(int(rest))


if __name__ == '__main__':
    main()

