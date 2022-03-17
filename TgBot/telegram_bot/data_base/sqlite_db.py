import sqlite3 as sq
from create_bot import bot


# создание базы данных
def sql_start():
    global base, cur
    base = sq.connect('pizza_cool.db')  # подключение к файлу бд или его создание
    cur = base.cursor()  # часть бд, которая осущ. поиск, встраиввание и выборку данных из бд
    if base:
        print('Data base connected ok')
    # создание таблицы для внесения данных
    base.execute('CREATE TABLE IF NOT EXISTS menu(img TEXT, name TEXT PRIMARY KEY, description TEXT, price TEXT)')
    # PRIMARY KEY - первичный ключ, повторяться название не будет
    base.commit()


async def sql_add_command(state):
    async with state.proxy() as data:
        cur.execute('INSERT INTO menu VALUES(?, ?, ?, ?)', tuple(data.values()))  # вставляем в табл значения из словаря
        base.commit()


async def sql_read(message):  # событие - сообщение от кнопки "/меню"
    for ret in cur.execute('SELECT * FROM menu').fetchall():
        await bot.send_photo(message.from_user.id, ret[0], f'{ret[1]}\nОписание: {ret[2]}\nЦена: {ret[-1]}')


async def sql_read2():  # чтение выборки из бд
    return cur.execute('SELECT * FROM menu').fetchall()


async def sql_delete_command(data):
    cur.execute('DELETE FROM menu WHERE name == ?', (data,))
    base.commit()