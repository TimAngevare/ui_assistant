from telegram.ext import Updater
from telegram.ext import CommandHandler


# Telegram bot
updater = Updater(token='1713632251:AAHSqbzXub852fruw3ngHypT3B12qxtkqSU', use_context=True)
dispatcher = updater.dispatcher

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="starting bot...")

def links(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Sending current links...")

def quote(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Which quote do you wanna add")
    controller.pulse((47,11,9))

def sleep(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id,text="Goodnight Tim")
    controller.pulse((26,38,18))

def stopping(update,context):
    context.bot.send_message(chat_id=update.effective_chat.id,text="Bye Bye")


start_handler = CommandHandler('start', start)
links_handler = CommandHandler('links', links)
quote_handler = CommandHandler('quote', quote)
sleep_handler = CommandHandler('gn', sleep)
stop = CommandHandler('stop', stopping)

dispatcher.add_handler(start_handler)
dispatcher.add_handler(links_handler)
dispatcher.add_handler(quote_handler)
dispatcher.add_handler(sleep_handler)
dispatcher.add_handler(stop)


updater.start_polling()
