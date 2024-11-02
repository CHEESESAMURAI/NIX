from aiogram import Bot, Dispatcher, types
import sqlite3

from django.db.migrations import executor

from keyboards import markups as kb
from config import config
from data import text_data as te

bot = Bot(token=config.BOT_TOKEN)
dp = Dispatcher(bot)

base = sqlite3.connect('../table.db')
cur = base.cursor()

@dp.message_handler(commands=['start'])
async def start_cmd(msg: types.Message):
    global user_id
    user_name = msg.from_user.username
    us_id = msg.from_user.id
    id = msg.chat.id
    await bot.send_message(id,te.START1 + str(user_name) + te.START2, reply_markup=kb.menu)
    await bot.delete_message(msg.from_user.id, msg.message_id)
    if us_id not in user_id:
        user_id.append(us_id)
        print(user_id)

@dp.callback_query_handler(text='back_to_menu')
async def menu(msg: types.Message):
    id = msg.from_user.id
    await bot.send_message(id,te.START2,reply_markup=kb.menu)
    await bot.delete_message(msg.from_user.id, msg.message.message_id)
    await bot.delete_message(msg.from_user.id, msg.message.message_id-1)

@dp.callback_query_handler(text='menu_1')
async def menu(msg: types.Message):
    id = msg.from_user.id
    await bot.send_message(id,te.menu_1,reply_markup=kb.back)
    await bot.delete_message(msg.from_user.id, msg.message.message_id)

@dp.callback_query_handler(text='menu_2')
async def menu(msg: types.Message):
    id = msg.from_user.id
    await bot.send_message(id,te.menu_2,reply_markup=kb.menu_2)
    await bot.delete_message(msg.from_user.id, msg.message.message_id)

@dp.callback_query_handler(text='menu_2_1')
async def menu(msg: types.Message):
    id = msg.from_user.id
    await bot.send_message(id,te.menu_2_1,reply_markup=kb.back)
    await bot.delete_message(msg.from_user.id, msg.message.message_id)

@dp.callback_query_handler(text='menu_2_2')
async def menu(msg: types.Message):
    id = msg.from_user.id
    await bot.send_message(id,te.menu_2_2,reply_markup=kb.back)
    await bot.delete_message(msg.from_user.id, msg.message.message_id)

@dp.callback_query_handler(text='menu_2_3')
async def menu(msg: types.Message):
    id = msg.from_user.id
    await bot.send_message(id,te.menu_2_3,reply_markup=kb.back)
    await bot.delete_message(msg.from_user.id, msg.message.message_id)

@dp.callback_query_handler(text='menu_3')
async def menu(msg: types.Message):
    id = msg.from_user.id
    await bot.send_message(id,te.menu_3,reply_markup=kb.menu_3)
    await bot.delete_message(msg.from_user.id, msg.message.message_id)

@dp.callback_query_handler(text='menu_3_1')
async def menu(msg: types.Message):
    id = msg.from_user.id
    await bot.send_message(id, te.menu_3_1, reply_markup=kb.back)
    await bot.delete_message(msg.from_user.id, msg.message.message_id)

@dp.callback_query_handler(text='menu_3_2')
async def menu(msg: types.Message):
    id = msg.from_user.id
    await bot.send_message(id, te.menu_3_2, reply_markup=kb.back)
    await bot.delete_message(msg.from_user.id, msg.message.message_id)

@dp.callback_query_handler(text='menu_3_3')
async def menu(msg: types.Message):
    id = msg.from_user.id
    await bot.send_message(id, te.menu_3_3, reply_markup=kb.back)
    await bot.delete_message(msg.from_user.id, msg.message.message_id)

@dp.callback_query_handler(text='menu_4')
async def menu(msg: types.Message):
    id = msg.from_user.id
    await bot.send_message(id,te.menu_4,reply_markup=kb.back)
    await bot.delete_message(msg.from_user.id, msg.message.message_id)

@dp.callback_query_handler(text='menu_5')
async def menu(msg: types.Message):
    id = msg.from_user.id
    await bot.send_message(id,te.menu_5,reply_markup=kb.back)
    await bot.delete_message(msg.from_user.id, msg.message.message_id)


@dp.message_handler(content_types=types.ContentTypes.ANY)
async def all_other_messages(message: types.Message):
    global state
    global admin_id
    await bot.send_message(message.from_user.id,'Не понял вас')
    g = message.from_user.id
    d = message.message_id


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
