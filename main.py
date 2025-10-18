import os
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram import F

import asyncio 

load_dotenv()
BOT_TOKEN = os.getenv("TG_API_KEY")

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

# Бот - питомцы

pets = {} # База данных нашего бота(словарь)

 # Делаем клавиатуру для бота
main_kb = types.ReplyKeyboardMarkup(
    keyboard=[
       [types.KeyboardButton(text="🎉Покормить"), types.KeyboardButton(text="🎈Поиграть")],
       [types.KeyboardButton(text="💤Спать"), types.KeyboardButton(text="🛠Статус")],
       [types.KeyboardButton(text="🎺Выход")] # Создаём кнопку - внизу будет кнопка "выход"
    ],
    resize_keyboard=True # Расстягивает клавиатуру по экран
 )

@dp.message(Command("start"))
async def start_handler(message: types.Message): # функция отвечающая за команду: start
    user_id = message.from_user.id # Получаем id пользователя

    if user_id not in pets:
        new_pet = {
            "name": "Baks😜",
            "hunger": 50, # параметр голод
            "energy": 50, # параметр энергия
            "happiness": 50 # параметр счастья

        }
        pets[user_id] = new_pet # Если новый пользователь ещё не заходил мы создаём ему нового питомца

    await message.answer(
        f"Привет, {message.from_user.first_name}!\n" # Обращаемся к пользователю по имени
        f"Познакомься со своим питомцем: {pets[user_id]["name"]}!\n"
        f"Позаботься о нём!",
        reply_markup=main_kb
    )

@dp.message(F.text == "🎉Покормить") # Перехватываем те сообщения которые содержат текст
async def feed_pet(message: types.Message):
    user_id = message.from_user.id
    if user_id not in pets:
        await message.answer("Сначала запусти бота с помощью команды /start")
        return
    pet = pets[user_id]
    pet["hunger"] = min(pet["hunger"] + 10, 100) # Функция минимума
    pet["energy"] = max(pet["energy"] - 5, 0)
    await message.answer(f"{pet['name']} вкусно покушал!")

@dp.message(F.text == "🎈Поиграть") # Перехватываем те сообщения которые содержат текст
async def play_pet(message: types.Message):
    user_id = message.from_user.id
    if user_id not in pets:
        await message.answer("Сначала запусти бота с помощью команды /start")
        return
    pet = pets[user_id]
    pet["happiness"] = min(pet["happiness"] + 10, 100) # Функция минимума
    pet["energy"] = max(pet["energy"] - 15, 0)
    await message.answer(f"{pet['name']} Весело поиграл!")


def progress_bar(value: int, length: int):
    filled = int(value/100 * 10)
    return "🟩" * filled + "⬛" * (length - filled)

@dp.message(F.text == "🛠Статус") # Перехватываем те сообщения которые содержат текст
async def status_pet(message: types.Message):
    user_id = message.from_user.id
    if user_id not in pets:
        await message.answer("Сначала запусти бота с помощью команды /start")
        return
    pet = pets[user_id]
    hun = pet['hunger']
    en = pet['energy']
    hap = pet['happiness']

    status = (
        f"Статус вашего питомца {pet['name']}:\n"
        f"Сытость: {hun}% {progress_bar(hun, 10)}\n"
        f"Энергия: {en}% {progress_bar(en, 10)}\n"
        f"Счастье: {hap}% {progress_bar(hap, 10)}"
    )
    await message.answer(status)

async def main():
    print("Бот запущен...")
    await dp.start_polling(bot)
   

if __name__== "__main__":
    asyncio.run(main())