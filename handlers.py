from db import pets

from aiogram import Dispatcher, types, F
from aiogram.filters import Command

from keyboards import main_kb, food_kb, BTN_EXIT, BTN_FEED, BTN_PLAY, BTN_SLEEP, BTN_STATUS


def progress_bar(value: int, length: int):
    filled = int(value/100 * 10)
    return "🟩" * filled + "⬛" * (length - filled)


async def register_handlers(dp: Dispatcher): #картотека которая отслеживает все наши действия с телеграмма
    dp.message.register(start_handler, Command("start"))
    dp.message.register(play_pet,F.text == BTN_PLAY)
    dp.message.register(feed_pet, F.text == BTN_FEED)
    dp.message.register(status_pet, F.text == BTN_STATUS)
    

# Здесь лежат все наши функции отвечающие за перехват всех функций - диспетчер(перехватчик событий)

async def start_handler(message: types.Message): # функция отвечающая за команду: start
    user_id = message.from_user.id # Получаем id пользователя

# Бот - питомцы
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


async def feed_pet(message: types.Message):
    user_id = message.from_user.id
    if user_id not in pets:
        await message.answer("Сначала запусти бота с помощью команды /start")
        return
    pet = pets[user_id]
    await message.answer(f"Чем вы хотите покрмить {pet['name']}?", reply_markup=food_kb)

    
    # pet["hunger"] = min(pet["hunger"] + 10, 100) # Функция минимума
    # pet["energy"] = max(pet["energy"] - 5, 0)
    # await message.answer(f"{pet['name']} вкусно покушал!")


async def play_pet(message: types.Message):
    user_id = message.from_user.id
    if user_id not in pets:
        await message.answer("Сначала запусти бота с помощью команды /start")
        return
    pet = pets[user_id]
    pet["happiness"] = min(pet["happiness"] + 10, 100) # Функция минимума
    pet["energy"] = max(pet["energy"] - 15, 0)
    await message.answer(f"{pet['name']} Весело поиграл!")




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