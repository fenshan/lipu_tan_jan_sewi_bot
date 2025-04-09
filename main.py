#fen nicolas
# tutorial https://github.com/python-telegram-bot/python-telegram-bot/wiki/Extensions---Your-first-Bot

import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters
from telegram.constants import ParseMode
import private
import dice

start_command_text = "start"
help_command_text = "help"
roll_dice_command_text = "roll_dice"
show_dice_command_text = "show_dice"

fen_user = "@nicolasfen"

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

#start
# async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
#     await context.bot.send_message(
#         chat_id=update.effective_chat.id, 
#         text=f"I am ✨lipu tan jan sewi✨, a tool for random text generation in toki pona by {fen_user} :)"
#     )

#help
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.effective_chat.id, 
        text=
            f"🔮 Use <b>/{show_dice_command_text}</b> to show the word configuration in the 23 dice. All pu and ku suli words currently included (137).\n\n"

            f"🔮 Use <b>/{roll_dice_command_text}</b> to roll the dice!\n"
                f"   ⛤ You can specify a number N between 1 and {dice.MAX_N} with the number of dice you want to roll. "
                    f"If a number is not specified, {dice.DEFAULT_N} dice will be rolled.\n"
                f"   ⛤ After specifying N, you can list up to N specific dice that you want to be rolled (repetitions are valid).\n"
                f"   ⛤ ⸸jan sewi⸸ will avoid choosing repeated dice when possible.\n\n"

            f"Examples:\n"
                f"   <code>/{roll_dice_command_text}</code> -> {dice.DEFAULT_N} dice will be rolled: ?, ?, ?, ?, ?, ?\n"
                f"   <code>/{roll_dice_command_text} 3</code> -> 3 dice will be rolled: ?, ?, ?\n"
                f"   <code>/{roll_dice_command_text} 8 3 19 8 3</code> -> 8 dice will be rolled: 3, 19, 8, 3, ?, ?, ?, ?\n\n"
            
            f"🔮 Message {fen_user} if you have any requests.",
        # parse_mode = ParseMode.MARKDOWN_V2
        parse_mode = ParseMode.HTML
    )

#roll dice
async def roll_dice_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    response = dice.roll_dice(context.args, help_command_text)
    await context.bot.send_message(chat_id=update.effective_chat.id, text=response, parse_mode = ParseMode.HTML)

#show dice
async def show_dice_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    response = dice.show_dice()
    await context.bot.send_message(chat_id=update.effective_chat.id, text=response)

if __name__ == '__main__':
    # If you create an Application object, using ApplicationBuilder, it will automatically create a Updater for you and link them together with an asyncio.Queue
    application = ApplicationBuilder().token(private.API_KEY).build()

    start_handler = CommandHandler(start_command_text, help_command)
    help_handler = CommandHandler(help_command_text, help_command)
    roll_dice_handler = CommandHandler(roll_dice_command_text, roll_dice_command)
    show_dice_handler = CommandHandler(show_dice_command_text, show_dice_command)

    application.add_handler(start_handler)
    application.add_handler(help_handler)
    application.add_handler(roll_dice_handler)
    application.add_handler(show_dice_handler)

    application.run_polling()
