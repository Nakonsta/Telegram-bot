from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton, 
  InlineKeyboardMarkup, InlineKeyboardButton)
from aiogram.utils.keyboard import InlineKeyboardBuilder
from app.database.requests import get_categories 

main = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Каталог')],[KeyboardButton(text='Корзина')], [KeyboardButton(text='Контакты'), KeyboardButton(text='О нас')]],
  resize_keyboard=True,input_field_placeholder='Выберите пункт меню')

# catalog = InlineKeyboardMarkup(inline_keyboard=[
#   [InlineKeyboardButton(text='Футболки', callback_data='t-shirt')],
#   [InlineKeyboardButton(text='Кроссовки', callback_data='sneakers')], 
#   [InlineKeyboardButton(text='Кепки', callback_data='cap')]
# ])

async def categories():
  all_categories = await get_categories()
  keyboard = InlineKeyboardBuilder()
  for category in all_categories:
    keyboard.add(InlineKeyboardButton(text=category.name, callback_data=f"category_{category.id}"))
  keyboard.add(InlineKeyboardButton(text='На главную', callback_data='to_main'))
  return keyboard.adjust(2).as_markup()


get_number = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Отправить номер', request_contact=True)]], resize_keyboard=True)