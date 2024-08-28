from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

import config
from tasks import healtchecker_start


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print('Telegram start triggered!')
    healtchecker_start()
    await update.message.reply_text('Healtcheck has started!')


def telegram_handler():
    # Create the Application instance with the bot's token
    application = Application.builder().token(
        config.TELEGRAM_BOT_TOKEN).build()

    # Register handlers
    application.add_handler(CommandHandler('start', start))
    # application.add_handler(CommandHandler('sendfile', send_file))

    # Start the Bot
    application.run_polling()
