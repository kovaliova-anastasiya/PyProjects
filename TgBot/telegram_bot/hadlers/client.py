from aiogram import types, Dispatcher  # для написания аннотаций типов
from create_bot import dp, bot
from keyboards import kb_client
from data_base import sqlite_db


# @dp.message_handler(commands=['старт', 'помощь'])
async def commands_start(message: types.Message):
    try:
        await bot.send_message(message.from_user.id, 'Приятного аппетита', reply_markup=kb_client)  # педедали клаву
        await message.delete()
    except:
        await message.reply('Общение с ботом через ЛС, напишите ему по ссылке:\nhttps://t.me/Your_Pizza_Chef_Bot')


# @dp.message_handler(commands=['режим_работы'])
async def pizza_open_command(message: types.Message):
    await bot.send_message(message.from_user.id, 'Вс-Чт с 9:00 до 20:00, Пт-Сб с 10:00 до 23:00')


# @dp.message_handler(commands=['расположение'])
async def pizza_place_command(message: types.Message):
    await bot.send_message(message.from_user.id, 'ул. Кальварийская 15')


# @dp.message_handler(commands=['меню'])
async def pizza_menu_command(message: types.Message):
    await sqlite_db.sql_read(message)


# пишем команды для регистрации хэндлеров нашего бота, с помощью неё передаём их в основоной файл
def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(commands_start, commands=['старт', 'помощь'])
    dp.register_message_handler(pizza_open_command, commands=['режим_работы'])
    dp.register_message_handler(pizza_place_command, commands=['расположение'])
    dp.register_message_handler(pizza_menu_command, commands=['меню'])
