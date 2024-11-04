from aiogram import Bot, Dispatcher, types, executor
import sqlite3

from keyboards import markups as kb
from config import config
from data import text_data as te

bot = Bot(token=config.BOT_TOKEN)
dp = Dispatcher(bot)

gg = []

rate1 = []
rate2 = []

admin_id = []

file_id = 0

mailing = 0

state = 0

user_id = []

score = 0
idd = 0

base = sqlite3.connect('table.db')
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


@dp.message_handler(commands=['setup'])
async def start_cmd(message: types.Message):
    global state
    await bot.send_message(message.from_user.id,te.ENTER_KEY,reply_markup=kb.cancel)
    state = 1
    await bot.delete_message(message.from_user.id, message.message_id)

@dp.message_handler(commands=['mailing'])
async def start_cmd(msg: types.Message):
    global state

    await bot.send_message(msg.from_user.id, te.MAILING_INFO)
    state = 2

@dp.callback_query_handler(text='back_to_menu')
async def menu(msg: types.Message):
    id = msg.from_user.id
    await bot.send_message(id,te.START2,reply_markup=kb.menu)
    await bot.delete_message(msg.from_user.id, msg.message.message_id)
    await bot.delete_message(msg.from_user.id, msg.message.message_id-1)

@dp.callback_query_handler(text='menu_1')
async def menu(msg: types.Message):
    global state
    state = 6
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


@dp.callback_query_handler(text='mailing')
async def menu(msg: types.Message):
    id = msg.from_user.id
    await bot.send_message(id,te.MAILING_TEXT,reply_markup=kb.mailing)
    await bot.delete_message(msg.from_user.id, msg.message.message_id)


@dp.callback_query_handler(text='off_on_mailing')
async def menu(msg: types.Message):
    global mailing
    id = msg.from_user.id
    mailing+=1
    if mailing % 2 ==1:
        await bot.send_message(id, te.ON_MAILING, reply_markup=kb.mailing)
        await bot.delete_message(msg.from_user.id, msg.message.message_id)
    elif mailing % 2 ==0:
        await bot.send_message(id, te.OFF_MAILING, reply_markup=kb.mailing)
        await bot.delete_message(msg.from_user.id, msg.message.message_id)
    if mailing == 10:
        mailing = 0


#Даты
@dp.callback_query_handler(text='1')
async def menu(msg: types.Message):
    global gg
    gg.append('1')
    id = msg.from_user.id
    await bot.send_message(id,te.EXCURSION_TIME,reply_markup=kb.time)
    await bot.delete_message(msg.from_user.id, msg.message.message_id)


@dp.callback_query_handler(text='2')
async def menu(msg: types.Message):
    global gg
    gg.append('2')
    id = msg.from_user.id
    await bot.send_message(id, te.EXCURSION_TIME, reply_markup=kb.time)
    await bot.delete_message(msg.from_user.id, msg.message.message_id)


@dp.callback_query_handler(text='3')
async def menu(msg: types.Message):
    global gg
    gg.append('3')
    id = msg.from_user.id
    await bot.send_message(id, te.EXCURSION_TIME, reply_markup=kb.time)
    await bot.delete_message(msg.from_user.id, msg.message.message_id)


@dp.callback_query_handler(text='4')
async def menu(msg: types.Message):
    global gg
    gg.append('4')
    id = msg.from_user.id
    await bot.send_message(id, te.EXCURSION_TIME, reply_markup=kb.time)
    await bot.delete_message(msg.from_user.id, msg.message.message_id)


@dp.callback_query_handler(text='5')
async def menu(msg: types.Message):
    global gg
    gg.append('5')
    id = msg.from_user.id
    await bot.send_message(id, te.EXCURSION_TIME, reply_markup=kb.time)
    await bot.delete_message(msg.from_user.id, msg.message.message_id)


@dp.callback_query_handler(text='6')
async def menu(msg: types.Message):
    global gg
    gg.append('6')
    id = msg.from_user.id
    await bot.send_message(id, te.EXCURSION_TIME, reply_markup=kb.time)
    await bot.delete_message(msg.from_user.id, msg.message.message_id)


@dp.callback_query_handler(text='7')
async def menu(msg: types.Message):
    global gg
    gg.append('7')
    id = msg.from_user.id
    await bot.send_message(id, te.EXCURSION_TIME, reply_markup=kb.time)
    await bot.delete_message(msg.from_user.id, msg.message.message_id)


