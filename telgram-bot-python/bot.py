"""
A Bot to reply telegram messages.
Echo-Bot that repeat messages
"""
import logging
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

#logging module
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logger = logging.getLogger(__name__)

#token generated after creating bot
TOKEN = "1530573294:AAGFpHGShEY4iqVTgd6-d-rHHguJ1eYvF9E"

#start fun return text defined in func when someone give command
def start(bot, update,context: CallbackContext):
    print(update)
    auther = update.message.from_user.first_name
    reply = "hi{}".format(auther)
    bot.send_message(chat_id=update.message.chat_id, text=reply)

#similarly all command,messages,error would be answered accc to defined fnction resp...
def _help(bot, update):
    text_help = "hey! this is the helper text"
    bot.send_message(chat_id=update.message.chat_id, text=text_help)


def echo_text(bot, update):
    reply = update.message.text
    bot.send_message(chat_id=update.message.chat_id, text=reply)


def echo_sticker(bot, update):
    reply = update.message.sticker.file_id
    bot.send_sticker(chat_id=update.message.chat_id, sticker=reply)


def error(bot, update):
    logger.error("update '%s' caused error '%s'", update, update.error)

#starting
def main():
    #creat updater by passing the token inside Updater
    updater = Updater(TOKEN,use_context=True)
    dp = updater.dispatcher      # dispatch reg handlers
    '''
    these are diif handlers which is use to answer the diff commands send by users
    these are both command and non-command handlers ie message or error... 
    '''
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", _help))
    dp.add_handler(MessageHandler(Filters.text, echo_text))
    dp.add_handler(MessageHandler(Filters.sticker, echo_sticker))
    dp.add_error_handler(error)

    updater.start_polling()   #start the bot by sending cont. req to telegram to check any command and message recived
    logger.info("starting...")#displaying this msg when starting this process
    updater.idle()

#entry->>
if __name__ == "__main__":
    main()