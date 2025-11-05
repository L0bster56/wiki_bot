from aiogram.utils.keyboard import InlineKeyboardBuilder

def get_article_kb(data):
    builder = InlineKeyboardBuilder()

    for i, article in enumerate(data, start=1):
        page_id = article.get("pageid")
        builder.button(text=str(i), callback_data=f"article.{page_id}")

    builder.adjust(5,5)
    return builder.as_markup()


def get_article_link_kb(url, leng="ru"):
    builder = InlineKeyboardBuilder()
    builder.button(text="Просмотреть статью", url=url)
    return builder.as_markup()
