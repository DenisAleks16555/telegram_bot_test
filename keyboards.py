from aiogram import types  # Библиотека для бота телеграмм

BTN_FEED = "🎉Покормить"
BTN_PLAY = "🎈Поиграть"
BTN_SLEEP = "💤Спать"  # Новая константа для кнопки "Спать"
BTN_STATUS = "🛠Статус"
BTN_EXIT = "🔴Выход"
BTN_TOP = "🏆Top"  # Новая константа для кнопки "Top"

# Делаем клавиатуру для бота
main_kb = types.ReplyKeyboardMarkup(
    keyboard=[
       [types.KeyboardButton(text=BTN_FEED), types.KeyboardButton(text=BTN_PLAY)],
       [types.KeyboardButton(text=BTN_SLEEP), types.KeyboardButton(text=BTN_STATUS)],
       [types.KeyboardButton(text=BTN_EXIT), types.KeyboardButton(text=BTN_TOP)]  # Добавили кнопку "Top" рядом с "Выход"
    ],
    resize_keyboard=True  # Растягивает клавиатуру по экран
 )

# Метод который отвечает за удаление клавиатуры
remove_kb = types.ReplyKeyboardRemove()

# Делаем клавиатуру допустим чем покормить питомца
food_kb = types.InlineKeyboardMarkup(
    inline_keyboard=[
        [
            types.InlineKeyboardButton(text="🍗 Курица", callback_data="feed_turkey"),
            types.InlineKeyboardButton(text="🥩 Стейк", callback_data="feed_steak")
        ],
        [types.InlineKeyboardButton(text="🥛 Дать попить", callback_data="feed_water")]
    ]
)






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