from dotenv import load_dotenv # come libreria
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import os # come classe

load_dotenv("variable.env")

TOKEN = os.getenv("TOKEN")

async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')


app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("hello", hello))

app.run_polling()

