from aiogram import types, Dispatcher  # для написания аннотаций типов
from create_bot import dp, bot
import json
import string


# @dp.message_handler()  # обозначает событие, когда в чат кто-то ЧТО УГОДНО пишет. Пустой обработчик внизу!
async def echo_send(message: types.Message):
    if {i.lower().translate(str.maketrans('', '', string.punctuation)) for i in message.text.split(' ')}\
        .intersection(set(json.load(open('cenz.json')))):
        await message.reply('Нецензурная лексика запрещена')
        await message.delete()


def register_handlers_other(dp: Dispatcher):
    dp.register_message_handler(echo_send)