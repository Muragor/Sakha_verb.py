from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from keyboards import kb_clien
from Sakha_verb import *
Verb_tel = Verb()
class FSMclien(StatesGroup):
    word = State()
    time = State()
    count = State()
    face = State()
async def start(message : types.Message):
    await message.answer("Это бот, который склоняет якутские глаголы. Напишите в чате '/Слово' и начните склонять", reply_markup=kb_clien)
async def word_sakha(message : types.Message):
    await message.answer("Якутские буквы:")
    await message.answer("ҥ")
    await message.answer("ҕ")
    await message.answer("ө")
    await message.answer("һ")
    await message.answer("ү")
#Начало диалога
async def word_text(message : types.Message):
    await FSMclien.word.set()
    await message.reply("Напишите ваш глагол")
#Введение глагола
async def load_word(message : types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['verb'] = message.text
    await FSMclien.next()
    await message.reply("Введите время. 1 - будущее, 2 - настоящее, 3 -прошедшее, 4 - недавнопрошедшее, 5 - настоящее время еще не совершившегося действия")
#Введение времени глагола
async def load_time(message : types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['time_verb'] = message.text
    await FSMclien.next()
    await message.reply("Введите число. 1 - единственное, 2 - множественное")
#Введение числа глагола
async def load_count(message : types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['count_verb'] = message.text
    await FSMclien.next()
    await message.reply("Введите лицо. 1 - первое лицо, 2 - второе лицо, 3 - третье лицо")
#Введение лциа глагола
async def load_face(message : types.Message, state: FSMContext):
    async with state.proxy() as data:
           data['face_verb'] = message.text
           verb = str(data['verb'])
           time_verb = data['time_verb']
           count_verb = int(data['count_verb'])
           face_verb = int(data['face_verb'])

    await message.reply(Verb_tel.verb_finnaly(verb, time_verb, count_verb, face_verb))

    await state.finish()

def register_handlers_client(dp : Dispatcher ):
    dp.register_message_handler(start, commands=['start'])
    dp.register_message_handler(word_text, commands=['Слово'], state=None)
    dp.register_message_handler(load_word, state=FSMclien.word)
    dp.register_message_handler(load_time, state=FSMclien.time)
    dp.register_message_handler(load_count, state=FSMclien.count)
    dp.register_message_handler(load_face, state=FSMclien.face)
    dp.register_message_handler(word_sakha, commands=['Буквы'])
