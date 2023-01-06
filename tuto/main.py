# fen nicolas

from telegram.ext import *
from telegram import Update
import constants as keys
import Responses as R

def start_command(update, context):
    update.message.reply_text('Type something radom to get started!')

def help_command(update, context):
    update.message.reply_text('If you need help you should ask for it on Google!')

def handle_message(update, context):
    text = str(update.message.text).lower()
    response = R.sample_responses(text)    
    update.message.reply_text(response)

def error(update, context):
    print(f"Update {update} caused error {context.error}")

def main():
    updater = Updater(keys.API_KEY, use_context = True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start_command))
    dp.add_handler(CommandHandler("help", help_command))
    dp.add_handler(MessageHandler(filters.text, handle_message))
    dp.add_error_handler(error)

    updater.start_polling() #5 -> checks user input each 5 seconds
    updater.idle() #so the bot stays active

#------Execution------
print("Bot started...")
main()
