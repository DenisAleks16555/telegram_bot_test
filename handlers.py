from aiogram import Router, F
from aiogram.types import Message
from keyboards import main_keyboard, back_keyboard, feed_keyboard, games_keyboard
from db import init_pet, get_pet, update_pet

router = Router()

@router.message(F.text == "/start")
async def start_handler(message: Message):
    user_id = message.from_user.id
    await init_pet(user_id)
    await message.reply("Привет! Ты получил виртуального питомца. Выбери действие:", reply_markup=main_keyboard)

@router.message(F.text == "📊 Статус")
async def status_handler(message: Message):
    user_id = message.from_user.id
    pet = await get_pet(user_id)
    if pet:
        text = f"Статус питомца:\nГолод: {pet['hunger']}\nЭнергия: {pet['energy']}\nЗдоровье: {pet['health']}"
    else:
        text = "Питомец не найден."
    await message.reply(text, reply_markup=back_keyboard)

@router.message(F.text == "🍗 Кормить")
async def feed_handler(message: Message):
    await message.reply("Выбери еду:", reply_markup=feed_keyboard())

@router.message(F.text == "🍗 Курица")
async def chicken_handler(message: Message):
    user_id = message.from_user.id
    pet = await get_pet(user_id)
    if pet:
        new_hunger = min(pet['hunger'] + 20, 100)
        await update_pet(user_id, hunger=new_hunger)
        await message.reply(f"Ты покормил курицей! Голод: {new_hunger}", reply_markup=main_keyboard)
    else:
        await message.reply("Питомец не найден.", reply_markup=main_keyboard)

@router.message(F.text == "🥩 Мясо")
async def meat_handler(message: Message):
    user_id = message.from_user.id
    pet = await get_pet(user_id)
    if pet:
        new_hunger = min(pet['hunger'] + 30, 100)
        await update_pet(user_id, hunger=new_hunger)
        await message.reply(f"Ты покормил мясом! Голод: {new_hunger}", reply_markup=main_keyboard)
    else:
        await message.reply("Питомец не найден.", reply_markup=main_keyboard)

@router.message(F.text == "💧 Вода")
async def water_handler(message: Message):
    user_id = message.from_user.id
    pet = await get_pet(user_id)
    if pet:
        new_hunger = min(pet['hunger'] + 10, 100)
        await update_pet(user_id, hunger=new_hunger)
        await message.reply(f"Ты напоил водой! Голод: {new_hunger}", reply_markup=main_keyboard)
    else:
        await message.reply("Питомец не найден.", reply_markup=main_keyboard)

@router.message(F.text == "🎮 Играть")
async def games_handler(message: Message):
    await message.reply("Выбери игру:", reply_markup=games_keyboard())

@router.message(F.text == "🎾 Теннис")
async def tennis_handler(message: Message):
    user_id = message.from_user.id
    pet = await get_pet(user_id)
    if pet:
        new_energy = max(pet['energy'] - 10, 0)
        await update_pet(user_id, energy=new_energy)
        await message.reply(f"Ты поиграл в теннис! Энергия: {new_energy}", reply_markup=main_keyboard)
    else:
        await message.reply("Питомец не найден.", reply_markup=main_keyboard)

@router.message(F.text == "🧸 Пазлы")
async def puzzles_handler(message: Message):
    user_id = message.from_user.id
    pet = await get_pet(user_id)
    if pet:
        new_energy = max(pet['energy'] - 5, 0)
        await update_pet(user_id, energy=new_energy)
        await message.reply(f"Ты поиграл в пазлы! Энергия: {new_energy}", reply_markup=main_keyboard)
    else:
        await message.reply("Питомец не найден.", reply_markup=main_keyboard)

@router.message(F.text == "🎯 Цель")
async def target_handler(message: Message):
    user_id = message.from_user.id
    pet = await get_pet(user_id)
    if pet:
        new_energy = max(pet['energy'] - 15, 0)
        await update_pet(user_id, energy=new_energy)
        await message.reply(f"Ты поиграл в цель! Энергия: {new_energy}", reply_markup=main_keyboard)
    else:
        await message.reply("Питомец не найден.", reply_markup=main_keyboard)

@router.message(F.text == "😴 Уложить спать")
async def sleep_handler(message: Message):
    user_id = message.from_user.id
    pet = await get_pet(user_id)
    if pet:
        new_energy = min(pet['energy'] + 50, 100)
        await update_pet(user_id, energy=new_energy)
        await message.reply(f"Питомец поспал! Энергия: {new_energy}", reply_markup=main_keyboard)
    else:
        await message.reply("Питомец не найден.", reply_markup=main_keyboard)

@router.message(F.text == "💊 Лечить")
async def heal_handler(message: Message):
    user_id = message.from_user.id
    pet = await get_pet(user_id)
    if pet:
        new_health = min(pet['health'] + 40, 100)
        await update_pet(user_id, health=new_health)
        await message.reply(f"Питомец вылечился! Здоровье: {new_health}", reply_markup=main_keyboard)
    else:
        await message.reply("Питомец не найден.", reply_markup=main_keyboard)

@router.message(F.text == "↩️ Назад")
async def back_handler(message: Message):
    await message.reply("Возвращаемся в главное меню:", reply_markup=main_keyboard)

# ВРЕМЕННО: Добавь это для диагностики (бот будет эхом повторять все сообщения). Если кнопки работают — удали.
@router.message()
async def echo_handler(message: Message):
    await message.reply(f"Получено сообщение: '{message.text}'. Нет подходящего хендлера.")













# from aiogram import Router, F
# from aiogram.types import Message
# from keyboards import main_keyboard, back_keyboard, feed_keyboard, games_keyboard
# from db import init_pet, get_pet, update_pet

# router = Router()

# @router.message(F.text == "/start")
# async def start_handler(message: Message):
#     user_id = message.from_user.id
#     await init_pet(user_id)
#     await message.reply("Привет! Ты получил виртуального питомца. Выбери действие:", reply_markup=main_keyboard)

# @router.message(F.text == "📊 Статус")
# async def status_handler(message: Message):
#     user_id = message.from_user.id
#     pet = await get_pet(user_id)
#     if pet:
#         text = f"Статус питомца:\nГолод: {pet['hunger']}\nЭнергия: {pet['energy']}\nЗдоровье: {pet['health']}"
#     else:
#         text = "Питомец не найден."
#     await message.reply(text, reply_markup=back_keyboard)

# @router.message(F.text == "🍗 Кормить")
# async def feed_handler(message: Message):
#     await message.reply("Выбери еду:", reply_markup=feed_keyboard)

# @router.message(F.text == "🍗 Курица")
# async def chicken_handler(message: Message):
#     user_id = message.from_user.id
#     pet = await get_pet(user_id)
#     if pet:
#         new_hunger = min(pet['hunger'] + 20, 100)
#         await update_pet(user_id, hunger=new_hunger)
#         await message.reply(f"Ты покормил курицей! Голод: {new_hunger}", reply_markup=main_keyboard)

# @router.message(F.text == "🥩 Мясо")
# async def meat_handler(message: Message):
#     user_id = message.from_user.id
#     pet = await get_pet(user_id)
#     if pet:
#         new_hunger = min(pet['hunger'] + 30, 100)
#         await update_pet(user_id, hunger=new_hunger)
#         await message.reply(f"Ты покормил мясом! Голод: {new_hunger}", reply_markup=main_keyboard)

# @router.message(F.text == "💧 Вода")
# async def water_handler(message: Message):
#     user_id = message.from_user.id
#     pet = await get_pet(user_id)
#     if pet:
#         new_hunger = min(pet['hunger'] + 10, 100)
#         await update_pet(user_id, hunger=new_hunger)
#         await message.reply(f"Ты напоил водой! Голод: {new_hunger}", reply_markup=main_keyboard)

# @router.message(F.text == "💧 Напоить")
# async def drink_handler(message: Message):
#     user_id = message.from_user.id
#     pet = await get_pet(user_id)
#     if pet:
#         new_hunger = min(pet['hunger'] + 15, 100)
#         await update_pet(user_id, hunger=new_hunger)
#         await message.reply(f"Ты напоил водой! Голод: {new_hunger}", reply_markup=main_keyboard)

# @router.message(F.text == "🎮 Играть")
# async def games_handler(message: Message):
#     await message.reply("Выбери игру:", reply_markup=games_keyboard)

# @router.message(F.text == "🎾 Теннис")
# async def tennis_handler(message: Message):
#     user_id = message.from_user.id
#     pet = await get_pet(user_id)
#     if pet:
#         new_energy = max(pet['energy'] - 10, 0)
#         await update_pet(user_id, energy=new_energy)
#         await message.reply(f"Ты поиграл в теннис! Энергия: {new_energy}", reply_markup=main_keyboard)

# @router.message(F.text == "🧸 Пазлы")
# async def puzzles_handler(message: Message):
#     user_id = message.from_user.id
#     pet = await get_pet(user_id)
#     if pet:
#         new_energy = max(pet['energy'] - 5, 0)
#         await update_pet(user_id, energy=new_energy)
#         await message.reply(f"Ты поиграл в пазлы! Энергия: {new_energy}", reply_markup=main_keyboard)

# @router.message(F.text == "🎯 Цель")
# async def target_handler(message: Message):
#     user_id = message.from_user.id
#     pet = await get_pet(user_id)
#     if pet:
#         new_energy = max(pet['energy'] - 15, 0)
#         await update_pet(user_id, energy=new_energy)
#         await message.reply(f"Ты поиграл в цель! Энергия: {new_energy}", reply_markup=main_keyboard)

# @router.message(F.text == "😴 Уложить спать")
# async def sleep_handler(message: Message):
#     user_id = message.from_user.id
#     pet = await get_pet(user_id)
#     if pet:
#         new_energy = min(pet['energy'] + 50, 100)
#         await update_pet(user_id, energy=new_energy)
#         await message.reply(f"Питомец поспал! Энергия: {new_energy}", reply_markup=main_keyboard)

# @router.message(F.text == "💊 Лечить")
# async def heal_handler(message: Message):
#     user_id = message.from_user.id
#     pet = await get_pet(user_id)
#     if pet:
#         new_health = min(pet['health'] + 40, 100)
#         await update_pet(user_id, health=new_health)
#         await message.reply(f"Питомец вылечился! Здоровье: {new_health}", reply_markup=main_keyboard)

# @router.message(F.text == "↩️ Назад")
# async def back_handler(message: Message):
#     await message.reply("Возвращаемся в главное меню:", reply_markup=main_keyboard)




























# from aiogram import Router, F
# from aiogram.types import Message, CallbackQuery
# from aiogram.utils.keyboard import InlineKeyboardBuilder
# from keyboards import main_keyboard, back_keyboard, feed_keyboard, sleep_keyboard, heal_keyboard, games_keyboard
# from db import init_pet, get_pet, update_pet

# router = Router()

# @router.message(F.text == "/start")
# async def start_handler(message: Message):
#     user_id = message.from_user.id
#     await init_pet(user_id)
#     await message.reply("Привет! Ты получил виртуального питомца. Выбери действие:", reply_markup=main_keyboard)

# @router.callback_query(F.data == "status")
# async def status_callback(callback: CallbackQuery):
#     user_id = callback.from_user.id
#     pet = await get_pet(user_id)
#     if pet:
#         text = f"Статус питомца:\nГолод: {pet['hunger']}\nЭнергия: {pet['energy']}\nЗдоровье: {pet['health']}"
#     else:
#         text = "Питомец не найден."
#     await callback.message.edit_text(text, reply_markup=back_keyboard)

# @router.callback_query(F.data == "feed")
# async def feed_callback(callback: CallbackQuery):
#     await callback.message.edit_text("Выбери еду:", reply_markup=feed_keyboard)

# @router.callback_query(F.data == "chicken")
# async def chicken_callback(callback: CallbackQuery):
#     user_id = callback.from_user.id
#     pet = await get_pet(user_id)
#     if pet:
#         new_hunger = min(pet['hunger'] + 20, 100)
#         await update_pet(user_id, hunger=new_hunger)
#         await callback.message.edit_text(f"Ты покормил курицей! Голод: {new_hunger}", reply_markup=back_keyboard)

# @router.callback_query(F.data == "meat")
# async def meat_callback(callback: CallbackQuery):
#     user_id = callback.from_user.id
#     pet = await get_pet(user_id)
#     if pet:
#         new_hunger = min(pet['hunger'] + 30, 100)
#         await update_pet(user_id, hunger=new_hunger)
#         await callback.message.edit_text(f"Ты покормил мясом! Голод: {new_hunger}", reply_markup=back_keyboard)

