from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

b1 = KeyboardButton('/режим_работы')
b2 = KeyboardButton('/расположение')
b3 = KeyboardButton('/меню')

# замещает обычную клавиатуру на ту, которую мы создаём
kb_client = ReplyKeyboardMarkup(resize_keyboard=True)

kb_client.add(b1).add(b2).insert(b3)
