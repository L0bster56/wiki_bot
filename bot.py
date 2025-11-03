from aiogram import Bot, Dispatcher, F
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from configs import TOKEN

from routers.start import router as start_router
from routers.about import router as start_about_router
from routers.setings import router as start_setings_router
from routers.search import router as start_search_router

properties = DefaultBotProperties(
    parse_mode=ParseMode.HTML
)

bot = Bot(token=TOKEN, default=properties)
dp = Dispatcher()


dp.include_router(start_router)
dp.include_router(start_about_router)
dp.include_router(start_setings_router)
dp.include_router(start_search_router)



