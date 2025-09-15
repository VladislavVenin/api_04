import telegram
import decouple
import os
import random
import argparse
import time


def send_picture(chat_id, path, image=None):
    if image is None:
        images = os.listdir(path)
        image = random.choice(images)
    bot.send_document(
        chat_id, document=open(f'{path}/{image}', 'rb')
        )


parser = argparse.ArgumentParser()
parser.add_argument('image', type=str, default=None)
args = parser.parse_args()
image = args.image

bot = telegram.Bot(token=decouple.config('BOT'))
chat_id = decouple.config('CHANNEL')
path = 'images'

while True:
    send_picture(chat_id, path, image)
    image = None
    time.sleep(int(decouple.config('REST')))
