from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram_bot.handlers import *
from telegram_bot.constants import *


updater = Updater(token=ACCESS_TOKEN, use_context=True)
dispatcher = updater.dispatcher

start_handler = CommandHandler('start', handle_start)
dispatcher.add_handler(start_handler)

run_poll_handler = CommandHandler('run_poll', handle_run_poll)
dispatcher.add_handler(run_poll_handler)

poll_handler = CommandHandler('poll', handle_poll)
dispatcher.add_handler(poll_handler)

execute_handler = CommandHandler('exec', handle_execute)
dispatcher.add_handler(execute_handler)

updater.start_polling()
