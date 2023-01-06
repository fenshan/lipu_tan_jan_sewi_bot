#fen nicolas
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters
import constants #as keys
import dices as D

# https://github.com/python-telegram-bot/python-telegram-bot/wiki/Exceptions%2C-Warnings-and-Logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.effective_chat.id, 
        text="I'm a bot, please talk to me!"
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.effective_chat.id, 
        text="I'm a bot, please talk to me!"
    )

async def roll_dices_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    #use context.args
    await context.bot.send_message(
        chat_id=update.effective_chat.id, 
        text="I'm a bot, please talk to me!"
    )

async def show_dices_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    dices_text = ""
    for i, value_i in enumerate(D.dices):
        dices_text += str(i) + ": "
        for value_j in value_i:
            dices_text += value_j + " "
        dices_text += "\n"

    await context.bot.send_message(chat_id=update.effective_chat.id, text=dices_text)

if __name__ == '__main__':
    # If you create an Application object, using ApplicationBuilder, it will automatically create a Updater for you and link them together with an asyncio.Queue
    application = ApplicationBuilder().token(constants.API_KEY).build()

    start_handler = CommandHandler('start', start_command)
    help_handler = CommandHandler('help', help_command)
    roll_dices_handler = CommandHandler('roll_dices', roll_dices_command)
    show_dices_handler = CommandHandler('show_dices', show_dices_command)

    application.add_handler(start_handler)
    application.add_handler(help_handler)
    application.add_handler(roll_dices_handler)
    application.add_handler(show_dices_handler)

    application.run_polling()