from aiogram import types, dispatcher
from aiogram.utils import executor
from create_bot import dp

async def on_startup():
    print('Бот работает')

from handlers import clien, admin, other

clien.register_handlers_client(dp)




executor.start_polling(dp, skip_updates=True)