# @router.callback_query(F.data == "water")
# async def water_callback(callback: CallbackQuery):
#     user_id = callback.from_user.id
#     pet = await get_pet(user_id)
#     if pet:
#         new_hunger = min(pet['hunger'] + 10, 100)
#         await update_pet(user_id, hunger=new_hunger)
#         await callback.message.edit_text(f"Ты напоил водой! Голод: {new_hunger}", reply_markup=back_keyboard)

# @router.callback_query(F.data == "sleep")
# async def sleep_callback(callback: CallbackQuery):
#     user_id = callback.from_user.id
#     pet = await get_pet(user_id)
#     if pet:
#         new_energy = min(pet['energy'] + 50, 100)
#         await update_pet(user_id, energy=new_energy)
#         await callback.message.edit_text(f"Питомец поспал! Энергия: {new_energy}", reply_markup=back_keyboard)

# @router.callback_query(F.data == "heal")
# async def heal_callback(callback: CallbackQuery):
#     user_id = callback.from_user.id
#     pet = await get_pet(user_id)
#     if pet:
#         new_health = min(pet['health'] + 40, 100)
#         await update_pet(user_id, health=new_health)
#         await callback.message.edit_text(f"Питомец вылечился! Здоровье: {new_health}", reply_markup=back_keyboard)

# @router.callback_query(F.data == "games")
# async def games_callback(callback: CallbackQuery):
#     await callback.message.edit_text("Выбери игру:", reply_markup=games_keyboard)

# @router.callback_query(F.data == "tennis")
# async def tennis_callback(callback: CallbackQuery):
#     user_id = callback.from_user.id
#     pet = await get_pet(user_id)
#     if pet:
#         new_energy = max(pet['energy'] - 10, 0)
#         new_hunger = max(pet['hunger'] - 5, 0)
#         new_health = min(pet['health'] + 5, 100)
#         await update_pet(user_id, energy=new_energy, hunger=new_hunger, health=new_health)
#         await callback.message.edit_text(f"Игра в теннис завершена! Энергия: {new_energy}, Голод: {new_hunger}, Здоровье: {new_health}", reply_markup=back_keyboard)

# @router.callback_query(F.data == "puzzles")
# async def puzzles_callback(callback: CallbackQuery):
#     user_id = callback.from_user.id
#     pet = await get_pet(user_id)
#     if pet:
#         new_energy = max(pet['energy'] - 10, 0)
#         new_hunger = max(pet['hunger'] - 5, 0)
#         new_health = min(pet['health'] + 5, 100)
#         await update_pet(user_id, energy=new_energy, hunger=new_hunger, health=new_health)
#         await callback.message.edit_text(f"Решение пазлов завершено! Энергия: {new_energy}, Голод: {new_hunger}, Здоровье: {new_health}", reply_markup=back_keyboard)

# @router.callback_query(F.data == "goal")
# async def goal_callback(callback: CallbackQuery):
#     user_id = callback.from_user.id
#     pet = await get_pet(user_id)
#     if pet:
#         new_energy = max(pet['energy'] - 10, 0)
#         new_hunger = max(pet['hunger'] - 5, 0)
#         new_health = min(pet['health'] + 5, 100)
#         await update_pet(user_id, energy=new_energy, hunger=new_hunger, health=new_health)
#         await callback.message.edit_text(f"Игра в цель завершена! Энергия: {new_energy}, Голод: {new_hunger}, Здоровье: {new_health}", reply_markup=back_keyboard)

# @router.callback_query(F.data == "back")
# async def back_callback(callback: CallbackQuery):
#     await callback.message.edit_text("Выбери действие:", reply_markup=main_keyboard)



























# import asyncio
# import logging
# from aiogram import F, Router
# from aiogram.types import Message, CallbackQuery
# from aiogram.filters import Command
# from keyboards import main_keyboard, game_keyboard
# from db import init_pet, get_pet, update_pet  # Теперь из БД

# router = Router()
# logging.basicConfig(level=logging.INFO)

# @router.message(Command("start"))
# async def start_handler(message: Message):
#     user_id = message.from_user.id
#     await init_pet(user_id)  # Инициализируем в БД
#     await message.answer("Привет! Это твой виртуальный питомец. Выбери действие:", reply_markup=main_keyboard)

# @router.message(F.text == "Статус")
# async def status_handler(message: Message):
#     user_id = message.from_user.id
#     data = await get_pet(user_id)  # Читаем из БД
#     if not data:
#         await message.reply("Сначала запусти /start!", reply_markup=main_keyboard)
#         return
#     hunger = data['hunger']
#     energy = data['energy']
#     health = data['health']
#     await message.reply(
#         f"Статус: Голод {hunger}, Энергия {energy}, Здоровье {health}\n\n"
#         f"Игр сыграно: {data['games_played']}\n"
#         f"- Теннис: {data['tennis_games']}\n"
#         f"- Пазлы: {data['puzzle_games']}\n"
#         f"- Цель: {data['target_games']}\n\n"
#         f"Кормлений: Курица {data['actions_chicken']}, Мясо {data['actions_meat']}, Вода {data['actions_water']}\n"
#         f"Сон: {data['actions_sleep']}, Лечение: {data['actions_heal']}", 
#         reply_markup=main_keyboard
#     )

# # Обработчики кормления (теперь с БД)
# @router.message(F.text == "🍗 Курица")
# async def chicken_handler(message: Message):
#     user_id = message.from_user.id
#     data = await get_pet(user_id)
#     if not data:
#         await message.reply("Сначала /start!", reply_markup=main_keyboard)
#         return
#     data['hunger'] = min(100, data['hunger'] + 20)
#     data['actions_chicken'] += 1  # Старое 'actions']['chicken' теперь колонка
#     await update_pet(user_id, data)  # Сохраняем в БД
#     await message.reply("Питомец поел курицу! 😋", reply_markup=main_keyboard)

# @router.message(F.text == "🥩 Мясо")
# async def meat_handler(message: Message):
#     user_id = message.from_user.id
#     data = await get_pet(user_id)
#     if not data:
#         await message.reply("Сначала /start!", reply_markup=main_keyboard)
#         return
#     data['hunger'] = min(100, data['hunger'] + 30)
#     data['actions_meat'] += 1
#     await update_pet(user_id, data)
#     await message.reply("Питомец поел мясо! 🥩", reply_markup=main_keyboard)

# @router.message(F.text == "💧 Вода")
# async def water_handler(message: Message):
#     user_id = message.from_user.id
#     data = await get_pet(user_id)
#     if not data:
#         await message.reply("Сначала /start!", reply_markup=main_keyboard)
#         return
#     data['hunger'] = min(100, data['hunger'] + 10)
#     data['actions_water'] += 1
#     await update_pet(user_id, data)
#     await message.reply("Питомец попил воды! 💧", reply_markup=main_keyboard)

# @router.message(F.text == "😴 Сон")
# async def sleep_handler(message: Message):
#     user_id = message.from_user.id
#     data = await get_pet(user_id)
#     if not data:
#         await message.reply("Сначала /start!", reply_markup=main_keyboard)
#         return
#     data['energy'] = min(100, data['energy'] + 50)
#     data['health'] = min(100, data['health'] + 10)
#     data['actions_sleep'] += 1
#     await update_pet(user_id, data)
#     await message.reply("Питомец поспал! 😴", reply_markup=main_keyboard)

# @router.message(F.text == "🩹 Лечение")
# async def heal_handler(message: Message):
#     user_id = message.from_user.id
#     data = await get_pet(user_id)
#     if not data:
#         await message.reply("Сначала /start!", reply_markup=main_keyboard)
#         return
#     data['health'] = min(100, data['health'] + 40)
#     data['actions_heal'] += 1
#     await update_pet(user_id, data)
#     await message.reply("Питомец вылечился! 🩹", reply_markup=main_keyboard)

# @router.message(F.text == "Играть")
# async def play_handler(message: Message):
#     await message.reply("Выбери игру для питомца:", reply_markup=game_keyboard)

# # Обработчики для Inline-кнопок игр (с БД)
# @router.callback_query(F.data == "tennis")
# async def tennis_handler(callback: CallbackQuery):
#     user_id = callback.from_user.id
#     data = await get_pet(user_id)
#     if not data:
#         await callback.answer("Сначала /start!")
#         return
#     data['games_played'] += 1
#     data['tennis_games'] += 1
#     data['energy'] = max(0, data['energy'] - 10)
#     data['hunger'] = max(0, data['hunger'] - 5)
#     data['health'] = min(100, data['health'] + 5)
#     await update_pet(user_id, data)
#     await callback.answer()
#     await callback.message.answer("Питомец поиграл в теннис! 🎾", reply_markup=main_keyboard)

# @router.callback_query(F.data == "puzzle")
# async def puzzle_handler(callback: CallbackQuery):
#     user_id = callback.from_user.id
#     data = await get_pet(user_id)
#     if not data:
#         await callback.answer("Сначала /start!")
#         return
#     data['games_played'] += 1
#     data['puzzle_games'] += 1
#     data['energy'] = max(0, data['energy'] - 10)
#     data['hunger'] = max(0, data['hunger'] - 5)
#     data['health'] = min(100, data['health'] + 5)
#     await update_pet(user_id, data)
#     await callback.answer()
#     await callback.message.answer("Питомец собрал пазл! 🧩", reply_markup=main_keyboard)

# @router.callback_query(F.data == "target")
# async def target_handler(callback: CallbackQuery):
#     user_id = callback.from_user.id
#     data = await get_pet(user_id)
#     if not data:
#         await callback.answer("Сначала /start!")
#         return
#     data['games_played'] += 1
#     data['target_games'] += 1
#     data['energy'] = max(0, data['energy'] - 10)
#     data['hunger'] = max(0, data['hunger'] - 5)
#     data['health'] = min(100, data['health'] + 5)
#     await update_pet(user_id, data)
#     await callback.answer()
#     await callback.message.answer("Питомец попал в цель! 🎯", reply_markup=main_keyboard)

# # Обработчик для кнопки "Назад"
# @router.callback_query(F.data == "back")
# async def back_handler(callback: CallbackQuery):
#     await callback.answer("Вернулись в главное меню")
#     await callback.message.answer("Главное меню:", reply_markup=main_keyboard)






# import asyncio
# import logging
# from aiogram import F, Router
# from aiogram.types import Message, CallbackQuery
# from aiogram.filters import Command
# from keyboards import main_keyboard, game_keyboard
# from db import init_pet, pets

# router = Router()
# logging.basicConfig(level=logging.INFO)

# @router.message(Command("start"))
# async def start_handler(message: Message):
#     user_id = message.from_user.id
#     init_pet(user_id)
#     await message.answer("Привет! Это твой виртуальный питомец. Выбери действие:", reply_markup=main_keyboard)

# @router.message(F.text == "Статус")
# async def status_handler(message: Message):
#     user_id = message.from_user.id
#     data = pets[user_id]
#     hunger = data['hunger']
#     energy = data['energy']
#     health = data['health']
#     await message.reply(
#         f"Статус: Голод {hunger}, Энергия {energy}, Здоровье {health}\n\n"
#         f"Игр сыграно: {data['games_played']}\n"
#         f"- Теннис: {data['tennis_games']}\n"
#         f"- Пазлы: {data['puzzle_games']}\n"
#         f"- Цель: {data['target_games']}", 
#         reply_markup=main_keyboard
#     )

# # Обработчики кормления, воды, сна, лечения (без изменений)
# @router.message(F.text == "🍗 Курица")
# async def chicken_handler(message: Message):
#     user_id = message.from_user.id
#     data = pets[user_id]
#     data['hunger'] = min(100, data['hunger'] + 20)
#     data['actions']['chicken'] += 1
#     await message.reply("Питомец поел курицу! 😋", reply_markup=main_keyboard)

# @router.message(F.text == "🥩 Мясо")
# async def meat_handler(message: Message):
#     user_id = message.from_user.id
#     data = pets[user_id]
#     data['hunger'] = min(100, data['hunger'] + 30)
#     data['actions']['meat'] += 1
#     await message.reply("Питомец поел мясо! 🥩", reply_markup=main_keyboard)

