from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

b1 = KeyboardButton('/Слово')
b2 = KeyboardButton('/Буквы')
kb_clien = ReplyKeyboardMarkup(resize_keyboard=True)
kb_clien.add(b1).add(b2)