from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = "8973949729:AAET0FcnQriw_y5OBC7uV0CGsneErAVM9Qg"
APP_URL = "https://forgetsee1-commits.github.io/blag-mini-app/"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton("🕵️ Открыть Тайный Благовещенск", web_app=WebAppInfo(url=APP_URL))]
    ])
    await update.message.reply_text(
        "👋 Здорова!\n\nЖми кнопку — откроется окно.",
        reply_markup=keyboard
    )

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    print("Бот запущен!")
    app.run_polling()

if __name__ == "__main__":
    main()