# @router.message(F.text == "💧 Вода")
# async def water_handler(message: Message):
#     user_id = message.from_user.id
#     data = pets[user_id]
#     data['hunger'] = min(100, data['hunger'] + 10)  # Вода слегка утоляет голод
#     data['actions']['water'] += 1
#     await message.reply("Питомец попил воды! 💧", reply_markup=main_keyboard)

# @router.message(F.text == "😴 Сон")
# async def sleep_handler(message: Message):
#     user_id = message.from_user.id
#     data = pets[user_id]
#     data['energy'] = min(100, data['energy'] + 50)
#     data['health'] = min(100, data['health'] + 10)
#     data['actions']['sleep'] += 1
#     await message.reply("Питомец поспал! 😴", reply_markup=main_keyboard)

# @router.message(F.text == "🩹 Лечение")
# async def heal_handler(message: Message):
#     user_id = message.from_user.id
#     data = pets[user_id]
#     data['health'] = min(100, data['health'] + 40)
#     data['actions']['heal'] += 1
#     await message.reply("Питомец вылечился! 🩹", reply_markup=main_keyboard)

# @router.message(F.text == "Играть")
# async def play_handler(message: Message):
#     await message.reply("Выбери игру для питомца:", reply_markup=game_keyboard)

# # Обработчики для Inline-кнопок игр (CallbackQuery)
# @router.callback_query(F.data == "tennis")
# async def tennis_handler(callback: CallbackQuery):
#     user_id = callback.from_user.id
#     data = pets[user_id]
#     data['games_played'] += 1
#     data['tennis_games'] += 1
#     data['energy'] = max(0, data['energy'] - 10)  # Тратит энергию
#     data['hunger'] = max(0, data['hunger'] - 5)   # Немного голода
#     data['health'] = min(100, data['health'] + 5) # Развлечение лечит
#     await callback.answer()  # Закрывает индикатор загрузки
#     await callback.message.answer("Питомец поиграл в теннис! 🎾", reply_markup=main_keyboard)

# @router.callback_query(F.data == "puzzle")
# async def puzzle_handler(callback: CallbackQuery):
#     user_id = callback.from_user.id
#     data = pets[user_id]
#     data['games_played'] += 1
#     data['puzzle_games'] += 1
#     data['energy'] = max(0, data['energy'] - 10)
#     data['hunger'] = max(0, data['hunger'] - 5)
#     data['health'] = min(100, data['health'] + 5)
#     await callback.answer()
#     await callback.message.answer("Питомец собрал пазл! 🧩", reply_markup=main_keyboard)

# @router.callback_query(F.data == "target")
# async def target_handler(callback: CallbackQuery):
#     user_id = callback.from_user.id
#     data = pets[user_id]
#     data['games_played'] += 1
#     data['target_games'] += 1
#     data['energy'] = max(0, data['energy'] - 10)
#     data['hunger'] = max(0, data['hunger'] - 5)
#     data['health'] = min(100, data['health'] + 5)
#     await callback.answer()
#     await callback.message.answer("Питомец попал в цель! 🎯", reply_markup=main_keyboard)

# # Обработчик для кнопки "Назад" (Inline)
# @router.callback_query(F.data == "back")
# async def back_handler(callback: CallbackQuery):
#     await callback.answer("Вернулись в главное меню")
#     await callback.message.answer("Главное меню:", reply_markup=main_keyboard)






# import asyncio
# import logging
# from aiogram import F, Router
# from aiogram.types import Message, CallbackQuery
# from aiogram.filters import Command
# from keyboards import main_keyboard, game_keyboard
# from db import init_pet, pets

# router = Router()
# logging.basicConfig(level=logging.INFO)

# @router.message(Command("start"))
# async def start_handler(message: Message):
#     user_id = message.from_user.id
#     init_pet(user_id)
#     await message.answer("Привет! Это твой виртуальный питомец. Выбери действие:", reply_markup=main_keyboard)

# @router.message(F.text == "Статус")
# async def status_handler(message: Message):
#     user_id = message.from_user.id
#     data = pets[user_id]
#     hunger = data['hunger']
#     energy = data['energy']
#     health = data['health']
#     await message.reply(
#         f"Статус: Голод {hunger}, Энергия {energy}, Здоровье {health}\n\n"
#         f"Игр сыграно: {data['games_played']}\n"
#         f"- Теннис: {data['tennis_games']}\n"
#         f"- Пазлы: {data['puzzle_games']}\n"
#         f"- Цель: {data['target_games']}", 
#         reply_markup=main_keyboard
#     )

# # Обработчики кормления, воды, сна, лечения (без изменений)
# @router.message(F.text == "🍗 Курица")
# async def chicken_handler(message: Message):
#     user_id = message.from_user.id
#     data = pets[user_id]
#     data['hunger'] = min(100, data['hunger'] + 20)
#     data['actions']['chicken'] += 1
#     await message.reply("Питомец поел курицу! 😋", reply_markup=main_keyboard)

# @router.message(F.text == "🥩 Мясо")
# async def meat_handler(message: Message):
#     user_id = message.from_user.id
#     data = pets[user_id]
#     data['hunger'] = min(100, data['hunger'] + 30)
#     data['actions']['meat'] += 1
#     await message.reply("Питомец поел мясо! 🥩", reply_markup=main_keyboard)

# @router.message(F.text == "💧 Вода")
# async def water_handler(message: Message):
#     user_id = message.from_user.id
#     data = pets[user_id]
#     data['hunger'] = min(100, data['hunger'] + 10)  # Вода слегка утоляет голод
#     data['actions']['water'] += 1
#     await message.reply("Питомец попил воды! 💧", reply_markup=main_keyboard)

# @router.message(F.text == "😴 Сон")
# async def sleep_handler(message: Message):
#     user_id = message.from_user.id
#     data = pets[user_id]
#     data['energy'] = min(100, data['energy'] + 50)
#     data['health'] = min(100, data['health'] + 10)
#     data['actions']['sleep'] += 1
#     await message.reply("Питомец поспал! 😴", reply_markup=main_keyboard)

# @router.message(F.text == "🩹 Лечение")
# async def heal_handler(message: Message):
#     user_id = message.from_user.id
#     data = pets[user_id]
#     data['health'] = min(100, data['health'] + 40)
#     data['actions']['heal'] += 1
#     await message.reply("Питомец вылечился! 🩹", reply_markup=main_keyboard)

# @router.message(F.text == "Играть")
# async def play_handler(message: Message):
#     await message.reply("Выбери игру для питомца:", reply_markup=game_keyboard)

# # Обработчики для Inline-кнопок игр (CallbackQuery)
# @router.callback_query(F.data == "tennis")
# async def tennis_handler(callback: CallbackQuery):
#     user_id = callback.from_user.id
#     data = pets[user_id]
#     data['games_played'] += 1
#     data['tennis_games'] += 1
#     data['energy'] = max(0, data['energy'] - 10)  # Тратит энергию
#     data['hunger'] = max(0, data['hunger'] - 5)   # Немного голода
#     data['health'] = min(100, data['health'] + 5) # Развлечение лечит
#     # await callback.message.edit_text("Питомец поиграл в теннис! 🎾\nВернемся в меню.", reply_markup=main_keyboard)
#     await callback.answer()  # Закрывает индикатор загрузки
#     await callback.message.answer("Питомец поиграл в теннис! 🎾", reply_markup=main_keyboard)

# @router.callback_query(F.data == "puzzle")
# async def puzzle_handler(callback: CallbackQuery):
#     user_id = callback.from_user.id
#     data = pets[user_id]
#     data['games_played'] += 1
#     data['puzzle_games'] += 1
#     data['energy'] = max(0, data['energy'] - 10)
#     data['hunger'] = max(0, data['hunger'] - 5)
#     data['health'] = min(100, data['health'] + 5)
#     # await callback.message.edit_text("Питомец собрал пазл! 🧩\nВернемся в меню.", reply_markup=main_keyboard)
#     await callback.answer()
#     await callback.message.answer("Питомец собрал пазл! 🧩", reply_markup=main_keyboard)

# @router.callback_query(F.data == "target")
# async def target_handler(callback: CallbackQuery):
#     user_id = callback.from_user.id
#     data = pets[user_id]
#     data['games_played'] += 1
#     data['target_games'] += 1
#     data['energy'] = max(0, data['energy'] - 10)
#     data['hunger'] = max(0, data['hunger'] - 5)
#     data['health'] = min(100, data['health'] + 5)
#     # await callback.message.edit_text("Питомец попал в цель! 🎯\nВернемся в меню.", reply_markup=main_keyboard)
#     await callback.answer()
#     await callback.message.answer("Питомец попал в цель! 🎯", reply_markup=main_keyboard)

# # Обработчик для кнопки "Назад" (Inline)
# @router.callback_query(F.data == "back")
# async def back_handler(callback: CallbackQuery):
#     # await callback.message.edit_reply_markup(main_keyboard)
#     await callback.answer("Вернулись в главное меню")
#     await callback.message.answer("Главное меню:", reply_markup=main_keyboard)







# from aiogram import Router, F
# from aiogram.types import Message
# from keyboards import main_keyboard, feed_keyboard, game_keyboard  # Добавили game_keyboard
# from db import pets, init_pet

# router = Router()

# @router.message(F.text == "/start")
# async def start_handler(message: Message):
#     user_id = message.from_user.id
#     init_pet(user_id)
#     await message.reply("Привет! Я твой виртуальный питомец. Выбери действие:", reply_markup=main_keyboard)

# @router.message(F.text == "Статус")
# async def status_handler(message: Message):
#     user_id = message.from_user.id
#     init_pet(user_id)
#     data = pets[user_id]
#     hunger = data['hunger']
#     energy = data['energy']
#     health = data['health']
#     await message.reply(f"Статус: Голод {hunger}, Энергия {energy}, Здоровье {health}\n\nИгр сыграно: {data['games_played']}\n- Теннис: {data['tennis_games']}\n- Пазлы: {data['puzzle_games']}\n- Цель: {data['target_games']}", reply_markup=main_keyboard)

    

# @router.message(F.text == "Кормить")
# async def feed_handler(message: Message):
#     await message.reply("Выбери еду:", reply_markup=feed_keyboard)

# @router.message(F.text == "Курица")
# async def chicken_handler(message: Message):
#     user_id = message.from_user.id
#     init_pet(user_id)
#     data = pets[user_id]
#     data['hunger'] = min(100, data['hunger'] + 20)
#     data['actions']['chicken'] += 1  # Увеличиваем счётчик
#     await message.reply("Ты покормил питомца курицей! Голод увеличен.", reply_markup=main_keyboard)

# @router.message(F.text == "Мясо")
# async def meat_handler(message: Message):
#     user_id = message.from_user.id
#     init_pet(user_id)
#     data = pets[user_id]
#     data['hunger'] = min(100, data['hunger'] + 30)
#     data['actions']['meat'] += 1  # Увеличиваем счётчик
#     await message.reply("Ты покормил питомца мясом! Голод увеличен.", reply_markup=main_keyboard)

# @router.message(F.text == "Вода")
# async def water_handler(message: Message):
#     user_id = message.from_user.id
#     init_pet(user_id)
#     data = pets[user_id]
#     data['hunger'] = min(100, data['hunger'] + 10)
#     data['actions']['water'] += 1  # Увеличиваем счётчик
#     await message.reply("Ты напоил питомца водой! Голод увеличен.", reply_markup=main_keyboard)

# @router.message(F.text == "Сон")
# async def sleep_handler(message: Message):
#     user_id = message.from_user.id
#     init_pet(user_id)
#     data = pets[user_id]
#     data['energy'] = min(100, data['energy'] + 50)
#     data['actions']['sleep'] += 1  # Увеличиваем счётчик
#     await message.reply("Питомец поспал! Энергия восстановлена.", reply_markup=main_keyboard)

# @router.message(F.text == "Лечение")
# async def heal_handler(message: Message):
#     user_id = message.from_user.id
#     init_pet(user_id)
#     data = pets[user_id]
#     data['health'] = min(100, data['health'] + 40)
#     data['actions']['heal'] += 1  # Увеличиваем счётчик
#     await message.reply("Питомец вылечился! Здоровье восстановлено.", reply_markup=main_keyboard)

# @router.message(F.text == "Top")
# async def top_handler(message: Message):
#     user_id = message.from_user.id
#     init_pet(user_id)
#     actions = pets[user_id]['actions']
#     top_text = f"Топ действий:\nКурица - {actions['chicken']} раз\nМясо - {actions['meat']} раза\nВода - {actions['water']} раза\nСон - {actions['sleep']} раза\nЛечение - {actions['heal']} раза"
#     await message.reply(top_text, reply_markup=main_keyboard)