@dp.callback_query_handler(text='8')
async def menu(msg: types.Message):
    global gg
    gg.append('8')
    id = msg.from_user.id
    await bot.send_message(id, te.EXCURSION_TIME, reply_markup=kb.time)
    await bot.delete_message(msg.from_user.id, msg.message.message_id)


@dp.callback_query_handler(text='9')
async def menu(msg: types.Message):
    global gg
    gg.append('9')
    id = msg.from_user.id
    await bot.send_message(id, te.EXCURSION_TIME, reply_markup=kb.time)
    await bot.delete_message(msg.from_user.id, msg.message.message_id)


@dp.callback_query_handler(text='10')
async def menu(msg: types.Message):
    global gg
    gg.append('10')
    id = msg.from_user.id
    await bot.send_message(id, te.EXCURSION_TIME, reply_markup=kb.time)
    await bot.delete_message(msg.from_user.id, msg.message.message_id)


@dp.callback_query_handler(text='11')
async def menu(msg: types.Message):
    global gg
    gg.append('11')
    id = msg.from_user.id
    await bot.send_message(id, te.EXCURSION_TIME, reply_markup=kb.time)
    await bot.delete_message(msg.from_user.id, msg.message.message_id)


@dp.callback_query_handler(text='12')
async def menu(msg: types.Message):
    global gg
    gg.append('12')
    id = msg.from_user.id
    await bot.send_message(id, te.EXCURSION_TIME, reply_markup=kb.time)
    await bot.delete_message(msg.from_user.id, msg.message.message_id)


@dp.callback_query_handler(text='13')
async def menu(msg: types.Message):
    global gg
    gg.append('13')
    id = msg.from_user.id
    await bot.send_message(id, te.EXCURSION_TIME, reply_markup=kb.time)
    await bot.delete_message(msg.from_user.id, msg.message.message_id)


@dp.callback_query_handler(text='14')
async def menu(msg: types.Message):
    global gg
    gg.append('14')
    id = msg.from_user.id
    await bot.send_message(id, te.EXCURSION_TIME, reply_markup=kb.time)
    await bot.delete_message(msg.from_user.id, msg.message.message_id)


@dp.callback_query_handler(text='15')
async def menu(msg: types.Message):
    global gg
    gg.append('15')
    id = msg.from_user.id
    await bot.send_message(id, te.EXCURSION_TIME, reply_markup=kb.time)
    await bot.delete_message(msg.from_user.id, msg.message.message_id)


@dp.callback_query_handler(text='16')
async def menu(msg: types.Message):
    global gg
    gg.append('16')
    id = msg.from_user.id
    await bot.send_message(id, te.EXCURSION_TIME, reply_markup=kb.time)
    await bot.delete_message(msg.from_user.id, msg.message.message_id)


@dp.callback_query_handler(text='17')
async def menu(msg: types.Message):
    global gg
    gg.append('17')
    id = msg.from_user.id
    await bot.send_message(id, te.EXCURSION_TIME, reply_markup=kb.time)
    await bot.delete_message(msg.from_user.id, msg.message.message_id)


@dp.callback_query_handler(text='18')
async def menu(msg: types.Message):
    global gg
    gg.append('18')
    id = msg.from_user.id
    await bot.send_message(id, te.EXCURSION_TIME, reply_markup=kb.time)
    await bot.delete_message(msg.from_user.id, msg.message.message_id)


@dp.callback_query_handler(text='19')
async def menu(msg: types.Message):
    global gg
    gg.append('19')
    id = msg.from_user.id
    await bot.send_message(id, te.EXCURSION_TIME, reply_markup=kb.time)
    await bot.delete_message(msg.from_user.id, msg.message.message_id)


@dp.callback_query_handler(text='20')
async def menu(msg: types.Message):
    global gg
    gg.append('20')
    id = msg.from_user.id
    await bot.send_message(id, te.EXCURSION_TIME, reply_markup=kb.time)
    await bot.delete_message(msg.from_user.id, msg.message.message_id)


@dp.callback_query_handler(text='21')
async def menu(msg: types.Message):
    global gg
    gg.append('21')
    id = msg.from_user.id
    await bot.send_message(id, te.EXCURSION_TIME, reply_markup=kb.time)
    await bot.delete_message(msg.from_user.id, msg.message.message_id)


@dp.callback_query_handler(text='22')
async def menu(msg: types.Message):
    global gg
    gg.append('22')
    id = msg.from_user.id
    await bot.send_message(id, te.EXCURSION_TIME, reply_markup=kb.time)
    await bot.delete_message(msg.from_user.id, msg.message.message_id)


