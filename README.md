# test_telegram_bot
Бот для Telegram для тестового задания

Доступные комманды:
1. /start - Выводит список доступных комманд с кратким описанием
1. /run_poll _N_ - Запускает периодический опрос базы данных и возвращает размеры таблиц каждые _N_ минут
1. /poll - Единичный запрос размеров таблиц
1. /exec _QUERY_ - исполняет запрос _QUERY_ на базе данных и возвращает результат, если он есть

Использовалась реализация [API Telegram](https://github.com/python-telegram-bot/python-telegram-bot)

И [драйвер PostgreSQL](https://github.com/python-postgres/fe)
