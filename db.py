
import asyncio
from collections import defaultdict

pets = defaultdict(dict)  # Словарь для хранения данных питомцев по user_id

async def background_task():
    while True:
        await asyncio.sleep(60)  # Каждые 60 секунд
        for user_id, data in pets.items():
            # Уменьшаем stats
            data['hunger'] = max(0, data.get('hunger', 100) - 10)
            data['energy'] = max(0, data.get('energy', 100) - 10)
            data['health'] = max(0, data.get('health', 100) - 5)
            # Счётчики действий не уменьшаем — они накапливаются

def init_pet(user_id):
    if user_id not in pets:
        pets[user_id] = {
            'hunger': 100,
            'energy': 100,
            'health': 100,
            'actions': {'chicken': 0, 'meat': 0, 'water': 0, 'sleep': 0, 'heal': 0}  # Счётчики нажатий
        }

# import asyncio
# from config import TIME_INTERVAL, DECREASE_PARAMS

# # Словарь для хранения данных питомцев (user_id: stats)
# pets = {}

# # Фоновая задача для уменьшения параметров
# async def background_task():
#     while True:
#         await asyncio.sleep(TIME_INTERVAL)
#         for user_id, pet in pets.items():
#             for param, decrease in DECREASE_PARAMS.items():
#                 if param in pet:
#                     pet[param] = max(0, pet[param] + decrease)  # Уменьшаем, но не ниже 0
#         print(f"Параметры уменьшены для {list(pets.keys())}")




# import asyncio
# from config import TIME_INTERVAL, DECREASE_PARAMS

# # Словарь для хранения данных питомцев (user_id: stats)
# pets = {}

# # Фоновая задача для уменьшения параметров каждые TIME_INTERVAL секунд
# async def background_task():
#     while True:
#         await asyncio.sleep(TIME_INTERVAL)
#         for user_id, pet in pets.items():
#             for param, decrease in DECREASE_PARAMS.items():
#                 if param in pet:
#                     pet[param] = max(0, pet[param] + decrease)  # Уменьшаем, но не ниже 0
#         print("Параметры уменьшены")
#         print(f"Параметры уменьшены для {list(pets.keys())}")




# import asyncio
# from config import TIME_INTERVAL, DECREASE_PARAMS
# from db import pets  # Это рекурсивный импорт? Нет, это просто словарь, но лучше импортировать в handlers.py напрямую.

# # Словарь для хранения данных питомцев (user_id: stats)
# pets = {}

# Фоновая задача для уменьшения параметров каждые TIME_INTERVAL секунд
# async def background_task():
#     while True:
#         await asyncio.sleep(TIME_INTERVAL)
#         for user_id, pet in pets.items():
#             for param, decrease in DECREASE_PARAMS.items():
#                 if param in pet:
#                     pet[param] = max(0, pet[param] + decrease)  # Уменьшаем, но не ниже 0
#         print("Параметры уменьшены")
#         print(f"Параметры уменьшены для {list(pets.keys())}")










# import asyncio

# # Словарь для хранения питомцев (в памяти, для простоты)
# pets = {}

# async def background_task():
#     while True:
#         await asyncio.sleep(10)  # Каждые 10 секунд
#         for user_id, pet in pets.items():
#             pet['hunger'] = max(0, pet['hunger'] - 5)
#             pet['energy'] = max(0, pet['energy'] - 5)
#             pet['happiness'] = max(0, pet['happiness'] - 5)
#             pet['health'] = max(0, pet['health'] - 2)  # Здоровье тоже уменьшается со временем
#             print(f"Параметры уменьшены для {user_id}")  # Лог в терминале






# pets = {} # База данных нашего бота(словарь).  # Пустой словарь для хранения питомцев (ключ: user_id, значение: {'name': ..., 'energy': ..., etc.})