from aiogram import Router, F
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

router = Router()

@router.message(F.text == "🧏🏿‍♂️ О нас")
async def about(message: Message):
    text = (
        "🧠 *О нас*\n\n"
        "WIKI — это интеллектуальный Telegram-бот, созданный для быстрого поиска "
        "и получения полезной информации прямо в чате.\n"
        "Наша цель — сделать знания доступными каждому, без лишних усилий.\n\n"
        "📚 *Что умеет WIKI:*\n"
        "• Поиск информации по ключевым словам\n"
        "• Быстрые и удобные ответы\n"
        "• Ссылки на источники\n\n"
        "💬 *Мы в Telegram:*\n"
        "[@bananana_56](https://t.me/bananana_56)\n\n"
        "💻 *Исходный код и разработка:*\n"
        "[GitHub →](https://github.com/L0bster56)"
    )

    await message.answer(text=text, parse_mode="Markdown")
