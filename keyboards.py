from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder

main_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="📊 Статус"), KeyboardButton(text="🍗 Кормить")],
        [KeyboardButton(text="🎮 Играть"), KeyboardButton(text="😴 Уложить спать")],
        [KeyboardButton(text="💊 Лечить")]
    ],
    resize_keyboard=True
)

back_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="↩️ Назад")]
    ],
    resize_keyboard=True
)

def feed_keyboard():
    builder = ReplyKeyboardBuilder()
    builder.add(
        KeyboardButton(text="🍗 Курица"),
        KeyboardButton(text="🥩 Мясо"),
        KeyboardButton(text="💧 Вода"),
        KeyboardButton(text="↩️ Назад")
    )
    builder.adjust(2)
    return builder.as_markup(resize_keyboard=True)

def games_keyboard():
    builder = ReplyKeyboardBuilder()
    builder.add(
        KeyboardButton(text="🎾 Теннис"),
        KeyboardButton(text="🧸 Пазлы"),
        KeyboardButton(text="🎯 Цель"),
        KeyboardButton(text="↩️ Назад")
    )
    builder.adjust(2)
    return builder.as_markup(resize_keyboard=True)





# from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
# from aiogram.utils.keyboard import ReplyKeyboardBuilder

# main_keyboard = ReplyKeyboardMarkup(
#     keyboard=[
#         [KeyboardButton(text="📊 Статус"), KeyboardButton(text="🍗 Кормить")],
#         [KeyboardButton(text="🎮 Играть"), KeyboardButton(text="😴 Уложить спать")],
#         [KeyboardButton(text="💊 Лечить")]
#     ],
#     resize_keyboard=True
# )

# back_keyboard = ReplyKeyboardMarkup(
#     keyboard=[
#         [KeyboardButton(text="↩️ Назад")]
#     ],
#     resize_keyboard=True
# )

# def feed_keyboard():
#     builder = ReplyKeyboardBuilder()
#     builder.add(
#         KeyboardButton(text="🍗 Курица"),
#         KeyboardButton(text="🥩 Мясо"),
#         KeyboardButton(text="💧 Вода"),
#         KeyboardButton(text="↩️ Назад")
#     )
#     builder.adjust(2)
#     return builder.as_markup(resize_keyboard=True)

# def games_keyboard():
#     builder = ReplyKeyboardBuilder()
#     builder.add(
#         KeyboardButton(text="🎾 Теннис"),
#         KeyboardButton(text="🧸 Пазлы"),
#         KeyboardButton(text="🎯 Цель"),
#         KeyboardButton(text="↩️ Назад")
#     )
#     builder.adjust(2)
#     return builder.as_markup(resize_keyboard=True)
















# from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

# # Основная клавиатура (Reply Keyboard)
# main_keyboard_builder = ReplyKeyboardBuilder()
# main_keyboard_builder.add("🍗 Кормить", "💧 Напоить", "😴 Уложить спать", "💊 Лечить", "📊 Статус", "🎾 Играть")
# main_keyboard_builder.adjust(2)  # 2 кнопки в ряд
# main_keyboard = main_keyboard_builder.as_markup()  # Готовый ReplyKeyboardMarkup

# # Клавиатура для возврата назад (Inline)
# back_keyboard_builder = InlineKeyboardBuilder()
# back_keyboard_builder.add("⬅️ Назад")
# back_keyboard = back_keyboard_builder.as_markup()  # Готовый InlineKeyboardMarkup

# # Клавиатура для кормления (Inline)
# feed_keyboard_builder = InlineKeyboardBuilder()
# feed_keyboard_builder.add("🍗 Курица", "🥩 Мясо", "💧 Вода", "⬅️ Назад")
# feed_keyboard_builder.adjust(2)  # 2 кнопки в ряд
# feed_keyboard = feed_keyboard_builder.as_markup()  # Готовый InlineKeyboardMarkup

# # Клавиатура для сна (если нужна, но в коде sleep напрямую)
# sleep_keyboard_builder = InlineKeyboardBuilder()
# sleep_keyboard_builder.add("😴 Уложить спать", "⬅️ Назад")
# sleep_keyboard = sleep_keyboard_builder.as_markup()  # Готовый InlineKeyboardMarkup

# # Клавиатура для лечения (если нужна, но в коде heal напрямую)
# heal_keyboard_builder = InlineKeyboardBuilder()
# heal_keyboard_builder.add("💊 Лечить", "⬅️ Назад")
# heal_keyboard = heal_keyboard_builder.as_markup()  # Готовый InlineKeyboardMarkup

# # Inline-клавиатура для игр
# games_keyboard_builder = InlineKeyboardBuilder()
# games_keyboard_builder.add("🎾 Теннис", "🧩 Пазлы", "🎯 Цель", "⬅️ Назад")
# games_keyboard_builder.adjust(1)  # 1 кнопка в ряд
# games_keyboard = games_keyboard_builder.as_markup()  # Готовый InlineKeyboardMarkup
























# from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