@dp.callback_query_handler(text='23')
async def menu(msg: types.Message):
    global gg
    gg.append('23')
    id = msg.from_user.id
    await bot.send_message(id, te.EXCURSION_TIME, reply_markup=kb.time)
    await bot.delete_message(msg.from_user.id, msg.message.message_id)


@dp.callback_query_handler(text='24')
async def menu(msg: types.Message):
    global gg
    gg.append('24')
    id = msg.from_user.id
    await bot.send_message(id, te.EXCURSION_TIME, reply_markup=kb.time)
    await bot.delete_message(msg.from_user.id, msg.message.message_id)


@dp.callback_query_handler(text='25')
async def menu(msg: types.Message):
    global gg
    gg.append('25')
    id = msg.from_user.id
    await bot.send_message(id, te.EXCURSION_TIME, reply_markup=kb.time)
    await bot.delete_message(msg.from_user.id, msg.message.message_id)


@dp.callback_query_handler(text='26')
async def menu(msg: types.Message):
    global gg
    gg.append('26')
    id = msg.from_user.id
    await bot.send_message(id, te.EXCURSION_TIME, reply_markup=kb.time)
    await bot.delete_message(msg.from_user.id, msg.message.message_id)


@dp.callback_query_handler(text='27')
async def menu(msg: types.Message):
    global gg
    gg.append('27')
    id = msg.from_user.id
    await bot.send_message(id, te.EXCURSION_TIME, reply_markup=kb.time)
    await bot.delete_message(msg.from_user.id, msg.message.message_id)


@dp.callback_query_handler(text='28')
async def menu(msg: types.Message):
    global gg
    gg.append('28')
    id = msg.from_user.id
    await bot.send_message(id, te.EXCURSION_TIME, reply_markup=kb.time)
    await bot.delete_message(msg.from_user.id, msg.message.message_id)
#Время
@dp.callback_query_handler(text='10:00')
async def menu(msg: types.Message):
    global gg
    id = msg.from_user.id

    await bot.send_message(7222770656,
                           te.FINAL_EXCURS + ' ' + str(gg[1]) + '\n в ' + str(gg[0]) + '\n на время : ' + '10:00')
    await bot.send_message(id,
                           te.FINAL_EXCURS + ' ' + str(gg[1]) + '\n в ' + str(gg[0]) + '\n на время : '+'10:00')
    await bot.send_message(id, te.SUCCES_ZAP, reply_markup=kb.menu)
    gg = []
    await bot.delete_message(msg.from_user.id, msg.message.message_id)


@dp.callback_query_handler(text='11:00')
async def menu(msg: types.Message):
    global gg
    id = msg.from_user.id
    await bot.send_message(7222770656,
                           te.FINAL_EXCURS + ' ' + str(gg[1]) + '\n в ' + str(
                               gg[0]) + '\n на время : ' + '11:00')
    await bot.send_message(id,
                           te.FINAL_EXCURS  + ' ' + str(gg[1]) + '\n в ' + str(
                               gg[0]) + '\n на время : ' + '11:00')
    await bot.send_message(id, te.SUCCES_ZAP, reply_markup=kb.menu)
    gg=[]
    await bot.delete_message(msg.from_user.id, msg.message.message_id)


@dp.callback_query_handler(text='12:00')
async def menu(msg: types.Message):
    global gg
    id = msg.from_user.id
    await bot.send_message(7222770656,
                           te.FINAL_EXCURS + ' ' + str(gg[1]) + '\n в ' + str(
                               gg[0]) + '\n на время : ' + '12:00')
    await bot.send_message(id,
                           te.FINAL_EXCURS  + ' ' + str(gg[1]) + '\n в ' + str(
                               gg[0]) + '\n на время : ' + '12:00')
    await bot.send_message(id, te.SUCCES_ZAP, reply_markup=kb.menu)
    gg = []
    await bot.delete_message(msg.from_user.id, msg.message.message_id)


@dp.callback_query_handler(text='13:00')
async def menu(msg: types.Message):
    global gg
    id = msg.from_user.id
    await bot.send_message(7222770656,
                           te.FINAL_EXCURS + ' ' + str(gg[1]) + '\n в ' + str(
                               gg[0]) + '\n на время : ' + '13:00')
    await bot.send_message(id,
                           te.FINAL_EXCURS  + ' ' + str(gg[1]) + '\n в ' + str(
                               gg[0]) + '\n на время : ' + '13:00')
    await bot.send_message(id, te.SUCCES_ZAP, reply_markup=kb.menu)
    gg = []
    await bot.delete_message(msg.from_user.id, msg.message.message_id)


