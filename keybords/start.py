from aiogram.utils.keyboard import ReplyKeyboardBuilder

def get_start_kb(leng: str = "ru"):
    bilder = ReplyKeyboardBuilder()
    bilder.button(text="🔍 Поиск")
    bilder.button(text="🧏🏿‍♂️ О нас")
    bilder.button(text="👨🏿‍🦯️ История поиск")
    bilder.button(text="⚙️ Настройки")

    bilder.adjust(1,3)

    return bilder.as_markup(resize_keyboard=True)