# # Основная клавиатура (Reply Keyboard)
# main_keyboard_builder = ReplyKeyboardBuilder()
# main_keyboard_builder.add("🍗 Кормить", "💧 Напоить", "😴 Уложить спать", "💊 Лечить", "📊 Статус", "🎾 Играть")
# main_keyboard_builder.adjust(2)  # 2 кнопки в ряд
# main_keyboard = main_keyboard_builder.as_markup()  # <-- ДОБАВИЛ .as_markup()

# # Inline-клавиатура для игр
# games_keyboard_builder = InlineKeyboardBuilder()
# games_keyboard_builder.add("🎾 Теннис", "🧩 Пазлы", "🎯 Цель")
# games_keyboard_builder.adjust(1)  # 1 кнопка в ряд
# games_keyboard = games_keyboard_builder.as_markup()  # <-- ДОБАВИЛ .as_markup()










# from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

# # Основная клавиатура (Reply)
# main_keyboard = ReplyKeyboardBuilder()
# main_keyboard.button(text="Статус")
# main_keyboard.button(text="Кормить")
# main_keyboard.button(text="Спать")
# main_keyboard.button(text="Лечить")
# main_keyboard.button(text="Игры")
# main_keyboard.adjust(2)

# # Клавиатура "Назад" (Inline)
# back_keyboard = InlineKeyboardBuilder()
# back_keyboard.button(text="Назад", callback_data="back")
# back_keyboard.adjust(1)

# # Клавиатура кормления (Inline)
# feed_keyboard = InlineKeyboardBuilder()
# feed_keyboard.button(text="Курица", callback_data="chicken")
# feed_keyboard.button(text="Мясо", callback_data="meat")
# feed_keyboard.button(text="Вода", callback_data="water")
# feed_keyboard.button(text="Назад", callback_data="back")
# feed_keyboard.adjust(2)

# # Клавиатура сна (Inline) — если нужно, но в handlers.py sleep напрямую
# sleep_keyboard = InlineKeyboardBuilder()
# sleep_keyboard.button(text="Спать", callback_data="sleep")
# sleep_keyboard.button(text="Назад", callback_data="back")
# sleep_keyboard.adjust(1)

# # Клавиатура лечения (Inline) — если нужно, но в handlers.py heal напрямую
# heal_keyboard = InlineKeyboardBuilder()
# heal_keyboard.button(text="Лечить", callback_data="heal")
# heal_keyboard.button(text="Назад", callback_data="back")
# heal_keyboard.adjust(1)

# # Клавиатура игр (Inline)
# games_keyboard = InlineKeyboardBuilder()
# games_keyboard.button(text="Теннис", callback_data="tennis")
# games_keyboard.button(text="Пазлы", callback_data="puzzles")
# games_keyboard.button(text="Цель", callback_data="goal")
# games_keyboard.button(text="Назад", callback_data="back")
# games_keyboard.adjust(2)




































# from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton

# main_keyboard = ReplyKeyboardMarkup(
#     keyboard=[
#         [KeyboardButton(text="🍗 Курица"), KeyboardButton(text="🥩 Мясо")],
#         [KeyboardButton(text="💧 Вода"), KeyboardButton(text="😴 Сон")],
#         [KeyboardButton(text="🩹 Лечение"), KeyboardButton(text="Статус")],
#         [KeyboardButton(text="Играть")]
#     ],
#     resize_keyboard=True
# )

# game_keyboard = InlineKeyboardMarkup(inline_keyboard=[
#     [InlineKeyboardButton(text="🎾 Теннис", callback_data="tennis")],
#     [InlineKeyboardButton(text="🧩 Пазлы", callback_data="puzzle")],
#     [InlineKeyboardButton(text="🎯 Цель", callback_data="target")],
#     [InlineKeyboardButton(text="Назад", callback_data="back")]
# ])








# from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# main_keyboard = ReplyKeyboardMarkup(
#     keyboard=[
#         [KeyboardButton(text="Статус"), KeyboardButton(text="Кормить")],
#         [KeyboardButton(text="Сон"), KeyboardButton(text="Лечение")],
#         [KeyboardButton(text="Играть"), KeyboardButton(text="Top")]  # Добавили "Играть"
#     ],
#     resize_keyboard=True
# )

# feed_keyboard = ReplyKeyboardMarkup(
#     keyboard=[
#         [KeyboardButton(text="Курица"), KeyboardButton(text="Мясо")],
#         [KeyboardButton(text="Вода"), KeyboardButton(text="Назад")]
#     ],
#     resize_keyboard=True
# )

# from aiogram.types import ReplyKeyboardMarkup, KeyboardButton



# # Новая клавиатура для выбора игры
# game_keyboard = ReplyKeyboardMarkup(
#     keyboard=[
#         [KeyboardButton(text="🎾 Поиграть в мяч"), KeyboardButton(text="🧩 Пазл")],
#         [KeyboardButton(text="🎯 Тренировка"), KeyboardButton(text="🔄 Назад")]
#     ],
#     resize_keyboard=True
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