@dp.callback_query_handler(text='14:00')
async def menu(msg: types.Message):
    global gg
    id = msg.from_user.id
    await bot.send_message(7222770656,
                           te.FINAL_EXCURS + ' ' + str(gg[1]) + '\n в ' + str(
                               gg[0]) + '\n на время : ' + '14:00')
    await bot.send_message(id,
                           te.FINAL_EXCURS + ' ' + str(gg[1]) + '\n в ' + str(
                               gg[0]) + '\n на время : ' + '14:00')
    await bot.send_message(id, te.SUCCES_ZAP, reply_markup=kb.menu)
    await bot.delete_message(msg.from_user.id, msg.message.message_id)


@dp.callback_query_handler(text='15:00')
async def menu(msg: types.Message):
    global gg
    id = msg.from_user.id
    await bot.send_message(7222770656,
                           te.FINAL_EXCURS + ' ' + str(gg[1]) + '\n в ' + str(
                               gg[0]) + '\n на время : ' + '15:00')
    await bot.send_message(id,
                           te.FINAL_EXCURS  + ' ' + str(gg[1]) + '\n в ' + str(
                               gg[0]) + '\n на время : ' + '15:00')
    gg = []
    await bot.send_message(id, te.SUCCES_ZAP, reply_markup=kb.menu)
    await bot.delete_message(msg.from_user.id, msg.message.message_id)


@dp.callback_query_handler(text='16:00')
async def menu(msg: types.Message):
    global gg
    id = msg.from_user.id
    await bot.send_message(7222770656,
                           te.FINAL_EXCURS + ' ' + str(gg[1]) + '\n в ' + str(
                               gg[0]) + '\n на время : ' + '16:00')
    await bot.send_message(id,
                           te.FINAL_EXCURS  + ' ' + str(gg[1]) + '\n в ' + str(
                               gg[0]) + '\n на время : ' + '16:00')
    await bot.send_message(id, te.SUCCES_ZAP, reply_markup=kb.menu)
    gg = []
    await bot.delete_message(msg.from_user.id, msg.message.message_id)


@dp.callback_query_handler(text='17:00')
async def menu(msg: types.Message):
    global gg
    id = msg.from_user.id
    await bot.send_message(7222770656,
                           te.FINAL_EXCURS + ' ' + str(gg[1]) + '\n в ' + str(
                               gg[0]) + '\n на время : ' + '17:00')
    await bot.send_message(id,
                           te.FINAL_EXCURS  + ' ' + str(gg[1]) + '\n в ' + str(
                               gg[0]) + '\n на время : ' + '17:00')
    await bot.send_message(id, te.SUCCES_ZAP, reply_markup=kb.menu)
    gg = []
    await bot.delete_message(msg.from_user.id, msg.message.message_id)
    gg.clear()


#Вывод данных

#месяца
@dp.callback_query_handler(text='jan')
async def menu(msg: types.Message):
    global gg
    gg.append('Января')
    id = msg.from_user.id
    await bot.send_message(id,te.EXCURSION_DATE,reply_markup=kb.calendar)
    await bot.delete_message(msg.from_user.id, msg.message.message_id)
@dp.callback_query_handler(text='feb')
async def menu(msg: types.Message):
    global gg
    gg.append('Февраля')
    id = msg.from_user.id
    await bot.send_message(id,te.EXCURSION_DATE,reply_markup=kb.calendar)
    await bot.delete_message(msg.from_user.id, msg.message.message_id)
@dp.callback_query_handler(text='mar')
async def menu(msg: types.Message):
    global gg
    gg.append('Марта')
    id = msg.from_user.id
    await bot.send_message(id,te.EXCURSION_DATE,reply_markup=kb.calendar)
    await bot.delete_message(msg.from_user.id, msg.message.message_id)
@dp.callback_query_handler(text='apr')
async def menu(msg: types.Message):
    global gg
    gg.append('Апреля')
    id = msg.from_user.id
    await bot.send_message(id,te.EXCURSION_DATE,reply_markup=kb.calendar)
    await bot.delete_message(msg.from_user.id, msg.message.message_id)
@dp.callback_query_handler(text='mai')
async def menu(msg: types.Message):
    global gg
    gg.append('Мая')
    id = msg.from_user.id
    await bot.send_message(id,te.EXCURSION_DATE,reply_markup=kb.calendar)
    await bot.delete_message(msg.from_user.id, msg.message.message_id)
@dp.callback_query_handler(text='iun')
async def menu(msg: types.Message):
    global gg
    gg.append('Июня')
    id = msg.from_user.id
    await bot.send_message(id,te.EXCURSION_DATE,reply_markup=kb.calendar)
    await bot.delete_message(msg.from_user.id, msg.message.message_id)
