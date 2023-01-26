from telethon import TelegramClient, events
import telebot

#брать с сайта телеграмма https://my.telegram.org/auth
api_id = ''
api_hash = ''

client = TelegramClient('mirror', api_id, api_hash)

#брать из botFather
bot = telebot.TeleBot('')
client.start()

#id чата, из которого нужно миррорить
@client.on(events.NewMessage(-1111111111111))
async def main1(event):
    sender = await event.get_sender()
    who = "Пишет " + sender.first_name + ": "

    #id чата куда мирорить
    bot.send_message(-111111111111, who)
    bot.send_message(-111111111111, event.message)

client.run_until_disconnected()

