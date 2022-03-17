# промежуточный файл нужен для произведения взаимоимпортов
# переносим сюда всё, что касается создания экземпляра бота

from aiogram import Bot
from aiogram.dispatcher import Dispatcher  # улавливает события в чате
import os
from aiogram.contrib.fsm_storage.memory import MemoryStorage  # позволяет хранить данные в оперативке, для админки
# для написания машины состояний - запоминать последовательность действий пользователя

storage = MemoryStorage()

bot = Bot(token=os.getenv('TOKEN'))
# инициализируем dispatcher
dp = Dispatcher(bot, storage=storage)
