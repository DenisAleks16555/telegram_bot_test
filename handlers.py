from db import pets
from aiogram import Dispatcher, types, F
from aiogram.filters import Command
from keyboards import main_kb, food_kb, BTN_EXIT, BTN_TOP, BTN_FEED, BTN_PLAY, BTN_SLEEP, BTN_STATUS


click_count = 0  # Счётчик кликов для кнопки "Top"

def progress_bar(value: int, length: int):
    filled = int(value/100 * 10)
    return "🟩" * filled + "⬛" * (length - filled)
 
# Здесь лежат все наши функции отвечающие за перехват всех функций - диспетчер(перехватчик событий)

async def start_handler(message: types.Message): # функция отвечающая за команду: start
    user_id = message.from_user.id # Получаем id пользователя
    print(f"start_handler triggered by user {user_id}")  # Отладка

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
        f"Познакомься со своим питомцем: {pets[user_id]['name']}!\n"  # Исправлено: одинарные кавычки для ключа
        f"Позаботься о нём!",
        reply_markup=main_kb
    )


async def about_handler(message: types.Message):
    print(f"about_handler triggered by user {message.from_user.id}")  # Отладка
    author_nick = "@Aleks16555den"  # Ваш ник
    description = (
        "Это мой питомец-бот! Здесь вы можете ухаживать за питомцем, кормить, играть и смотреть его статус.\n"
        f"Создатель этого бота: {author_nick}\n"
        "Для возврата в меню нажмите /start."  # Добавлено, чтобы не казалось пустым
    )
    await message.answer(description)


async def feed_pet(message: types.Message):
    user_id = message.from_user.id
    print(f"feed_pet triggered by user {user_id}")  # Отладка
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
    print(f"play_pet triggered by user {user_id}")  # Отладка
    if user_id not in pets:
        await message.answer("Сначала запусти бота с помощью команды /start")
        return
    pet = pets[user_id]
    pet["happiness"] = min(pet["happiness"] + 10, 100) # Функция минимума
    pet["energy"] = max(pet["energy"] - 15, 0)
    await message.answer(f"{pet['name']} Весело поиграл!")


async def status_pet(message: types.Message):
    user_id = message.from_user.id
    print(f"status_pet triggered by user {user_id}")  # Отладка
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


# message_handler(lambda message: message.text == "💤Спать")  # Исправлено: добавлен эмодзи 💤, как в keyboards.py
async def sleep_pet(message: types.Message):
    print("sleep_pet triggered by user", message.from_user.id)  # Это лог: добавь его, чтобы видеть в терминале, когда кнопка нажата
    user_id = message.from_user.id
    if user_id in pets:
        pets[user_id]['energy'] = min(pets[user_id]['energy'] + 20, 100)  # Восстанавливаем энергию (не больше 100%)
        await message.reply(f"Питомец поспал и восстановил энергию! Энергия: {pets[user_id]['energy']}%")
    else:
        await message.reply("У тебя нет питомца! Сначала нажми /start.")

async def top_click(message: types.Message):
    global click_count  # Используем глобальную переменную из main.py
    click_count += 1  # Увеличиваем счётчик на 1
    await message.answer(f"Ты нажал на Top {click_count} раз!", reply_markup=main_kb)

async def food_callback_handler(callback: types.CallbackQuery): # Запрос через кнопки логика обработки этих кнопок
    user_id = callback.from_user.id
    print(f"food_callback_handler triggered by user {user_id} with data {callback.data}")  # Отладка
    if user_id not in pets:
        await callback.message.edit_text("Сначала запусти бота с помощью команды /start")# Редактируем наше сообщение
        return
    
    pet = pets[user_id]
    food = callback.data
    message = "" # Где будем хранить сообщения для ответа пользователю
    h = pet["hunger"]

    if food == "feed_steak":
      h =  pet["hunger"] + 20
      message = f"Вы покормили {pet['name']} вкусным стейком"

    elif food == "feed_turkey":
      h =  pet["hunger"] + 15
      message = f"Вы покормили {pet['name']} вкусной индейкой"  

    elif food == "feed_water":
      h =  pet["hunger"] + 5
      message = f"Вы дали {pet['name']} немного воды!"

    pet["hunger"] = min(100, h)

    # Для перезаписи нашего сообщения
    await callback.message.edit_text(message)
    await callback.answer(
        f"Сытость {pet['name']} -- {pet['hunger']}/100\n"
        f"{progress_bar(pet['hunger'], 10)}"        
        )

    
async def register_handlers(dp: Dispatcher): #картотека которая отслеживает все наши действия с телеграмма
    dp.message.register(start_handler, Command("start"))
    dp.message.register(about_handler, Command("about"))# Новая строка для /about
    dp.message.register(play_pet,F.text == BTN_PLAY)
    dp.message.register(feed_pet, F.text == BTN_FEED)
    dp.message.register(status_pet, F.text == BTN_STATUS)
    dp.message.register(sleep_pet, F.text == BTN_SLEEP)  # Новая строка для кнопки "Спать"
    dp.message.register(top_click, F.text == BTN_TOP)  # Новая строка для кнопки "Top"
    dp.callback_query.register(food_callback_handler, lambda c: 
c.data.startswith("feed_")) # Функция перехватчик кнопок с вариантами кормления




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
