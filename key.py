from aiogram import types

import Database

db = Database.DateB()

glav_key = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
gl_buttn = types.KeyboardButton('Полные лекции')
gl_buttn2 = types.KeyboardButton('Короткие видео')
gl_buttn3 = types.KeyboardButton('Ссылки, книги')
glav_key.add(gl_buttn, gl_buttn2, gl_buttn3)


def get_full_thems_keys():
    key_board = types.InlineKeyboardMarkup(row_width=1)
    groups = db.get_all_group()
    for i in range(len(groups)):
        key = types.InlineKeyboardButton(text=groups[i][0], callback_data=f"full-{groups[i][0]}")
        key_board.add(key)
    return key_board


def get_short_thems_keys():
    key_board = types.InlineKeyboardMarkup(row_width=1)
    groups = db.get_all_group()
    for i in range(len(groups)):
        key = types.InlineKeyboardButton(text=groups[i][0], callback_data=f"short-{groups[i][0]}")
        key_board.add(key)
    return key_board


print(get_short_thems_keys())
