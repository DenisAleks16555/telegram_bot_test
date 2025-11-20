from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Статус"), KeyboardButton(text="Кормить")],
        [KeyboardButton(text="Сон"), KeyboardButton(text="Лечение")],
        [KeyboardButton(text="Top")]  # Новая кнопка для статистики
    ],
    resize_keyboard=True
)

feed_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Курица"), KeyboardButton(text="Мясо")],
        [KeyboardButton(text="Вода"), KeyboardButton(text="Назад")]
    ],
    resize_keyboard=True
)







# from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# # Главное меню
# main_kb = ReplyKeyboardMarkup(
#     keyboard=[
#         [KeyboardButton(text="🍽 Покормить")],
#         [KeyboardButton(text="😴 Уложить спать"), KeyboardButton(text="❤️ Подлечить")],
#         [KeyboardButton(text="📊 Статус")]
#     ],
#     resize_keyboard=True,
#     one_time_keyboard=False
# )

# # Меню еды (только стейк, мясо, вода, назад)
# food_kb = ReplyKeyboardMarkup(
#     keyboard=[
#         [KeyboardButton(text="🥩 Стейк"), KeyboardButton(text="🥩 Мясо")],
#         [KeyboardButton(text="💧 Вода")],
#         [KeyboardButton(text="⬅️ Назад")]
#     ],
#     resize_keyboard=True,
#     one_time_keyboard=False
# )

















# from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# # Главное меню
# main_kb = ReplyKeyboardMarkup(
#     keyboard=[
#         [KeyboardButton(text="🍽 Покормить")],
#         [KeyboardButton(text="😴 Уложить спать"), KeyboardButton(text="❤️ Подлечить")],
#         [KeyboardButton(text="📊 Статус")]
#     ],
#     resize_keyboard=True,
#     one_time_keyboard=False
# )

# # Меню еды
# food_kb = ReplyKeyboardMarkup(
#     keyboard=[
#         [KeyboardButton(text="🍗 Курица"), KeyboardButton(text="🥩 Стейк")],
#         [KeyboardButton(text="🍎 Яблоко"), KeyboardButton(text="🥩 Мясо")],
#         [KeyboardButton(text="🍞 Хлеб"), KeyboardButton(text="🍪 Печенье")],
#         [KeyboardButton(text="💧 Вода"), KeyboardButton(text="⬅️ Назад")]
#     ],
#     resize_keyboard=True,
#     one_time_keyboard=False
# )






# from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# # Reply-клавиатура для меню еды
# food_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
# food_kb.add(
#     KeyboardButton("🍗 Курица"),
#     KeyboardButton("🥩 Стейк"),
#     KeyboardButton("🍎 Яблоко"),
#     KeyboardButton("🥩 Мясо"),
#     KeyboardButton("🍞 Хлеб"),
#     KeyboardButton("🍪 Печенье"),
#     KeyboardButton("💧 Вода")
# )
# food_kb.add(KeyboardButton("⬅️ Назад"))  # Кнопка для возврата в главное меню

# # Главная reply-клавиатура (для старта и навигации)
# main_kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
# main_kb.add(
#     KeyboardButton("🍽 Покормить"),
#     KeyboardButton("😴 Уложить спать"),
#     KeyboardButton("❤️ Подлечить"),
#     KeyboardButton("📊 Статус")
# )



# from aiogram import types # Библиотека для бота телеграмм

# # Кнопки (твои существующие)
# BTN_FEED = "🍎 Покормить"
# BTN_PLAY = "🎾 Поиграть"
# BTN_SLEEP = "😴 Спать"
# BTN_STATUS = "🛠Статус"
# BTN_EXIT = "🚪 Выход"
# BTN_TOP = "📊 Top"  # Новая константа для кнопки "Top"

# # Основная клавиатура (существующая, с новой кнопкой)
# main_kb = types.ReplyKeyboardMarkup(
#     keyboard=[
#         [types.KeyboardButton(text=BTN_FEED), types.KeyboardButton(text=BTN_PLAY)],
#         [types.KeyboardButton(text=BTN_SLEEP), types.KeyboardButton(text=BTN_STATUS)],
#         [types.KeyboardButton(text=BTN_EXIT), types.KeyboardButton(text=BTN_TOP)],
#         [types.KeyboardButton(text="❤️ Подлечить")]  # НОВАЯ КНОПКА: добавлена в новую строку
#     ],
#     resize_keyboard=True
# )





# from aiogram import types  # Библиотека для бота телеграмм

# # Кнопки (твои существующие)
# BTN_FEED = "🍎 Покормить"
# BTN_PLAY = "🎾 Поиграть"
# BTN_SLEEP = "😴 Спать"
# BTN_STATUS = "🛠Статус"
# BTN_EXIT = "🚪 Выход"
# BTN_TOP = "📊 Top"  # Новая константа для кнопки "Top"

