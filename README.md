<img src="https://github.com/user-attachments/assets/d9e40660-97da-444a-a5cf-136db03b84da" width="500" height="auto">


# simple telegram bot made in python

simple telegram bot made in python using polling

## features

* list users
* show any info
* reset

## setup

```bash
git clone https://github.com/jasurlive/TelegramBotPy.git
cd TelegramBotPy

python -m venv .venv
source .venv/bin/activate

pip freeze > requirements.txt
pip install -r requirements.txt
or
pip install python-telegram-bot python-dotenv requests

```

.env

```
BOT_TOKEN=<your_telegram_token>
```

## run

```bash
python main.py
```

## systemd
use main.py as service on linux

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

[Install]
WantedBy=multi-user.target
```

```bash
sudo systemctl daemon-reload
sudo systemctl enable telegrambot
sudo systemctl start telegrambot
```

you'll also need these commands if you make any changes to main.py

## license

MIT
