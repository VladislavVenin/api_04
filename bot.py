import telegram
import decouple
import os
import random
import time

bot = telegram.Bot(token=decouple.config('BOT'))
chat_id = decouple.config('CHANNEL')
path = 'images'
images = os.listdir(path)
while True:
    bot.send_document(
        chat_id, document=open(f'{path}/{random.choice(images)}', 'rb')
        )
    time.sleep(decouple.config('REST'))