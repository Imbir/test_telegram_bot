import threading
import postgresql
import time
from telegram import Update
from telegram.ext import CallbackContext
from telegram_bot import constants

threads = {}


def handle_start(update: Update, context: CallbackContext):
    message = '/run_poll N - start polling database every N minutes\n' \
              '/poll - poll database once\n' \
              '/exec QUERY - execute a QUERY, outputs results, if any'
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=message
    )


def poll_database(update: Update, context: CallbackContext):
    with postgresql.open(constants.get_db_connection_line()) as database:
        public_tables = database.prepare("SELECT * FROM pg_catalog.pg_tables where schemaname = 'public'")
        message = ''

        for table in public_tables():
            table_name = table['tablename']
            table_count = database.prepare(f'SELECT COUNT(*) FROM {table_name}')
            message += f'Table "{table_name}" contains {table_count()[0][0]} rows.\n'

        context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=message
        )


def poll_database_periodically(update: Update, context: CallbackContext, delay):
    chat_id = update.effective_chat.id
    while threads[chat_id]['run']:
        poll_database(update, context)
        time.sleep(delay)


def handle_run_poll(update: Update, context: CallbackContext):
    chat_id = update.effective_chat.id
    frequency = 60.0 * int(context.args[0])

    if chat_id in threads:
        threads[chat_id]['run'] = False
        threads[chat_id]['thread'].join()

    new_thread = threading.Thread(target=poll_database_periodically, args=(update, context, frequency))
    threads[chat_id] = {'thread': new_thread, 'run': True}
    new_thread.start()


def handle_poll(update: Update, context: CallbackContext):
    poll_database(update, context)


def handle_execute(update: Update, context: CallbackContext):
    query = ' '.join(context.args).strip()
    with postgresql.open(constants.get_db_connection_line()) as database:
        result = database.prepare(query)
        message = ''
        for row in result():
            message += str(row) + '\n'

    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=message
    )
    return
