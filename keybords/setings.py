from aiogram.types import InlineKeyboardMarkup, ReplyKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder, ReplyKeyboardBuilder


def get_lang_kb():
    builder =  InlineKeyboardMarkup()
    builder.button(text="🇷🇺", callback_data="lang_ru")
    builder.button(text="🏳️‍🌈", callback_data="lang_en")
    builder.button(text="🇺🇿", callback_data="lang_uz")
    return builder.as_markup(resize_keyboard=True)

def get_back_kb():
    builder = ReplyKeyboardBuilder()
    builder.button(text="➡️ Назад")
    return builder.as_markup(resize_keyboard=True)