# @router.message(F.text == "Играть")
# async def play_handler(message: Message):
#     await message.reply("Выберите игру с питомцем:", reply_markup=game_keyboard)

# @router.message(F.text == "Назад")
# async def back_handler(message: Message):
#     await message.reply("Выбери действие:", reply_markup=main_keyboard)


# # Обработчик для игры в теннис (🎾)
# @router.message(F.text == '🎾 Теннис')
# async def play_tennis(message: Message):
#     user_id = message.from_user.id
#     init_pet(user_id)  # Инициализируем, если нужно
#     data = pets[user_id]
    
#     # Игра: повышаем энергию, чуть уменьшаем голод
#     data['energy'] = min(100, data['energy'] + 20)
#     data['hunger'] = max(0, data['hunger'] - 5)
#     data['games_played'] += 1
#     data['tennis_games'] += 1
    
#     await message.reply(f"Вы поиграли в теннис! Энергия +20, голод -5.\nВсего игр: {data['games_played']}", reply_markup=game_keyboard)

# # Обработчик для игры в пазлы (🧩)
# @router.message(F.text == '🧩 Пазлы')
# async def play_puzzle(message: Message):
#     user_id = message.from_user.id
#     init_pet(user_id)
#     data = pets[user_id]
    
#     # Игра: повышаем здоровье, чуть уменьшаем энергию
#     data['health'] = min(100, data['health'] + 15)
#     data['energy'] = max(0, data['energy'] - 5)
#     data['games_played'] += 1
#     data['puzzle_games'] += 1
    
#     await message.reply(f"Вы собрали пазл! Здоровье +15, энергия -5.\nВсего игр: {data['games_played']}", reply_markup=game_keyboard)

# # Обработчик для игры в цель (🎯)
# @router.message(F.text == '🎯 Цель')
# async def play_target(message: Message):
#     user_id = message.from_user.id
#     init_pet(user_id)
#     data = pets[user_id]
    
#     # Игра: повышаем голод (как будто еда в награду), чуть уменьшаем здоровье
#     data['hunger'] = min(100, data['hunger'] + 10)
#     data['health'] = max(0, data['health'] - 5)
#     data['games_played'] += 1
#     data['target_games'] += 1
    
#     await message.reply(f"Вы попали в цель! Голод +10, здоровье -5.\nВсего игр: {data['games_played']}", reply_markup=game_keyboard)

# # Обработчик для кнопки "Назад" в меню игр (совместим с твоим "Назад")
# @router.message(F.text == 'Назад')
# async def back_from_games(message: Message):
#     user_id = message.from_user.id
#     init_pet(user_id)
    
#     await message.reply("Возвращаемся в главное меню!", reply_markup=main_keyboard)




# from aiogram import F, Router
# from aiogram.types import Message
# from keyboards import food_kb, main_kb
# from db import pets
# from config import FOOD_PARAMS as fpar

# router = Router()

# @router.message(F.text == "/start")
# async def start_handler(message: Message):
#     user_id = message.from_user.id
#     if user_id not in pets:
#         pets[user_id] = {'hunger': 50, 'energy': 50, 'happiness': 50, 'health': 50}  # Начальные stats
#     await message.reply("Привет! Твой виртуальный питомец готов. Выбери действие:", reply_markup=main_kb)
#     print(f"start_handler triggered by user {user_id}")

# @router.message(F.text == "🍽 Покормить")
# async def show_food_menu(message: Message):
#     user_id = message.from_user.id
#     if user_id not in pets:
#         await message.reply("Сначала запусти /start!")
#         return
#     await message.reply("Выбери еду для питомца:", reply_markup=food_kb)
#     print(f"show_food_menu triggered by user {user_id}")

# @router.message(F.text == "🥩 Стейк")
# async def feed_steak(message: Message):
#     user_id = message.from_user.id
#     if user_id in pets:
#         pets[user_id]['hunger'] = min(100, pets[user_id]['hunger'] + fpar['стейк']['hunger'])
#         pets[user_id]['energy'] = min(100, pets[user_id]['energy'] + fpar['стейк']['energy'])
#         await message.reply("Питомец съел стейк! Голод и энергия восстановлены.", reply_markup=food_kb)
#     print(f"feed_steak triggered by user {user_id}")

# @router.message(F.text == "🥩 Мясо")
# async def feed_meat(message: Message):
#     user_id = message.from_user.id
#     if user_id in pets:
#         pets[user_id]['hunger'] = min(100, pets[user_id]['hunger'] + fpar['мясо']['hunger'])
#         pets[user_id]['energy'] = min(100, pets[user_id]['energy'] + fpar['мясо']['energy'])
#         await message.reply("Питомец съел мясо! Голод и энергия восстановлены.", reply_markup=food_kb)
#     print(f"feed_meat triggered by user {user_id}")

# @router.message(F.text == "💧 Вода")
# async def feed_water(message: Message):
#     user_id = message.from_user.id
#     if user_id in pets:
#         pets[user_id]['hunger'] = min(100, pets[user_id]['hunger'] + fpar['вода']['hunger'])
#         pets[user_id]['health'] = min(100, pets[user_id]['health'] + fpar['вода']['health'])
#         await message.reply("Питомец попил воды! Голод и здоровье восстановлены.", reply_markup=food_kb)
#     print(f"feed_water triggered by user {user_id}")

# @router.message(F.text == "⬅️ Назад")
# async def back_to_main(message: Message):
#     await message.reply("Возвращаемся в главное меню:", reply_markup=main_kb)
#     print(f"back_to_main triggered by user {message.from_user.id}")

# @router.message(F.text == "😴 Уложить спать")
# async def sleep_pet(message: Message):
#     user_id = message.from_user.id
#     if user_id in pets:
#         pets[user_id]['energy'] = min(100, pets[user_id]['energy'] + 30)
#         pets[user_id]['happiness'] = min(100, pets[user_id]['happiness'] + 10)
#         await message.reply("Питомец поспал! Энергия и счастье восстановлены.", reply_markup=main_kb)
#     print(f"sleep_pet triggered by user {user_id}")

# @router.message(F.text == "❤️ Подлечить")
# async def heal_pet(message: Message):
#     user_id = message.from_user.id
#     if user_id in pets:
#         pets[user_id]['health'] = min(100, pets[user_id]['health'] + 25)
#         await message.reply("Питомец подлечился! Здоровье восстановлено.", reply_markup=main_kb)
#     print(f"heal_pet triggered by user {user_id}")

# @router.message(F.text == "📊 Статус")
# async def status_pet(message: Message):
#     user_id = message.from_user.id
#     if user_id in pets:
#         pet = pets[user_id]
#         status = f"🍽 Голод: {pet['hunger']}%\n⚡ Энергия: {pet['energy']}%\n😊 Счастье: {pet['happiness']}%\n❤️ Здоровье: {pet['health']}%"
#         await message.reply(f"Статус питомца:\n{status}", reply_markup=main_kb)
#     else:
#         await message.reply("Питомец не найден. Запусти /start.", reply_markup=main_kb)
#     print(f"status_pet triggered by user {user_id}")




















































































# from aiogram import types, Dispatcher
# from keyboards import food_kb, main_kb
# from db import pets
# from config import FOOD_PARAMS as fpar

# def register_handlers(dp: Dispatcher):
#     # Хэндлер /start
#     @dp.message_handler(commands=['start'])
#     async def start_handler(message: types.Message):
#         user_id = message.from_user.id
#         if user_id not in pets:
#             pets[user_id] = {'hunger': 50, 'energy': 50, 'happiness': 50, 'health': 50}  # Начальные stats
#         await message.reply("Привет! Твой виртуальный питомец готов. Выбери действие:", reply_markup=main_kb)
#         print(f"start_handler triggered by user {user_id}")

#     # Хэндлер "🍽 Покормить" — показывает меню еды
#     @dp.message_handler(text="🍽 Покормить")
#     async def show_food_menu(message: types.Message):
#         user_id = message.from_user.id
#         if user_id not in pets:
#             await message.reply("Сначала запусти /start!")
#             return
#         await message.reply("Выбери еду для питомца:", reply_markup=food_kb)
#         print(f"show_food_menu triggered by user {user_id}")

#     # Хэндлеры для конкретной еды
#     @dp.message_handler(text="🍗 Курица")
#     async def feed_chicken(message: types.Message):
#         user_id = message.from_user.id
#         if user_id in pets:
#             pets[user_id]['hunger'] = min(100, pets[user_id]['hunger'] + fpar['курица']['hunger'])
#             pets[user_id]['energy'] = min(100, pets[user_id]['energy'] + fpar['курица'].get('energy', 0))
#             await message.reply("Питомец съел курицу! Голод и энергия восстановлены.", reply_markup=food_kb)
#         print(f"feed_chicken triggered by user {user_id}")

#     @dp.message_handler(text="🥩 Стейк")
#     async def feed_steak(message: types.Message):
#         user_id = message.from_user.id
#         if user_id in pets:
#             pets[user_id]['hunger'] = min(100, pets[user_id]['hunger'] + fpar['стейк']['hunger'])
#             pets[user_id]['energy'] = min(100, pets[user_id]['energy'] + fpar['стейк'].get('energy', 0))
#             await message.reply("Питомец съел стейк! Голод и энергия восстановлены.", reply_markup=food_kb)
#         print(f"feed_steak triggered by user {user_id}")

#     @dp.message_handler(text="🍎 Яблоко")
#     async def feed_apple(message: types.Message):
#         user_id = message.from_user.id
#         if user_id in pets:
#             pets[user_id]['hunger'] = min(100, pets[user_id]['hunger'] + fpar['яблоко']['hunger'])
#             pets[user_id]['happiness'] = min(100, pets[user_id]['happiness'] + fpar['яблоко'].get('happiness', 0))
#             await message.reply("Питомец съел яблоко! Голод и счастье восстановлены.", reply_markup=food_kb)
#         print(f"feed_apple triggered by user {user_id}")

#     @dp.message_handler(text="🥩 Мясо")
#     async def feed_meat(message: types.Message):
#         user_id = message.from_user.id
#         if user_id in pets:
#             pets[user_id]['hunger'] = min(100, pets[user_id]['hunger'] + fpar['мясо']['hunger'])
#             pets[user_id]['energy'] = min(100, pets[user_id]['energy'] + fpar['мясо'].get('energy', 0))
#             await message.reply("Питомец съел мясо! Голод и энергия восстановлены.", reply_markup=food_kb)
#         print(f"feed_meat triggered by user {user_id}")

#     @dp.message_handler(text="🍞 Хлеб")
#     async def feed_bread(message: types.Message):
#         user_id = message.from_user.id
#         if user_id in pets:
#             pets[user_id]['hunger'] = min(100, pets[user_id]['hunger'] + fpar['хлеб']['hunger'])
#             await message.reply("Питомец съел хлеб! Голод восстановлен.", reply_markup=food_kb)
#         print(f"feed_bread triggered by user {user_id}")

#     @dp.message_handler(text="🍪 Печенье")
#     async def feed_cookie(message: types.Message):
#         user_id = message.from_user.id
#         if user_id in pets:
#             pets[user_id]['hunger'] = min(100, pets[user_id]['hunger'] + fpar['печенье']['hunger'])
#             pets[user_id]['happiness'] = min(100, pets[user_id]['happiness'] + fpar['печенье'].get('happiness', 0))
#             await message.reply("Питомец съел печенье! Голод и счастье восстановлены.", reply_markup=food_kb)
#         print(f"feed_cookie triggered by user {user_id}")

#     @dp.message_handler(text="💧 Вода")
#     async def feed_water(message: types.Message):
#         user_id = message.from_user.id
#         if user_id in pets:
#             pets[user_id]['hunger'] = min(100, pets[user_id]['hunger'] + fpar['вода']['hunger'])
#             pets[user_id]['health'] = min(100, pets[user_id]['health'] + fpar['вода'].get('health', 0))
#             await message.reply("Питомец попил воды! Голод и здоровье восстановлены.", reply_markup=food_kb)
#         print(f"feed_water triggered by user {user_id}")

#     # Кнопка "⬅️ Назад" — возвращает в главное меню
#     @dp.message_handler(text="⬅️ Назад")
#     async def back_to_main(message: types.Message):
#         await message.reply("Возвращаемся в главное меню:", reply_markup=main_kb)
#         print(f"back_to_main triggered by user {message.from_user.id}")

