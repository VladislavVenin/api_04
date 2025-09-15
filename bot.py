import telegram
import decouple

bot = telegram.Bot(token=decouple.config('BOT'))
image = open("images/spacex_0.jpg")
bot.send_document(
    chat_id='@dsdsfasgrg', document=open('images/spacex_0.jpg', 'rb')
    )