@dp.callback_query_handler(text='iul')
async def menu(msg: types.Message):
    global gg
    gg.append('Июля')
    id = msg.from_user.id
    await bot.send_message(id,te.EXCURSION_DATE,reply_markup=kb.calendar)
    await bot.delete_message(msg.from_user.id, msg.message.message_id)
@dp.callback_query_handler(text='avg')
async def menu(msg: types.Message):
    global gg
    gg.append('Августа')
    id = msg.from_user.id
    await bot.send_message(id,te.EXCURSION_DATE,reply_markup=kb.calendar)
    await bot.delete_message(msg.from_user.id, msg.message.message_id)
@dp.callback_query_handler(text='sent')
async def menu(msg: types.Message):
    global gg
    gg.append('Сентября')
    id = msg.from_user.id
    await bot.send_message(id,te.EXCURSION_DATE,reply_markup=kb.calendar)
    await bot.delete_message(msg.from_user.id, msg.message.message_id)
@dp.callback_query_handler(text='okt')
async def menu(msg: types.Message):
    global gg
    gg.append('Октября')
    id = msg.from_user.id
    await bot.send_message(id,te.EXCURSION_DATE,reply_markup=kb.calendar)
    await bot.delete_message(msg.from_user.id, msg.message.message_id)
@dp.callback_query_handler(text='noyab')
async def menu(msg: types.Message):
    global gg
    gg.append('Ноября')
    id = msg.from_user.id
    await bot.send_message(id,te.EXCURSION_DATE,reply_markup=kb.calendar)
    await bot.delete_message(msg.from_user.id, msg.message.message_id)
@dp.callback_query_handler(text='dec')
async def menu(msg: types.Message):
    global gg
    gg.append('Декабря')
    id = msg.from_user.id
    await bot.send_message(id,te.EXCURSION_DATE,reply_markup=kb.calendar)
    await bot.delete_message(msg.from_user.id, msg.message.message_id)


@dp.message_handler(content_types=["photo"])
async def get_photo(message):
    global file_id
    global user_id
    global admin_id

    if message.from_user.id in admin_id:
        file_id = message.photo[-1].file_id
        caption = message.caption
        print(file_id) # этот идентификатор нужно где-то сохранить
        await bot.delete_message(message.from_user.id, message.message_id)
        for i in user_id:
            try:
                await bot.send_photo(chat_id=i, photo=file_id, caption=caption)
                state = 0
            except Exception as e:
                print('сырный тут')
    else:
        await bot.delete_message(message.from_user.id, message.message_id)
#Записать на экскурсию
@dp.callback_query_handler(text='excursion_mount')
async def menu(msg: types.Message):
    id = msg.from_user.id
    await bot.send_message(id,te.EXCURSION_MOUNT,reply_markup=kb.mount)
    await bot.delete_message(msg.from_user.id, msg.message.message_id)

@dp.callback_query_handler(text='excursion_date')
async def menu(msg: types.Message):
    id = msg.from_user.id
    await bot.send_message(id,te.EXCURSION_DATE,reply_markup=kb.calendar)
    await bot.delete_message(msg.from_user.id, msg.message.message_id)

@dp.message_handler(content_types=types.ContentTypes.ANY)
async def all_other_messages(message: types.Message):
    global state
    global admin_id
    # await bot.send_message(message.from_user.id,'Не понял вас')
    g = message.from_user.id
    d = message.message_id

    if state == 1:
        if message.text == te.ADMIN_KEY:
            await bot.send_message(g, te.ACCES)
            await bot.delete_message(g, d)
            await bot.delete_message(g, d - 1)
            if message.from_user.id not in admin_id:
                admin_id.append(g)
                state = 0
        else:
            await bot.send_message(g, te.NOTACCES, reply_markup=kb.cancel)
            await bot.delete_message(g, d)
            await bot.delete_message(g, d - 1)
    elif state == 2:
        for i in user_id:
            try:
                await bot.send_message(i,message.text)
                state = 0
            except Exception as e:
                print('сырный и тут')
    elif state == 2:
        await bot.send_message(g,'Ваше заявление успешно отправлено, если что либо не успели дописать, то отправьте повтороное завление в одном сообщении',reply_markup=kb.menu)
        await bot.send_message(7222770656, 'Новое заявление \n\n' + message.text + message.from_user.username)
        state = 0
    else:
        await bot.send_message(g,'Не понял вас, повторите попытки или сформулируйте мысли')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