#     # Хэндлер "😴 Уложить спать"
#     @dp.message_handler(text="😴 Уложить спать")
#     async def sleep_pet(message: types.Message):
#         user_id = message.from_user.id
#         if user_id in pets:
#             pets[user_id]['energy'] = min(100, pets[user_id]['energy'] + 30)
#             pets[user_id]['happiness'] = min(100, pets[user_id]['happiness'] + 10)
#             await message.reply("Питомец поспал! Энергия и счастье восстановлены.", reply_markup=main_kb)
#         print(f"sleep_pet triggered by user {user_id}")

#     # Хэндлер "❤️ Подлечить"
#     @dp.message_handler(text="❤️ Подлечить")
#     async def heal_pet(message: types.Message):
#         user_id = message.from_user.id
#         if user_id in pets:
#             pets[user_id]['health'] = min(100, pets[user_id]['health'] + 25)
#             await message.reply("Питомец подлечился! Здоровье восстановлено.", reply_markup=main_kb)
#         print(f"heal_pet triggered by user {user_id}")

#     # Хэндлер "📊 Статус"
#     @dp.message_handler(text="📊 Статус")
#     async def status_pet(message: types.Message):
#         user_id = message.from_user.id
#         if user_id in pets:
#             pet = pets[user_id]
#             status = f"🍽 Голод: {pet['hunger']}%\n⚡ Энергия: {pet['energy']}%\n😊 Счастье: {pet['happiness']}%\n❤️ Здоровье: {pet['health']}%"
#             await message.reply(f"Статус питомца:\n{status}", reply_markup=main_kb)
#         else:
#             await message.reply("Питомец не найден. Запусти /start.", reply_markup=main_kb)
#         print(f"status_pet triggered by user {user_id}")




# from aiogram import types
# from keyboards import food_kb, main_kb
# from db import pets
# from config import FOOD_PARAMS as fpar, DECREASE_PARAMS  # Импортируем FOOD_PARAMS и другие константы
# from main import dp  # Импортируем dp из main.py (убедись, что в main.py dp = Dispatcher(bot))

# # Хэндлер /start
# @dp.message_handler(commands=['start'])
# async def start_handler(message: types.Message):
#     user_id = message.from_user.id
#     if user_id not in pets:
#         pets[user_id] = {'hunger': 50, 'energy': 50, 'happiness': 50, 'health': 50}  # Начальные stats
#     await message.reply("Привет! Твой виртуальный питомец готов. Выбери действие:", reply_markup=main_kb)
#     print(f"start_handler triggered by user {user_id}")

# # Хэндлер "🍽 Покормить" — показывает меню еды
# @dp.message_handler(text="🍽 Покормить")
# async def show_food_menu(message: types.Message):
#     user_id = message.from_user.id
#     if user_id not in pets:
#         await message.reply("Сначала запусти /start!")
#         return
#     await message.reply("Выбери еду для питомца:", reply_markup=food_kb)
#     print(f"show_food_menu triggered by user {user_id}")

# # Хэндлеры для конкретной еды (увеличивают голод и энергию из config, возвращают в меню еды)
# @dp.message_handler(text="🍗 Курица")
# async def feed_chicken(message: types.Message):
#     user_id = message.from_user.id
#     if user_id in pets:
#         pets[user_id]['hunger'] = min(100, pets[user_id]['hunger'] + fpar['курица']['hunger'])  # +20 голод
#         pets[user_id]['energy'] = min(100, pets[user_id]['energy'] + fpar['курица'].get('energy', 0))  # +5 энергия (если есть)
#         await message.reply("Питомец съел курицу! Голод и энергия восстановлены.", reply_markup=food_kb)
#     print(f"feed_chicken triggered by user {user_id}")

# @dp.message_handler(text="🥩 Стейк")
# async def feed_steak(message: types.Message):
#     user_id = message.from_user.id
#     if user_id in pets:
#         pets[user_id]['hunger'] = min(100, pets[user_id]['hunger'] + fpar['стейк']['hunger'])
#         pets[user_id]['energy'] = min(100, pets[user_id]['energy'] + fpar['стейк'].get('energy', 0))
#         await message.reply("Питомец съел стейк! Голод и энергия восстановлены.", reply_markup=food_kb)
#     print(f"feed_steak triggered by user {user_id}")

# @dp.message_handler(text="🍎 Яблоко")
# async def feed_apple(message: types.Message):
#     user_id = message.from_user.id
#     if user_id in pets:
#         pets[user_id]['hunger'] = min(100, pets[user_id]['hunger'] + fpar['яблоко']['hunger'])
#         pets[user_id]['happiness'] = min(100, pets[user_id]['happiness'] + fpar['яблоко'].get('happiness', 0))  # +10 счастье
#         await message.reply("Питомец съел яблоко! Голод и счастье восстановлены.", reply_markup=food_kb)
#     print(f"feed_apple triggered by user {user_id}")

# @dp.message_handler(text="🥩 Мясо")
# async def feed_meat(message: types.Message):
#     user_id = message.from_user.id
#     if user_id in pets:
#         pets[user_id]['hunger'] = min(100, pets[user_id]['hunger'] + fpar['мясо']['hunger'])
#         pets[user_id]['energy'] = min(100, pets[user_id]['energy'] + fpar['мясо'].get('energy', 0))
#         await message.reply("Питомец съел мясо! Голод и энергия восстановлены.", reply_markup=food_kb)
#     print(f"feed_meat triggered by user {user_id}")

# @dp.message_handler(text="🍞 Хлеб")
# async def feed_bread(message: types.Message):
#     user_id = message.from_user.id
#     if user_id in pets:
#         pets[user_id]['hunger'] = min(100, pets[user_id]['hunger'] + fpar['хлеб']['hunger'])
#         await message.reply("Питомец съел хлеб! Голод восстановлен.", reply_markup=food_kb)
#     print(f"feed_bread triggered by user {user_id}")

# @dp.message_handler(text="🍪 Печенье")
# async def feed_cookie(message: types.Message):
#     user_id = message.from_user.id
#     if user_id in pets:
#         pets[user_id]['hunger'] = min(100, pets[user_id]['hunger'] + fpar['печенье']['hunger'])
#         pets[user_id]['happiness'] = min(100, pets[user_id]['happiness'] + fpar['печенье'].get('happiness', 0))
#         await message.reply("Питомец съел печенье! Голод и счастье восстановлены.", reply_markup=food_kb)
#     print(f"feed_cookie triggered by user {user_id}")

# @dp.message_handler(text="💧 Вода")
# async def feed_water(message: types.Message):
#     user_id = message.from_user.id
#     if user_id in pets:
#         pets[user_id]['hunger'] = min(100, pets[user_id]['hunger'] + fpar['вода']['hunger'])
#         pets[user_id]['health'] = min(100, pets[user_id]['health'] + fpar['вода'].get('health', 0))  # +5 здоровье
#         await message.reply("Питомец попил воды! Голод и здоровье восстановлены.", reply_markup=food_kb)
#     print(f"feed_water triggered by user {user_id}")

# # Кнопка "⬅️ Назад" — возвращает в главное меню
# @dp.message_handler(text="⬅️ Назад")
# async def back_to_main(message: types.Message):
#     await message.reply("Возвращаемся в главное меню:", reply_markup=main_kb)
#     print(f"back_to_main triggered by user {message.from_user.id}")

# # Хэндлер "😴 Уложить спать"
# @dp.message_handler(text="😴 Уложить спать")
# async def sleep_pet(message: types.Message):
#     user_id = message.from_user.id
#     if user_id in pets:
#         pets[user_id]['energy'] = min(100, pets[user_id]['energy'] + 30)  # +30 энергия
#         pets[user_id]['happiness'] = min(100, pets[user_id]['happiness'] + 10)  # +10 счастье
#         await message.reply("Питомец поспал! Энергия и счастье восстановлены.", reply_markup=main_kb)
#     print(f"sleep_pet triggered by user {user_id}")

# # Хэндлер "❤️ Подлечить"
# @dp.message_handler(text="❤️ Подлечить")
# async def heal_pet(message: types.Message):
#     user_id = message.from_user.id
#     if user_id in pets:
#         pets[user_id]['health'] = min(100, pets[user_id]['health'] + 25)  # +25 здоровье
#         await message.reply("Питомец подлечился! Здоровье восстановлено.", reply_markup=main_kb)
#     print(f"heal_pet triggered by user {user_id}")

# # Хэндлер "📊 Статус"
# @dp.message_handler(text="📊 Статус")
# async def status_pet(message: types.Message):
#     user_id = message.from_user.id
#     if user_id in pets:
#         pet = pets[user_id]
#         status = f"🍽 Голод: {pet['hunger']}%\n⚡ Энергия: {pet['energy']}%\n😊 Счастье: {pet['happiness']}%\n❤️ Здоровье: {pet['health']}%"
#         await message.reply(f"Статус питомца:\n{status}", reply_markup=main_kb)
#     else:
#         await message.reply("Питомец не найден. Запусти /start.", reply_markup=main_kb)
#     print(f"status_pet triggered by user {user_id}")




# from aiogram import types
# from keyboards import food_kb, main_kb
# from db import pets
# from config import FOOD_PARAMS as fpar  # Предполагаем, что в config.py есть FOOD_PARAMS = {'курица': {'hunger': 20, 'energy': 5}, ...} — добавь, если нет

# # Хэндлер /start
# @dp.message_handler(commands=['start'])
# async def start_handler(message: types.Message):
#     user_id = message.from_user.id
#     if user_id not in pets:
#         pets[user_id] = {'hunger': 50, 'energy': 50, 'happiness': 50, 'health': 50}  # Начальные stats
#     await message.reply("Привет! Твой виртуальный питомец готов. Выбери действие:", reply_markup=main_kb)
#     print(f"start_handler triggered by user {user_id}")

# # Хэндлер "🍽 Покормить" — показывает меню еды
# @dp.message_handler(text="🍽 Покормить")
# async def show_food_menu(message: types.Message):
#     user_id = message.from_user.id
#     if user_id not in pets:
#         await message.reply("Сначала запусти /start!")
#         return
#     await message.reply("Выбери еду для питомца:", reply_markup=food_kb)
#     print(f"show_food_menu triggered by user {user_id}")

# # Хэндлеры для конкретной еды (увеличивают голод и энергию из config, возвращают в меню еды)
# @dp.message_handler(text="🍗 Курица")
# async def feed_chicken(message: types.Message):
#     user_id = message.from_user.id
#     if user_id in pets:
#         pets[user_id]['hunger'] = min(100, pets[user_id]['hunger'] + fpar['курица']['hunger'])  # +20 голод
#         pets[user_id]['energy'] = min(100, pets[user_id]['energy'] + fpar['курица']['energy'])  # +5 энергия (если есть в config)
#         await message.reply("Питомец съел курицу! Голод и энергия восстановлены.", reply_markup=food_kb)
#     print(f"feed_chicken triggered by user {user_id}")

# @dp.message_handler(text="🥩 Стейк")
# async def feed_steak(message: types.Message):
#     user_id = message.from_user.id
#     if user_id in pets:
#         pets[user_id]['hunger'] = min(100, pets[user_id]['hunger'] + fpar['стейк']['hunger'])
#         pets[user_id]['energy'] = min(100, pets[user_id]['energy'] + fpar['стейк']['energy'])
#         await message.reply("Питомец съел стейк! Голод и энергия восстановлены.", reply_markup=food_kb)
#     print(f"feed_steak triggered by user {user_id}")

# @dp.message_handler(text="🍎 Яблоко")
# async def feed_apple(message: types.Message):
#     user_id = message.from_user.id
#     if user_id in pets:
#         pets[user_id]['hunger'] = min(100, pets[user_id]['hunger'] + fpar['яблоко']['hunger'])
#         pets[user_id]['happiness'] = min(100, pets[user_id]['happiness'] + fpar['яблоко']['happiness'])  # +10 счастье
#         await message.reply("Питомец съел яблоко! Голод и счастье восстановлены.", reply_markup=food_kb)
#     print(f"feed_apple triggered by user {user_id}")

# @dp.message_handler(text="🥩 Мясо")
# async def feed_meat(message: types.Message):
#     user_id = message.from_user.id
#     if user_id in pets:
#         pets[user_id]['hunger'] = min(100, pets[user_id]['hunger'] + fpar['мясо']['hunger'])
#         pets[user_id]['energy'] = min(100, pets[user_id]['energy'] + fpar['мясо']['energy'])
#         await message.reply("Питомец съел мясо! Голод и энергия восстановлены.", reply_markup=food_kb)
#     print(f"feed_meat triggered by user {user_id}")

