from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext

from keybords.setings import get_back_kb
from states.search import SearchForm

router = Router()


@router.message(F.text == "🔍 Поиск")
async def search_kb(message: Message, state: FSMContext):
    await message.answer("Что ищете?", reply_markup=get_back_kb())
    await state.set_state(SearchForm.query)


@router.message(SearchForm.query, F.text)
async def get_text_search_kb(message: Message, state: FSMContext):
    query = message.text
    await state.update_data(query=query)


    data = [
        {"pageId": "1234"},
        {"pageId": "1"}
    ]

    await message.answer("Выбор статьи:", reply_markup=get_back_kb(data))
    await state.set_state(SearchForm.article)


@router.callback_query(SearchForm.article, F.data.func(lambda x: x.isdigit()))
async def callback_search_kb(callback: CallbackQuery, state: FSMContext):
    await state.update_data(article=callback.data)
    data = await state.get_data()

    print(data)
    await callback.message.answer(f"Вы выбрали статью ID: {callback.data}")

