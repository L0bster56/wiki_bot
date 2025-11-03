from aiogram import Router, F
from aiogram.types import Message
from keybords.setings import get_lang_kb, get_back_kb

router = Router()

@router.message(F.text == "⚙️ Настройки")
async def setings(message: Message):
    await message.answer("Выберите язык:", reply_markup=get_back_kb())
    await message.answer("Выберите язык:", reply_markup=get_lang_kb())