# @dp.message_handler(text="🍞 Хлеб")
# async def feed_bread(message: types.Message):
#     user_id = message.from_user.id
#     if user_id in pets:
#         pets[user_id]['hunger'] = min(100, pets[user_id]['hunger'] + fpar['хлеб']['hunger'])
#         await message.reply("Питомец съел хлеб! Голод восстановлен.", reply_markup=food_kb)
#     print(f"feed_bread triggered by user {user_id}")

# @dp.message_handler(text="🍪 Печенье")
# async def feed_cookie(message: types.Message):
#     user_id = message.from_user.id
#     if user_id in pets:
#         pets[user_id]['hunger'] = min(100, pets[user_id]['hunger'] + fpar['печенье']['hunger'])
#         pets[user_id]['happiness'] = min(100, pets[user_id]['happiness'] + fpar['печенье']['happiness'])
#         await message.reply("Питомец съел печенье! Голод и счастье восстановлены.", reply_markup=food_kb)
#     print(f"feed_cookie triggered by user {user_id}")

# @dp.message_handler(text="💧 Вода")
# async def feed_water(message: types.Message):
#     user_id = message.from_user.id
#     if user_id in pets:
#         pets[user_id]['hunger'] = min(100, pets[user_id]['hunger'] + fpar['вода']['hunger'])
#         pets[user_id]['health'] = min(100, pets[user_id]['health'] + fpar['вода']['health'])  # +5 здоровье
#         await message.reply("Питомец попил воды! Голод и здоровье восстановлены.", reply_markup=food_kb)
#     print(f"feed_water triggered by user {user_id}")

# # Кнопка "⬅️ Назад" — возвращает в главное меню
# @dp.message_handler(text="⬅️ Назад")
# async def back_to_main(message: types.Message):
#     await message.reply("Возвращаемся в главное меню:", reply_markup=main_kb)
#     print(f"back_to_main triggered by user {message.from_user.id}")

# # Хэндлер "😴 Уложить спать"
# @dp.message_handler(text="😴 Уложить спать")
# async def sleep_pet(message: types.Message):
#     user_id = message.from_user.id
#     if user_id in pets:
#         pets[user_id]['energy'] = min(100, pets[user_id]['energy'] + 30)  # +30 энергия
#         pets[user_id]['happiness'] = min(100, pets[user_id]['happiness'] + 10)  # +10 счастье
#         await message.reply("Питомец поспал! Энергия и счастье восстановлены.", reply_markup=main_kb)
#     print(f"sleep_pet triggered by user {user_id}")

# # Хэндлер "❤️ Подлечить"
# @dp.message_handler(text="❤️ Подлечить")
# async def heal_pet(message: types.Message):
#     user_id = message.from_user.id
#     if user_id in pets:
#         pets[user_id]['health'] = min(100, pets[user_id]['health'] + 25)  # +25 здоровье
#         await message.reply("Питомец подлечился! Здоровье восстановлено.", reply_markup=main_kb)
#     print(f"heal_pet triggered by user {user_id}")

# # Хэндлер "📊 Статус"
# @dp.message_handler(text="📊 Статус")
# async def status_pet(message: types.Message):
#     user_id = message.from_user.id
#     if user_id in pets:
#         pet = pets[user_id]
#         status = f"🍽 Голод: {pet['hunger']}%\n⚡ Энергия: {pet['energy']}%\n😊 Счастье: {pet['happiness']}%\n❤️ Здоровье: {pet['health']}%"
#         await message.reply(f"Статус питомца:\n{status}", reply_markup=main_kb)
#     else:
#         await message.reply("Питомец не найден. Запусти /start.", reply_markup=main_kb)
#     print(f"status_pet triggered by user {user_id}")













# from db import pets
# from aiogram import Dispatcher, types, F
# from aiogram.filters import Command
# from keyboards import main_kb, food_kb, BTN_EXIT, BTN_TOP, BTN_FEED, BTN_PLAY, BTN_SLEEP, BTN_STATUS

# click_count = 0  # Счётчик кликов для кнопки "Top"

# def progress_bar(value: int, length: int):
#     filled = int(value/100 * 10)
#     return "🟩" * filled + "⬛" * (length - filled)

# async def start_handler(message: types.Message):  # функция отвечающая за команду: start
#     user_id = message.from_user.id  # Получаем id пользователя
#     print(f"start_handler triggered by user {user_id}")  # Отладка

#     # Бот - питомцы
#     if user_id not in pets:
#         new_pet = {
#             "name": "Baks😜",
#             "hunger": 50,  # параметр голод
#             "energy": 50,  # параметр энергия
#             "happiness": 50,  # параметр счастья
#             "health": 50  # НОВОЕ
#         }
#         pets[user_id] = new_pet  # Если новый пользователь ещё не заходил мы создаём ему нового питомца

#     await message.answer(
#         f"Привет, {message.from_user.first_name}!\n"  # Обращаемся к пользователю по имени
#         f"Познакомься со своим питомцем: {pets[user_id]['name']}!\n"  # Исправлено: одинарные кавычки для ключа
#         f"Позаботься о нём!",
#         reply_markup=main_kb
#     )

# async def about_handler(message: types.Message):
#     print(f"about_handler triggered by user {message.from_user.id}")  # Отладка
#     author_nick = "@Aleks16555den"  # Ваш ник
#     description = (
#         "Это мой питомец-бот! Здесь вы можете ухаживать за питомцем, кормить, играть и смотреть его статус.\n"
#         f"Создатель этого бота: {author_nick}\n"
#         "Для возврата в меню нажмите /start."  # Добавлено, чтобы не казалось пустым
#     )
#     await message.answer(description)

# async def feed_pet(message: types.Message):
#     user_id = message.from_user.id
#     print(f"feed_pet triggered by user {user_id}")  # Отладка
#     if user_id not in pets:
#         await message.answer("Сначала запусти бота с помощью команды /start")
#         return
#     pet = pets[user_id]
#     await message.answer(f"Чем вы хотите покормить {pet['name']}?", reply_markup=food_kb)


#     # Новые кнопки закомментированы (пока не добавляем)
#     # elif data == "apple":
#     #     pet['hunger'] = min(100, pet['hunger'] + 10)
#     #     await callback.answer(f"{pet['name']} съел яблоко! 🍎 Голод: {pet['hunger']}%")
#     # ... остальные новые
#    # ОБРАБОТЧИК ДЛЯ ВСЕХ INLINE-КНОПОК ЕДЫ (старые + новые)
# async def food_callback_handler(callback: types.CallbackQuery):
#     user_id = callback.from_user.id
#     pet = pets.get(user_id)
#     if not pet:
#         await callback.answer("У тебя нет питомца!")
#         return

#     data = callback.data
#     if data == "chicken":
#         pet['hunger'] = min(100, pet['hunger'] + 15)
#         await callback.answer(f"{pet['name']} съел курицу! 🍗 Голод: {pet['hunger']}%")
#     elif data == "steak":
#         pet['hunger'] = min(100, pet['hunger'] + 25)
#         pet['energy'] = min(100, pet['energy'] + 10)
#         await callback.answer(f"{pet['name']} съел стейк! 🥩 Голод: {pet['hunger']}%, ⚡ Энергия: {pet['energy']}%")
#     elif data == "water":
#         pet['hunger'] = min(100, pet['hunger'] + 5)
#         await callback.answer(f"{pet['name']} попил воды! 🚰 Голод: {pet['hunger']}%")
#     # Новые кнопки закомментированы (пока не добавляем)
#     # elif data == "apple":
#     #     pet['hunger'] = min(100, pet['hunger'] + 10)
#     #     await callback.answer(f"{pet['name']} съел яблоко! 🍎 Голод: {pet['hunger']}%")
#     # ... остальные новые
#     elif data == "back":
#         await callback.message.edit_text("Возвращаемся в главное меню.", reply_markup=main_kb)
#         return

#     # ИСПРАВЛЕНИЕ: Меняем текст, чтобы показать текущее состояние (избегаем "message is not modified")
#     new_text = f"Чем ещё хотите покормить {pet['name']}?\nТекущий голод: {pet['hunger']}%"  # Добавили текущий голод
#     await callback.message.edit_text(new_text, reply_markup=food_kb)  # Обновляем с новым текстом

    
#     data = callback.data
#     if data == "chicken":
#         pet['hunger'] = min(100, pet['hunger'] + 15)
#         await callback.answer(f"{pet['name']} съел курицу! 🍗 Голод: {pet['hunger']}%")
#     elif data == "steak":
#         pet['hunger'] = min(100, pet['hunger'] + 25)
#         pet['energy'] = min(100, pet['energy'] + 10)
#         await callback.answer(f"{pet['name']} съел стейк! 🥩 Голод: {pet['hunger']}%, ⚡ Энергия: {pet['energy']}%")
#     elif data == "water":
#         pet['hunger'] = min(100, pet['hunger'] + 5)
#         await callback.answer(f"{pet['name']} попил воды! 🚰 Голод: {pet['hunger']}%")
#     # elif data == "apple":
#     #     pet['hunger'] = min(100, pet['hunger'] + 10)
#     #     await callback.answer(f"{pet['name']} съел яблоко! 🍎 Голод: {pet['hunger']}%")
#     # elif data == "meat":
#     #     pet['hunger'] = min(100, pet['hunger'] + 20)
#     #     pet['energy'] = min(100, pet['energy'] + 5)
#     #     await callback.answer(f"{pet['name']} съел мясо! 🥩 Голод: {pet['hunger']}%, ⚡ Энергия: {pet['energy']}%")
#     # elif data == "bread":
#     #     pet['hunger'] = min(100, pet['hunger'] + 15)
#     #     await callback.answer(f"{pet['name']} съел хлеб! 🍞 Голод: {pet['hunger']}%")
#     # elif data == "cookie":
#     #     pet['hunger'] = min(100, pet['hunger'] + 5)
#         # pet['happiness'] = min(100, pet['happiness'] + 10)
#         # await callback.answer(f"{pet['name']} съел печенье! 🍪 Голод: {pet['hunger']}%, 😊 Счастье: {pet['happiness']}%")
#     elif data == "back":
#         await callback.message.edit_text("Возвращаемся в главное меню.", reply_markup=main_kb)
#         return

#     # Обновляем сообщение, чтобы меню осталось
#     await callback.message.edit_text(f"Чем ещё хотите покормить {pet['name']}?", reply_markup=food_kb)

# # Старый код (play_pet, status_pet и т.д. — оставляем как есть)
# async def play_pet(message: types.Message):
#     user_id = message.from_user.id
#     print(f"play_pet triggered by user {user_id}")  # Отладка
#     if user_id not in pets:
#         await message.answer("Сначала запусти бота с помощью команды /start")
#         return
#     pet = pets[user_id]
#     pet["happiness"] = min(pet["happiness"] + 10, 100)  # Функция минимума
#     pet["energy"] = max(pet["energy"] - 15, 0)
#     await message.answer(f"{pet['name']} Весело поиграл!")

# async def status_pet(message: types.Message):
#     user_id = message.from_user.id
#     print(f"status_pet triggered by user {user_id}")  # Отладка
#     if user_id not in pets:
#         await message.answer("Сначала запусти бота с помощью команды /start")
#         return
#     pet = pets[user_id]
#     hun = pet['hunger']
#     en = pet['energy']
#     hap = pet['happiness']

#     status = (
#         f"Статус вашего питомца {pet['name']}:\n"
#         f"Сытость: {hun}% {progress_bar(hun, 10)}\n"
#         f"Энергия: {en}% {progress_bar(en, 10)}\n"
#         f"Счастье: {hap}% {progress_bar(hap, 10)}\n"
#         f"Здоровье: {pet['health']}% {progress_bar(pet['health'], 10)}"  # НОВОЕ: добавил эту строку
#     )
#     await message.answer(status)

# async def sleep_pet(message: types.Message):
#     print("sleep_pet triggered by user", message.from_user.id)  # Это лог: добавь его, чтобы видеть в терминале, когда кнопка нажата
#     user_id = message.from_user.id
#     if user_id in pets:
#         pets[user_id]['energy'] = min(pets[user_id]['energy'] + 20, 100)  # Восстанавливаем энергию (не больше 100%)
#         await message.reply(f"Питомец поспал и восстановил энергию! Энергия: {pets[user_id]['energy']}%")
#     else:
#         await message.reply("У тебя нет питомца! Сначала нажми /start.")