# # Основная клавиатура (существующая, с новой кнопкой)
# main_kb = types.ReplyKeyboardMarkup(
#     keyboard=[
#         [types.KeyboardButton(text=BTN_FEED), types.KeyboardButton(text=BTN_PLAY)],
#         [types.KeyboardButton(text=BTN_SLEEP), types.KeyboardButton(text=BTN_STATUS)],
#         [types.KeyboardButton(text=BTN_EXIT), types.KeyboardButton(text=BTN_TOP)],
#         [types.KeyboardButton(text="❤️ Подлечить")]  # НОВАЯ КНОПКА: добавлена в новую строку
#     ],
#     resize_keyboard=True
# )

# # Клавиатура для еды (inline-версия со ВСЕМИ кнопками: старые + новые)
# food_kb = types.InlineKeyboardMarkup(
#     inline_keyboard=[
#         [types.InlineKeyboardButton(text="🍗 Курица", callback_data="chicken"),
#          types.InlineKeyboardButton(text="🥩 Стейк", callback_data="steak")],
#         [types.InlineKeyboardButton(text="🍎 Яблоко", callback_data="apple"),
#          types.InlineKeyboardButton(text="🥩 Мясо", callback_data="meat")],
#         [types.InlineKeyboardButton(text="🍞 Хлеб", callback_data="bread"),
#          types.InlineKeyboardButton(text="🍪 Печенье", callback_data="cookie")],
#         [types.InlineKeyboardButton(text="🚰 Вода", callback_data="water"),
#          types.InlineKeyboardButton(text="⬅️ Назад", callback_data="back")]
#     ]
# )




















# # Клавиатура для еды (существующая, без изменений)
# food_kb = types.ReplyKeyboardMarkup(
#     keyboard=[
#         [types.KeyboardButton(text="🍎 Яблоко"), types.KeyboardButton(text="🥩 Мясо")],
#         [types.KeyboardButton(text="🍞 Хлеб"), types.KeyboardButton(text="🍪 Печенье")],
#         [types.KeyboardButton(text="⬅️ Назад")]
#     ],
#     resize_keyboard=True
# )


# from aiogram import types  # Библиотека для бота телеграмм

# BTN_FEED = "🎉Покормить"
# BTN_PLAY = "🎈Поиграть"
# BTN_SLEEP = "💤Спать"  # Новая константа для кнопки "Спать"
# BTN_STATUS = "🛠Статус"
# BTN_EXIT = "🔴Выход"
# BTN_TOP = "🏆Top"  # Новая константа для кнопки "Top"

# Делаем клавиатуру для бота
# main_kb = types.ReplyKeyboardMarkup(
#     keyboard=[
#        [types.KeyboardButton(text=BTN_FEED), types.KeyboardButton(text=BTN_PLAY)],
#        [types.KeyboardButton(text=BTN_SLEEP), types.KeyboardButton(text=BTN_STATUS)],
#        [types.KeyboardButton(text=BTN_EXIT), types.KeyboardButton(text=BTN_TOP)]  # Добавили кнопку "Top" рядом с "Выход"
#        [types.KeyboardButton(text="❤️ Подлечить")]  # НОВОЕ: добавь эту строку в новую строку
#     ],
#     resize_keyboard=True  # Растягивает клавиатуру по экран
#  )

# Метод который отвечает за удаление клавиатуры
# remove_kb = types.ReplyKeyboardRemove()

# # Делаем клавиатуру допустим чем покормить питомца
# food_kb = types.InlineKeyboardMarkup(
#     inline_keyboard=[
#         [
#             types.InlineKeyboardButton(text="🍗 Курица", callback_data="feed_turkey"),
#             types.InlineKeyboardButton(text="🥩 Стейк", callback_data="feed_steak")
#         ],
#         [types.InlineKeyboardButton(text="🥛 Дать попить", callback_data="feed_water")]
#     ]
# )






# from aiogram import types # Библиотека для бота телеграмм

# BTN_FEED = "🎉Покормить"
# BTN_PLAY = "🎈Поиграть"
# BTN_SLEEP = "💤Спать"  # Новая константа для кнопки "Спать"
# BTN_STATUS = "🛠Статус"
# BTN_EXIT = "🔴Выход"


# # Делаем клавиатуру для бота
# main_kb = types.ReplyKeyboardMarkup(
#     keyboard=[
#        [types.KeyboardButton(text=BTN_FEED), types.KeyboardButton(text=BTN_PLAY)],
#        [types.KeyboardButton(text=BTN_SLEEP), types.KeyboardButton(text=BTN_STATUS)],
#        [types.KeyboardButton(text=BTN_EXIT)] # Создаём кнопку - внизу будет кнопка "выход"
#     ],
#     resize_keyboard=True # Растягивает клавиатуру по экран
#  )

# # Метод который отвечает за удаление клавиатуры
# remove_kb = types.ReplyKeyboardRemove()


# # Делаем клавиатуру допустим чем покормить питомца

# food_kb = types.InlineKeyboardMarkup(
#     inline_keyboard= [
#         [
#             types.InlineKeyboardButton(text="🍗 Курица", callback_data="feed_turkey"),
#             types.InlineKeyboardButton(text="🥩 Стейк", callback_data="feed_steak")
#         ],
#         [types.InlineKeyboardButton(text="🥛 Дать попить", callback_data="feed_water")]
#     ]
# )