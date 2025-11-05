from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext
from pyexpat.errors import messages

from keybords.search import get_article_kb, get_article_link_kb
from keybords.setings import get_back_kb
from servises.res import get_wiki_kb
from servises.search import get_wikw_results
from states.search import SearchForm

router = Router()


@router.message(F.text == "🔍 Поиск")
async def search_kb(message: Message, state: FSMContext):
    await message.answer("Что ищете?", reply_markup=get_back_kb())
    await state.set_state(SearchForm.query)


@router.message(SearchForm.query, F.text)
async def get_text_search_kb(message: Message, state: FSMContext):
    query = message.text

    data = get_wikw_results(query)
    if len(data) == 0:
        await message.answer("Напишите по другому")
        await state.set_state(SearchForm.query)
        return None

    text = "Выберите статью "
    for i in range(len(data)):
        text += f"\n<b>{i+1}</b>. {data[i].get('title')}, "


    await message.answer(f"{text}", reply_markup=get_article_kb(data))
    await state.set_state(SearchForm.article)


@router.callback_query(F.data.startswith("article"),SearchForm.article)
async def article_handler(cb: CallbackQuery, state: FSMContext):
    pageid_1 = cb.data.split(".")[1]
    pageid = int(pageid_1)
    text,url = get_wiki_kb(pageid, "ru")
    await state.update_data(article=cb.data)
    data = await state.get_data()
    print(data)
    await cb.message.delete()
    await cb.message.answer(text,reply_markup=get_article_link_kb(url))
    await cb.message.answer(text,reply_markup=get_article_link_kb(url))
    await state.clear()