# async def top_click(message: types.Message):
#     global click_count  # Используем глобальную переменную из main.py
#     click_count += 1  # Увеличиваем счётчик на 1
#     await message.answer(f"Ты нажал на Top {click_count} раз!", reply_markup=main_kb)

# # НОВЫЙ ОБРАБОТЧИК: добавь после top_click
# async def heal_pet(message: types.Message):
#     user_id = message.from_user.id
#     print(f"heal_pet triggered by user {user_id}")  # Отладка
#     if user_id not in pets:
#         await message.answer("Сначала запусти бота с помощью команды /start")
#         return
#     pet = pets[user_id]
#     if pet["energy"] >= 5:  # Проверяем, есть ли энергия для лечения
#         pet["health"] = min(100, pet["health"] + 10)  # Увеличиваем здоровье на 10, но не выше 100
#         pet["energy"] = max(0, pet["energy"] - 5)     # Уменьшаем энергию на 5, но не ниже 0
#         await message.answer(f"{pet['name']} подлечился! ❤️ Здоровье: {pet['health']}%, ⚡ Энергия: {pet['energy']}%")
#     else:
#         await message.answer(f"{pet['name']} слишком устал! Сначала отдохни или поиграй, чтобы восстановить энергию.")

# async def register_handlers(dp: Dispatcher):  # картотека которая отслеживает все наши действия с телеграмма
#     dp.message.register(start_handler, Command("start"))
#     dp.message.register(about_handler, Command("about"))  # Новая строка для /about
#     dp.message.register(play_pet, F.text == BTN_PLAY)
#     dp.message.register(feed_pet, F.text == BTN_FEED)
#     dp.message.register(status_pet, F.text == BTN_STATUS)
#     dp.message.register(sleep_pet, F.text == BTN_SLEEP)  # Новая строка для кнопки "Спать"
#     dp.message.register(top_click, F.text == BTN_TOP)  # Новая строка для кнопки "Top"
#     dp.message.register(heal_pet, F.text == "❤️ Подлечить")  # НОВОЕ: регистрация обработчика
#     # КЛЮЧЕВОЕ: регистрация для inline-кнопок еды (это было пропущено!)
#     dp.callback_query.register(food_callback_handler)








# from db import pets
# from aiogram import Dispatcher, types, F
# from aiogram.filters import Command
# from keyboards import main_kb, food_kb, BTN_EXIT, BTN_TOP, BTN_FEED, BTN_PLAY, BTN_SLEEP, BTN_STATUS

# click_count = 0  # Счётчик кликов для кнопки "Top"

# def progress_bar(value: int, length: int):
#     filled = int(value/100 * 10)
#     return "🟩" * filled + "⬛" * (length - filled)

# async def start_handler(message: types.Message):  # функция отвечающая за команду: start
#     user_id = message.from_user.id  # Получаем id пользователя
#     print(f"start_handler triggered by user {user_id}")  # Отладка

#     # Бот - питомцы
#     if user_id not in pets:
#         new_pet = {
#             "name": "Baks😜",
#             "hunger": 50,  # параметр голод
#             "energy": 50,  # параметр энергия
#             "happiness": 50,  # параметр счастья
#             "health": 50  # НОВОЕ
#         }
#         pets[user_id] = new_pet  # Если новый пользователь ещё не заходил мы создаём ему нового питомца

#     await message.answer(
#         f"Привет, {message.from_user.first_name}!\n"  # Обращаемся к пользователю по имени
#         f"Познакомься со своим питомцем: {pets[user_id]['name']}!\n"  # Исправлено: одинарные кавычки для ключа
#         f"Позаботься о нём!",
#         reply_markup=main_kb
#     )

# async def about_handler(message: types.Message):
#     print(f"about_handler triggered by user {message.from_user.id}")  # Отладка
#     author_nick = "@Aleks16555den"  # Ваш ник
#     description = (
#         "Это мой питомец-бот! Здесь вы можете ухаживать за питомцем, кормить, играть и смотреть его статус.\n"
#         f"Создатель этого бота: {author_nick}\n"
#         "Для возврата в меню нажмите /start."  # Добавлено, чтобы не казалось пустым
#     )
#     await message.answer(description)

# async def feed_pet(message: types.Message):
#     user_id = message.from_user.id
#     print(f"feed_pet triggered by user {user_id}")  # Отладка
#     if user_id not in pets:
#         await message.answer("Сначала запусти бота с помощью команды /start")
#         return
#     pet = pets[user_id]
#     await message.answer(f"Чем вы хотите покормить {pet['name']}?", reply_markup=food_kb)

# # НОВЫЙ ОБРАБОТЧИК: для всех inline-кнопок еды (старые + новые)
# async def food_callback_handler(callback: types.CallbackQuery):
#     user_id = callback.from_user.id
#     pet = pets.get(user_id)
#     if not pet:
#         await callback.answer("У тебя нет питомца!")
#         return

#     if callback.data == "chicken":
#         pet['hunger'] = min(100, pet['hunger'] + 15)
#         await callback.answer(f"{pet['name']} съел курицу! 🍗 Голод: {pet['hunger']}%")
#     elif callback.data == "steak":
#         pet['hunger'] = min(100, pet['hunger'] + 25)
#         pet['energy'] = min(100, pet['energy'] + 10)
#         await callback.answer(f"{pet['name']} съел стейк! 🥩 Голод: {pet['hunger']}%, ⚡ Энергия: {pet['energy']}%")
#     elif callback.data == "water":
#         pet['hunger'] = min(100, pet['hunger'] + 5)
#         await callback.answer(f"{pet['name']} попил воды! 🚰 Голод: {pet['hunger']}%")
#     elif callback.data == "apple":
#         pet['hunger'] = min(100, pet['hunger'] + 10)
#         await callback.answer(f"{pet['name']} съел яблоко! 🍎 Голод: {pet['hunger']}%")
#     elif callback.data == "meat":
#         pet['hunger'] = min(100, pet['hunger'] + 20)
#         pet['energy'] = min(100, pet['energy'] + 5)
#         await callback.answer(f"{pet['name']} съел мясо! 🥩 Голод: {pet['hunger']}%, ⚡ Энергия: {pet['energy']}%")
#     elif callback.data == "bread":
#         pet['hunger'] = min(100, pet['hunger'] + 15)
#         await callback.answer(f"{pet['name']} съел хлеб! 🍞 Голод: {pet['hunger']}%")
#     elif callback.data == "cookie":
#         pet['hunger'] = min(100, pet['hunger'] + 5)
#         pet['happiness'] = min(100, pet['happiness'] + 10)
#         await callback.answer(f"{pet['name']} съел печенье! 🍪 Голод: {pet['hunger']}%, 😊 Счастье: {pet['happiness']}%")
#     elif callback.data == "back":
#         await callback.message.edit_text("Возвращаемся в главное меню.", reply_markup=main_kb)
#         return

#     # После кормления обновляем сообщение с меню еды (чтобы кнопки остались)
#     await callback.message.edit_text(f"Чем ещё хотите покормить {pet['name']}?", reply_markup=food_kb)

# # Старый код
# async def play_pet(message: types.Message):
#     user_id = message.from_user.id
#     print(f"play_pet triggered by user {user_id}")  # Отладка
#     if user_id not in pets:
#         await message.answer("Сначала запусти бота с помощью команды /start")
#         return
#     pet = pets[user_id]
#     pet["happiness"] = min(pet["happiness"] + 10, 100)  # Функция минимума
#     pet["energy"] = max(pet["energy"] - 15, 0)
#     await message.answer(f"{pet['name']} Весело поиграл!")

# # Старый код
# async def status_pet(message: types.Message):
#     user_id = message.from_user.id
#     print(f"status_pet triggered by user {user_id}")  # Отладка
#     if user_id not in pets:
#         await message.answer("Сначала запусти бота с помощью команды /start")
#         return
#     pet = pets[user_id]
#     hun = pet['hunger']
#     en = pet['energy']
#     hap = pet['happiness']

#     status = (
#         f"Статус вашего питомца {pet['name']}:\n"
#         f"Сытость: {hun}% {progress_bar(hun, 10)}\n"
#         f"Энергия: {en}% {progress_bar(en, 10)}\n"
#         f"Счастье: {hap}% {progress_bar(hap, 10)}\n"
#         f"Здоровье: {pet['health']}% {progress_bar(pet['health'], 10)}"  # НОВОЕ: добавил эту строку
#     )
#     await message.answer(status)

# async def sleep_pet(message: types.Message):
#     print("sleep_pet triggered by user", message.from_user.id)  # Это лог: добавь его, чтобы видеть в терминале, когда кнопка нажата
#     user_id = message.from_user.id
#     if user_id in pets:
#         pets[user_id]['energy'] = min(pets[user_id]['energy'] + 20, 100)  # Восстанавливаем энергию (не больше 100%)
#         await message.reply(f"Питомец поспал и восстановил энергию! Энергия: {pets[user_id]['energy']}%")
#     else:
#         await message.reply("У тебя нет питомца! Сначала нажми /start.")

# async def top_click(message: types.Message):
#     global click_count  # Используем глобальную переменную из main.py
#     click_count += 1  # Увеличиваем счётчик на 1
#     await message.answer(f"Ты нажал на Top {click_count} раз!", reply_markup=main_kb)

# # НОВЫЙ ОБРАБОТЧИК: добавь после top_click
# async def heal_pet(message: types.Message):
#     user_id = message.from_user.id
#     print(f"heal_pet triggered by user {user_id}")  # Отладка
#     if user_id not in pets:
#         await message.answer("Сначала запусти бота с помощью команды /start")
#         return
#     pet = pets[user_id]
#     if pet["energy"] >= 5:  # Проверяем, есть ли энергия для лечения
#         pet["health"] = min(100, pet["health"] + 10)  # Увеличиваем здоровье на 10, но не выше 100
#         pet["energy"] = max(0, pet["energy"] - 5)     # Уменьшаем энергию на 5, но не ниже 0
#         await message.answer(f"{pet['name']} подлечился! ❤️ Здоровье: {pet['health']}%, ⚡ Энергия: {pet['energy']}%")
#     else:
#         await message.answer(f"{pet['name']} слишком устал! Сначала отдохни или поиграй, чтобы восстановить энергию.")

# async def register_handlers(dp: Dispatcher):  # картотека которая отслеживает все наши действия с телеграмма
#     dp.message.register(start_handler, Command("start"))
#     dp.message.register(about_handler, Command("about"))  # Новая строка для /about
#     dp.message.register(play_pet, F.text == BTN_PLAY)
#     dp.message.register(feed_pet, F.text == BTN_FEED)
#     dp.message.register(status_pet, F.text == BTN_STATUS)
#     dp.message.register(sleep_pet, F.text == BTN_SLEEP)  # Новая строка для кнопки "Спать"
#     dp.message.register(top_click, F.text == BTN_TOP)  # Новая строка для кнопки "Top"
#     dp.message.register(heal_pet, F.text == "❤️ Подлечить")  # НОВОЕ: регистрация обработчика
#     # НОВАЯ РЕГИСТРАЦИЯ: для inline-кнопок еды
#     dp.callback_query.register(food_callback_handler)




















# from db import pets
# from aiogram import Dispatcher, types, F
# from aiogram.filters import Command
# from keyboards import main_kb, food_kb, BTN_EXIT, BTN_TOP, BTN_FEED, BTN_PLAY, BTN_SLEEP, BTN_STATUS


# click_count = 0  # Счётчик кликов для кнопки "Top"

# def progress_bar(value: int, length: int):
#     filled = int(value/100 * 10)
#     return "🟩" * filled + "⬛" * (length - filled)
 
# # Здесь лежат все наши функции отвечающие за перехват всех функций - диспетчер(перехватчик событий)

# async def start_handler(message: types.Message): # функция отвечающая за команду: start
#     user_id = message.from_user.id # Получаем id пользователя
#     print(f"start_handler triggered by user {user_id}")  # Отладка

#     # Бот - питомцы
#     if user_id not in pets:
#         new_pet = {
#             "name": "Baks😜",
#             "hunger": 50, # параметр голод
#             "energy": 50, # параметр энергия
#             "happiness": 50, # параметр счастья
#             "health": 50    # НОВОЕ
#         }
#         pets[user_id] = new_pet # Если новый пользователь ещё не заходил мы создаём ему нового питомца

