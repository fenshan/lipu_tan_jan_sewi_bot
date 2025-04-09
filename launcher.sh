#!/bin/bash
# launcher.sh

BOT_DIR=/home/fnicolas/Documents/lipu_tan_jan_sewi_bot
VENV_DIR=/home/fnicolas/.virtualenvs/telegram-bot

# telegram-bot venv: python-telegram-bot, numpy

# install/upgrade python-telegram-bot into telegram-bot venv
# echo "install last version of python-telegram-bot into the python venv:"
# $VENV_DIR/bin/pip install python-telegram-bot --upgrade

# pull last version of the bot
echo "pull last version of the bot from github:"
cd $BOT_DIR
git pull
cd ~/

# activate telegram-bot environment
# source $VENV_DIR/bit/activate
# execute lipu tan jan sewi bot
# python $BOT_DIR/main.py

# executing the bot without activating the venv beforehand
echo "executing bot:"
$VENV_DIR/bin/python $BOT_DIR/main.py

