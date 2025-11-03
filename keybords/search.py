from aiogram.utils.keyboard import ReplyKeyboardBuilder

def get_article_kb(data: list):
    bilder = ReplyKeyboardBuilder()

    i = 1
    for article in data:
        bilder.button(text=str(i), callback_data=article.get("pageId"))
        i+=1
    return bilder.as_markup()