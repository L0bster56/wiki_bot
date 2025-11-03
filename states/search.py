from aiogram.fsm.state import State, StatesGroup




# Шаги
class SearchForm(StatesGroup):
    query = State() #Шаг
    article = State()



