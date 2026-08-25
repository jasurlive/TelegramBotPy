<img src="https://github.com/user-attachments/assets/d9e40660-97da-444a-a5cf-136db03b84da" width="500" height="auto">


# simple telegram bot made in python

simple telegram bot made in python using polling

## features

* list users (open source json data used from *https://jsonplaceholder.typicode.com/users*)
* show any info
* reset the bot

## setup

```bash
git clone https://github.com/jasurlive/TelegramBotPy.git
cd TelegramBotPy

python -m venv .venv
source .venv/bin/activate

pip install -r requirements.txt
or
pip install python-telegram-bot python-dotenv requests

```

.env

```
BOT_TOKEN=<your_telegram_token>
ADMIN_ID=<your_telegram_id>
```

## run

```bash
python src/main.py
```

## systemd
use src/main.py as service on linux

sudo nano /etc/systemd/system/telegrambot.service (!)

```
[Unit]
Description=telegram bot
After=network.target

[Service]
WorkingDirectory=/home/YOURUSERNAME/bot
ExecStart=/home/YOURUSERNAME/bot/.venv/bin/python main.py

Restart=always
Environment="BOT_TOKEN=your_token"
Restart=always
Environment="ADMIN_ID=your_id"

[Install]
WantedBy=multi-user.target
```

```bash
sudo systemctl daemon-reload
sudo systemctl enable telegrambot
sudo systemctl start telegrambot
```

you'll also need to run these commands if you make any changes to main.py

## license

MIT
