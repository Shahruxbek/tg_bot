from aiogram.types import ReplyKeyboardMarkup,KeyboardButton
from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton


main_menu = ReplyKeyboardMarkup(resize_keyboard=True)
tel_reg = KeyboardButton(text='📱Telefon Registion📱')

main_menu.add(tel_reg)