#     await message.answer(
#         f"Привет, {message.from_user.first_name}!\n" # Обращаемся к пользователю по имени
#         f"Познакомься со своим питомцем: {pets[user_id]['name']}!\n"  # Исправлено: одинарные кавычки для ключа
#         f"Позаботься о нём!",
#         reply_markup=main_kb
#     )


# async def about_handler(message: types.Message):
#     print(f"about_handler triggered by user {message.from_user.id}")  # Отладка
#     author_nick = "@Aleks16555den"  # Ваш ник
#     description = (
#         "Это мой питомец-бот! Здесь вы можете ухаживать за питомцем, кормить, играть и смотреть его статус.\n"
#         f"Создатель этого бота: {author_nick}\n"
#         "Для возврата в меню нажмите /start."  # Добавлено, чтобы не казалось пустым
#     )
#     await message.answer(description)


# async def feed_pet(message: types.Message):
#     user_id = message.from_user.id
#     print(f"feed_pet triggered by user {user_id}")  # Отладка
#     if user_id not in pets:
#         await message.answer("Сначала запусти бота с помощью команды /start")
#         return
#     pet = pets[user_id]
#     await message.answer(f"Чем вы хотите покрмить {pet['name']}?", reply_markup=food_kb)

    
#     # pet["hunger"] = min(pet["hunger"] + 10, 100) # Функция минимума
#     # pet["energy"] = max(pet["energy"] - 5, 0)
#     # await message.answer(f"{pet['name']} вкусно покушал!")

# async def feed_click(message: types.Message):
#     user_id = message.from_user.id
#     pet = pets.get(user_id)
#     if not pet:
#         await message.answer("У тебя нет питомца! Создай его командой /start.")
#         return
#     await message.answer("Выбери еду для питомца:", reply_markup=food_kb)

# async def play_pet(message: types.Message):
#     user_id = message.from_user.id
#     print(f"play_pet triggered by user {user_id}")  # Отладка
#     if user_id not in pets:
#         await message.answer("Сначала запусти бота с помощью команды /start")
#         return
#     pet = pets[user_id]
#     pet["happiness"] = min(pet["happiness"] + 10, 100) # Функция минимума
#     pet["energy"] = max(pet["energy"] - 15, 0)
#     await message.answer(f"{pet['name']} Весело поиграл!")


# async def status_pet(message: types.Message):
#     user_id = message.from_user.id
#     print(f"status_pet triggered by user {user_id}")  # Отладка
#     if user_id not in pets:
#         await message.answer("Сначала запусти бота с помощью команды /start")
#         return
#     pet = pets[user_id]
#     hun = pet['hunger']
#     en = pet['energy']
#     hap = pet['happiness']

#     status = (
#         f"Статус вашего питомца {pet['name']}:\n"
#         f"Сытость: {hun}% {progress_bar(hun, 10)}\n"
#         f"Энергия: {en}% {progress_bar(en, 10)}\n"
#         f"Счастье: {hap}% {progress_bar(hap, 10)}"
#         f"Здоровье: {pet['health']}% {progress_bar(pet['health'], 10)}"  # НОВОЕ: добавил эту строку
#     )
#     await message.answer(status)


# # message_handler(lambda message: message.text == "💤Спать")  # Исправлено: добавлен эмодзи 💤, как в keyboards.py
# async def sleep_pet(message: types.Message):
#     print("sleep_pet triggered by user", message.from_user.id)  # Это лог: добавь его, чтобы видеть в терминале, когда кнопка нажата
#     user_id = message.from_user.id
#     if user_id in pets:
#         pets[user_id]['energy'] = min(pets[user_id]['energy'] + 20, 100)  # Восстанавливаем энергию (не больше 100%)
#         await message.reply(f"Питомец поспал и восстановил энергию! Энергия: {pets[user_id]['energy']}%")
#     else:
#         await message.reply("У тебя нет питомца! Сначала нажми /start.")

# async def top_click(message: types.Message):
#     global click_count  # Используем глобальную переменную из main.py
#     click_count += 1  # Увеличиваем счётчик на 1
#     await message.answer(f"Ты нажал на Top {click_count} раз!", reply_markup=main_kb)


# # НОВЫЙ ОБРАБОТЧИК: добавь после top_click
# async def heal_pet(message: types.Message):
#     user_id = message.from_user.id
#     print(f"heal_pet triggered by user {user_id}")  # Отладка
#     if user_id not in pets:
#         await message.answer("Сначала запусти бота с помощью команды /start")
#         return
#     pet = pets[user_id]
#     if pet["energy"] >= 5:  # Проверяем, есть ли энергия для лечения
#         pet["health"] = min(100, pet["health"] + 10)  # Увеличиваем здоровье на 10, но не выше 100
#         pet["energy"] = max(0, pet["energy"] - 5)     # Уменьшаем энергию на 5, но не ниже 0
#         await message.answer(f"{pet['name']} подлечился! ❤️ Здоровье: {pet['health']}%, ⚡ Энергия: {pet['energy']}%")
#     else:
#         await message.answer(f"{pet['name']} слишком устал! Сначала отдохни или поиграй, чтобы восстановить энергию.")


# async def food_callback_handler(callback: types.CallbackQuery): # Запрос через кнопки логика обработки этих кнопок
#     user_id = callback.from_user.id
#     print(f"food_callback_handler triggered by user {user_id} with data {callback.data}")  # Отладка
#     if user_id not in pets:
#         await callback.message.edit_text("Сначала запусти бота с помощью команды /start")# Редактируем наше сообщение
#         return
    
#     pet = pets[user_id]
#     food = callback.data
#     message = "" # Где будем хранить сообщения для ответа пользователю
#     h = pet["hunger"]

#     if food == "feed_steak":
#       h =  pet["hunger"] + 20
#       message = f"Вы покормили {pet['name']} вкусным стейком"

#     elif food == "feed_turkey":
#       h =  pet["hunger"] + 15
#       message = f"Вы покормили {pet['name']} вкусной индейкой"  

#     elif food == "feed_water":
#       h =  pet["hunger"] + 5
#       message = f"Вы дали {pet['name']} немного воды!"

#     pet["hunger"] = min(100, h)

#     # Для перезаписи нашего сообщения
#     await callback.message.edit_text(message)
#     await callback.answer(
#         f"Сытость {pet['name']} -- {pet['hunger']}/100\n"
#         f"{progress_bar(pet['hunger'], 10)}"        
#         )

    
# async def register_handlers(dp: Dispatcher): #картотека которая отслеживает все наши действия с телеграмма
#     dp.message.register(start_handler, Command("start"))
#     dp.message.register(about_handler, Command("about"))# Новая строка для /about
#     dp.message.register(play_pet,F.text == BTN_PLAY)
#     dp.message.register(feed_pet, F.text == BTN_FEED)
#     dp.message.register(status_pet, F.text == BTN_STATUS)
#     dp.message.register(sleep_pet, F.text == BTN_SLEEP)  # Новая строка для кнопки "Спать"
#     dp.message.register(top_click, F.text == BTN_TOP)  # Новая строка для кнопки "Top"
#     dp.message.register(heal_pet, F.text == "❤️ Подлечить")  # НОВОЕ: регистрация обработчика
#     dp.callback_query.register(food_callback_handler, lambda c: 
#     c.data.startswith("feed_")) # Функция перехватчик кнопок с вариантами кормления




# from db import pets

# from aiogram import Dispatcher, types, F
# from aiogram.filters import Command

# from keyboards import main_kb, food_kb, BTN_EXIT, BTN_FEED, BTN_PLAY, BTN_SLEEP, BTN_STATUS


# def progress_bar(value: int, length: int):
#     filled = int(value/100 * 10)
#     return "🟩" * filled + "⬛" * (length - filled)
   

# # Здесь лежат все наши функции отвечающие за перехват всех функций - диспетчер(перехватчик событий)

# async def start_handler(message: types.Message): # функция отвечающая за команду: start
#     user_id = message.from_user.id # Получаем id пользователя


# # Бот - питомцы
#     if user_id not in pets:
#         new_pet = {
#             "name": "Baks😜",
#             "hunger": 50, # параметр голод
#             "energy": 50, # параметр энергия
#             "happiness": 50 # параметр счастья

#         }
#         pets[user_id] = new_pet # Если новый пользователь ещё не заходил мы создаём ему нового питомца

#     await message.answer(
#         f"Привет, {message.from_user.first_name}!\n" # Обращаемся к пользователю по имени
#         f"Познакомься со своим питомцем: {pets[user_id]["name"]}!\n"
#         f"Позаботься о нём!",
#         reply_markup=main_kb
#     )


# async def about_handler(message: types.Message):
#     author_nick = "@Aleks16555den"  # Ваш ник, как в коде
#     description = (
#         "Это мой питомец-бот! Здесь вы можете ухаживать за питомцем, кормить, играть и смотреть его статус.\n"
#         f"Создатель этого бота: {author_nick}"  # Просто текст с @
#     )
#     await message.answer(description)

# async def feed_pet(message: types.Message):
#     user_id = message.from_user.id
#     if user_id not in pets:
#         await message.answer("Сначала запусти бота с помощью команды /start")
#         return
#     pet = pets[user_id]
#     await message.answer(f"Чем вы хотите покрмить {pet['name']}?", reply_markup=food_kb)

    
#     # pet["hunger"] = min(pet["hunger"] + 10, 100) # Функция минимума
#     # pet["energy"] = max(pet["energy"] - 5, 0)
#     # await message.answer(f"{pet['name']} вкусно покушал!")


# async def play_pet(message: types.Message):
#     user_id = message.from_user.id
#     if user_id not in pets:
#         await message.answer("Сначала запусти бота с помощью команды /start")
#         return
#     pet = pets[user_id]
#     pet["happiness"] = min(pet["happiness"] + 10, 100) # Функция минимума
#     pet["energy"] = max(pet["energy"] - 15, 0)
#     await message.answer(f"{pet['name']} Весело поиграл!")


# async def status_pet(message: types.Message):
#     user_id = message.from_user.id
#     if user_id not in pets:
#         await message.answer("Сначала запусти бота с помощью команды /start")
#         return
#     pet = pets[user_id]
#     hun = pet['hunger']
#     en = pet['energy']
#     hap = pet['happiness']

#     status = (
#         f"Статус вашего питомца {pet['name']}:\n"
#         f"Сытость: {hun}% {progress_bar(hun, 10)}\n"
#         f"Энергия: {en}% {progress_bar(en, 10)}\n"
#         f"Счастье: {hap}% {progress_bar(hap, 10)}"
#     )
#     await message.answer(status)


# async def food_callback_handler(callback: types.CallbackQuery): # Запрос через кнопки логика обработки этих кнопок
#     user_id = callback.from_user.id
#     if user_id not in pets:
#         await callback.message.edit_text("Сначала запусти бота с помощью команды /start")# Редактируем наше сообщение
#         return
    
#     pet = pets[user_id]
#     food = callback.data
#     message = "" # Где будем хранить сообщения для ответа пользователю
#     h = pet["hunger"]

#     if food == "feed_steak":
#       h =  pet["hunger"] + 20
#       message = f"Вы покормили {pet['name']} вкусным стейком"

#     elif food == "feed_turkey":
#       h =  pet["hunger"] + 15
#       message = f"Вы покормили {pet['name']} вкусной индейкой"  

#     elif food == "feed_water":
#       h =  pet["hunger"] + 5
#       message = f"Вы дали {pet['name']} немного воды!"

#     pet["hunger"] = min(100, h)

#     # Для перезаписи нашего сообщения
#     await callback.message.edit_text(message)
#     await callback.answer(
#         f"Сытость {pet['name']} -- {pet['hunger']}/100\n"
#         f"{progress_bar(pet['hunger'], 10)}"        
#         )

    
# async def register_handlers(dp: Dispatcher): #картотека которая отслеживает все наши действия с телеграмма
#     dp.message.register(start_handler, Command("start"))
#     dp.message.register(about_handler, Command("about"))# Новая строка для /about
#     dp.message.register(play_pet,F.text == BTN_PLAY)
#     dp.message.register(feed_pet, F.text == BTN_FEED)
#     dp.message.register(status_pet, F.text == BTN_STATUS)
#     dp.callback_query.register(food_callback_handler, lambda c: 
# c.data.startswith("feed_")) # Функция перехватчик кнопок с вариантами кормления
