from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State,StatesGroup
from aiogram import Bot,Dispatcher,types,executor
from buttons import main_menu
from datas import add_to_db,start_db
from datas import show_datas

async def on_startup(_):
    await start_db()

class Registration(StatesGroup):
    name = State()
    pamet = State()
    operativ = State()
    dyumi = State()
    color = State()
    pixel = State()
    year = State()
    sena = State()
    photo = State()



API = '6728919621:AAH5W9ZwLfYQfC7MWE5tQCCoaDy3IM-KiKg'
PROXY_URL = "http://proxy.server:3128/"
bot = Bot(API,proxy=PROXY_URL)



dp = Dispatcher(bot)




@dp.message_handler(commands=['start'])
async def send_hi(message:types.Message):
    user = message.from_user.first_name
    await message.answer(text=f'Assalamu aleykum {user}!',
                         reply_markup=main_menu)
    

@dp.message_handler(text='📱Telefon Registion📱')
async def begin_telefon(message:types.Message):
    await message.answer(text='''Siz telefon registratsiya qildingiz...
Bizge Telefonding atin ayting📝:''',)
    await Registration.name.set()

@dp.message_handler(state=Registration.name)
async def set_name(message:types.Message,state:FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text
    await message.answer(text='Endi pemetin jazip qaldiring♻️:')
    await Registration.pamet.set()

@dp.message_handler(state=Registration.pamet)
async def set_pamet(message:types.Message,state:FSMContext):
    async with state.proxy() as data:
        data['pamet'] = message.text
    await message.answer(text='Endi bizge operativin  ayting🗑:')
    await Registration.operativ.set()

@dp.message_handler(state=Registration.operativ)
async def set_operativ(message:types.Message,state:FSMContext):
    async with state.proxy() as data:
        data['operativ'] = message.text
    await message.answer(text='Endi bizge dyumin ayting📏:')
    await Registration.dyumi.set()

@dp.message_handler(state=Registration.dyumi)
async def set_dyum(message:types.Message,state:FSMContext):
    async with state.proxy() as data:
        data['dyumi'] = message.text
    await message.answer(text='Endi bizge svetin ayting🔵:')
    await Registration.color.set()

@dp.message_handler(state=Registration.color)
async def set_color(message:types.Message,state:FSMContext):
    async with state.proxy() as data:
        data['color'] = message.text
    await message.answer(text='Endi bizge pixelin ayting📷:')
    await Registration.pixel.set()

@dp.message_handler(state=Registration.pixel)
async def set_pix(message:types.Message,state:FSMContext):
    async with state.proxy() as data:
        data['pixel'] = message.text
    await message.answer(text='Endi bizge jilin ayting📅:')
    await Registration.year.set()

@dp.message_handler(state=Registration.year)
async def set_year(message:types.Message,state:FSMContext):
    async with state.proxy() as data:
        data['year'] = message.text
    await message.answer(text='Endi bizge senasin ayting💶:')
    await Registration.sena.set()

@dp.message_handler(state=Registration.sena)
async def set_sena(message:types.Message,state:FSMContext):
    async with state.proxy() as data:
        data['sena'] = message.text
    await message.answer(text='Endi bizge potosin tastang🌉:')
    await Registration.photo.set()

@dp.message_handler(state=Registration.photo,content_types=['photo'])
async def set_photo(message:types.Message,state:FSMContext):
    img_id = message.photo[0].file_id
    async with state.proxy() as data:
        data['photo'] = img_id
        await  add_to_db(
            ati=data['name'],
            xotira=data['pamet'],
            operat=data['operativ'],
            ulkenligi=data['dyumi'],
            reni=data['color'],
            kam=data['pixel'],
            jili=data['year'],
            cena=data['sena'],
            photo=data['photo']
        )
    await bot.send_photo(
        photo=img_id,
        chat_id=message.from_user.id,
        caption=f'''Registratciya Juwmaqlandi:
📱ati: {data['name']},
🗑pameti: {data['pamet']},
♻️operativi: {data['operativ']},
📏dyum: {data['dyumi']},
🔵sveti: {data['color']},
📷kamerasi: {data['pixel']},
📅jili: {data['year']},
💵senasi: {data['sena']}''')
    await state.finish()



@dp.message_handler(commands=['phones'])
async def show_phones(message:types.Message):
    phones = await show_datas()
    for phone in phones:
        await message.answer(phone)
        




if __name__=='__main__':
    executor.start_polling(dp,skip_updates=True,on_startup=on_startup)

