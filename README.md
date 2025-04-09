# lipu_tan_jan_sewi_bot

python telegram bot using [python-telegram-bot](https://github.com/python-telegram-bot)

https://t.me/lipu_tan_jan_sewi_bot

[launcher.sh](launcher.sh) script to execute the bot as a `systemd` (`/etc/systemd/system/telegrambot.service`) from my Raspbery Pi.

telegrambot.sevice script:
```
[Unit]
Description=Telegram Bot Service: lipu tan jan sewi bot
After=network.target

[Service]
Type=simple
User=root
ExecStart=%h/Documents/lipu_tan_jan_sewi_bot/launcher.sh
Restart=on-failure

[Install]
WantedBy=multi-user.target

```
Useful commands:
- `sudo systemctl daemon-reload`
- `sudo systemctl enable telegrambot.service`
- `sudo systemctl start telegrambot.service`
- `sudo systemctl status telegrambot.service`
