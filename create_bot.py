from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

storage=MemoryStorage()
bot = Bot(token='5947903189:AAF6rU7hJ04FP8zPvY078PO3_1Taq8X9OGc')
dp = Dispatcher(bot, storage=storage)
