from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters
from dotenv import load_dotenv
import os, requests, logging

load_dotenv()
TOKEN=os.getenv("BOT_TOKEN")

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(message)s")

kb=ReplyKeyboardMarkup([
    ["ℹ️ About Bot"],
    ["👥 Who is on shift today?"],
    ["🛠️ Who handles what?"],
    ["♻️ Reset Bot"],
], resize_keyboard=True)

def log(update: Update):
    user=update.effective_user
    logging.info(f"user_id={user.id} username={user.name} text={update.message.text}")

async def info(update, context):
    log(update)
    await update.message.reply_text(
        "This bot shows members and small info using api.\n\n"
        "Available actions:\n"
        "- View today's members\n"
        "- View user info\n"
        "- Reset bot state\n"
        "- /start to reload menu"
    )

async def reset(update, context):
    log(update)
    context.user_data.clear()
    await update.message.reply_text("Bot state has been reset.", reply_markup=kb)

async def users(update, context):
    log(update)
    users=requests.get("https://jsonplaceholder.typicode.com/users").json()
    out="\n".join(f"{u['name']}" for u in users)
    await update.message.reply_text(out)

async def numbers(update, context):
    log(update)
    users=requests.get("https://jsonplaceholder.typicode.com/users").json()
    out="\n".join(f"{u['name']} -> age {20 + u['id']}" for u in users)
    await update.message.reply_text(out)

routes={
    "ℹ️ About Bot": info,
    "👥 Who is on shift today?": users,
    "🛠️ Who handles what?": numbers,
    "♻️ Reset Bot": reset
}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log(update)
    await update.message.reply_text("Select an option:", reply_markup=kb)

async def handle(update: Update, context: ContextTypes.DEFAULT_TYPE):
    log(update)
    fn=routes.get(update.message.text)
    if fn: await fn(update, context)

app=ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle))
app.run_polling()