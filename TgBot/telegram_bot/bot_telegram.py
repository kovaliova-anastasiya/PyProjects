# файл явялется точкой входа
from aiogram.utils import executor  # запуск бота, чтобы он вышел в онлайн
from create_bot import dp
from hadlers import admin, other, client
from data_base import sqlite_db


async def on_startup(_):
    print('Бот вышел в онлайн!')
    sqlite_db.sql_start()

client.register_handlers_client(dp)
admin.register_handlers_admin(dp)
other.register_handlers_other(dp)


# сейчас бот работает в режиме LongPolling
executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
# бот не будет отвечать на те сообщения, когда он был не онлайн
