# launcher.sh
#!/bin/bash

BOT_DIR=~/Documents/lipu_tan_jan_sewi_bot
VENV_DIR=~/.virtualenvs/telegram-bot

# telegram-bot venv: python-telegram-bot, numpy

# install python-telegram-bot into telegram-bot venv
# $VENV_DIR/bin/pip install python-telegram-bot --upgrade

# pull last version of the bot
cd $BOT_DIR
git pull
cd ~/
echo "last version of the bot pulled from github"

# activate telegram-bot environment
# source $VENV_DIR/bit/activate
# execute lipu tan jan sewi bot
# python $BOT_DIR/main.py

# executing the bot without activating the venv beforehand
echo "executing bot:"
$VENV_DIR/bin/python $BOT_DIR/main.py

