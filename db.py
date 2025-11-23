import aiosqlite
from typing import Optional, Dict

DATABASE_FILE = 'pets.db'

async def init_db():
    async with aiosqlite.connect(DATABASE_FILE) as db:
        await db.execute('''
            CREATE TABLE IF NOT EXISTS pets (
                user_id INTEGER PRIMARY KEY,
                hunger INTEGER DEFAULT 100,
                energy INTEGER DEFAULT 100,
                health INTEGER DEFAULT 100
            )
        ''')
        await db.commit()
        print("Таблица pets создана/проверена.")  # Для проверки в терминале

async def init_pet(user_id: int):
    async with aiosqlite.connect(DATABASE_FILE) as db:
        await db.execute('INSERT OR IGNORE INTO pets (user_id, hunger, energy, health) VALUES (?, 100, 100, 100)', (user_id,))
        await db.commit()

async def get_pet(user_id: int) -> Optional[Dict[str, int]]:
    async with aiosqlite.connect(DATABASE_FILE) as db:
        cursor = await db.execute('SELECT hunger, energy, health FROM pets WHERE user_id = ?', (user_id,))
        row = await cursor.fetchone()
        if row:
            return {'hunger': row[0], 'energy': row[1], 'health': row[2]}
        return None

async def update_pet(user_id: int, hunger: Optional[int] = None, energy: Optional[int] = None, health: Optional[int] = None):
    async with aiosqlite.connect(DATABASE_FILE) as db:
        if hunger is not None:
            await db.execute('UPDATE pets SET hunger = ? WHERE user_id = ?', (hunger, user_id))
        if energy is not None:
            await db.execute('UPDATE pets SET energy = ? WHERE user_id = ?', (energy, user_id))
        if health is not None:
            await db.execute('UPDATE pets SET health = ? WHERE user_id = ?', (health, user_id))
        await db.commit()

async def decrease_all_stats():
    async with aiosqlite.connect(DATABASE_FILE) as db:
        # Правильный SQL: CASE для min=0 (работает во всех SQLite)
        await db.execute('''
            UPDATE pets 
            SET 
                hunger = CASE WHEN hunger - 5 < 0 THEN 0 ELSE hunger - 5 END,
                energy = CASE WHEN energy - 5 < 0 THEN 0 ELSE energy - 5 END,
                health = CASE WHEN health - 5 < 0 THEN 0 ELSE health - 5 END
        ''')
        await db.commit()














# import sqlite3
# import aiosqlite  # Добавил для async
# from typing import Optional, Dict

# DATABASE_FILE = 'pets.db'

# async def init_db():
#     """Инициализация базы данных и создание таблицы, если она не существует."""
#     async with aiosqlite.connect(DATABASE_FILE) as db:
#         await db.execute('''
#             CREATE TABLE IF NOT EXISTS pets (
#                 user_id INTEGER PRIMARY KEY,
#                 hunger INTEGER DEFAULT 100,
#                 energy INTEGER DEFAULT 100,
#                 health INTEGER DEFAULT 100
#             )
#         ''')
#         await db.commit()

# async def init_pet(user_id: int):
#     """Создание нового питомца для пользователя."""
#     async with aiosqlite.connect(DATABASE_FILE) as db:
#         await db.execute('INSERT OR IGNORE INTO pets (user_id, hunger, energy, health) VALUES (?, 100, 100, 100)', (user_id,))
#         await db.commit()

# async def get_pet(user_id: int) -> Optional[Dict[str, int]]:
#     """Получение данных питомца по user_id."""
#     async with aiosqlite.connect(DATABASE_FILE) as db:
#         cursor = await db.execute('SELECT hunger, energy, health FROM pets WHERE user_id = ?', (user_id,))
#         row = await cursor.fetchone()
#         if row:
#             return {'hunger': row[0], 'energy': row[1], 'health': row[2]}
#         return None

# async def update_pet(user_id: int, hunger: Optional[int] = None, energy: Optional[int] = None, health: Optional[int] = None):
#     """Обновление stats питомца."""
#     async with aiosqlite.connect(DATABASE_FILE) as db:
#         if hunger is not None:
#             await db.execute('UPDATE pets SET hunger = ? WHERE user_id = ?', (hunger, user_id))
#         if energy is not None:
#             await db.execute('UPDATE pets SET energy = ? WHERE user_id = ?', (energy, user_id))
#         if health is not None:
#             await db.execute('UPDATE pets SET health = ? WHERE user_id = ?', (health, user_id))
#         await db.commit()

# async def decrease_all_stats():
#     """Уменьшение stats всех питомцев каждые 60 секунд."""
#     async with aiosqlite.connect(DATABASE_FILE) as db:
#         await db.execute('UPDATE pets SET hunger = MAX(hunger - 5, 0), energy = MAX(energy - 5, 0), health = MAX(health - 5, 0)')
#         await db.commit()



















# import sqlite3
# import asyncio
# from typing import Optional, Dict

# DATABASE_FILE = 'pets.db'

# def init_db():
#     """Инициализация базы данных и создание таблицы, если она не существует."""
#     conn = sqlite3.connect(DATABASE_FILE)
#     cursor = conn.cursor()
#     cursor.execute('''
#         CREATE TABLE IF NOT EXISTS pets (
#             user_id INTEGER PRIMARY KEY,
#             hunger INTEGER DEFAULT 100,
#             energy INTEGER DEFAULT 100,
#             health INTEGER DEFAULT 100
#         )
#     ''')
#     conn.commit()
#     conn.close()

# async def init_pet(user_id: int):
#     """Создание нового питомца для пользователя."""
#     conn = sqlite3.connect(DATABASE_FILE) 
#     cursor = conn.cursor()
#     cursor.execute('INSERT OR IGNORE INTO pets (user_id, hunger, energy, health) VALUES (?, 100, 100, 100)', (user_id,))
#     conn.commit()
#     conn.close()

# async def get_pet(user_id: int) -> Optional[Dict[str, int]]:
#     """Получение данных питомца по user_id."""
#     conn = sqlite3.connect(DATABASE_FILE)
#     cursor = conn.cursor()
#     cursor.execute('SELECT hunger, energy, health FROM pets WHERE user_id = ?', (user_id,))
#     row = cursor.fetchone()
#     conn.close()
#     if row:
#         return {'hunger': row[0], 'energy': row[1], 'health': row[2]}
#     return None

# async def update_pet(user_id: int, hunger: Optional[int] = None, energy: Optional[int] = None, health: Optional[int] = None):
#     """Обновление stats питомца."""
#     conn = sqlite3.connect(DATABASE_FILE)
#     cursor = conn.cursor()
#     if hunger is not None:
#         cursor.execute('UPDATE pets SET hunger = ? WHERE user_id = ?', (hunger, user_id))
#     if energy is not None:
#         cursor.execute('UPDATE pets SET energy = ? WHERE user_id = ?', (energy, user_id))
#     if health is not None:
#         cursor.execute('UPDATE pets SET health = ? WHERE user_id = ?', (health, user_id))
#     conn.commit()
#     conn.close()

# async def decrease_all_stats():
#     """Уменьшение stats всех питомцев каждые 60 секунд."""
#     conn = sqlite3.connect(DATABASE_FILE)
#     cursor = conn.cursor()
#     cursor.execute('UPDATE pets SET hunger = MAX(hunger - 5, 0), energy = MAX(energy - 5, 0), health = MAX(health - 5, 0)')
#     conn.commit()
#     conn.close()







# import asyncio
# from collections import defaultdict

# pets = defaultdict(dict)  # Словарь для хранения данных питомцев по user_id

# async def background_task():
#     while True:
#         await asyncio.sleep(60)  # Каждые 60 секунд
#         for user_id, data in pets.items():
#             # Уменьшаем stats
#             data['hunger'] = max(0, data.get('hunger', 100) - 10)
#             data['energy'] = max(0, data.get('energy', 100) - 10)
#             # Изменения для health (расширение из прошлого задания)
#             health_change = 5  # Обычное уменьшение
#             if data.get('energy', 100) < 50:  # Если энергия низкая
#                 health_change += 5  # Дополнительное уменьшение
#             data['health'] = max(0, data.get('health', 100) - health_change)
#             # Счётчики действий не уменьшаем — они накапливаются


# def init_pet(user_id):
#     if user_id not in pets:
#         pets[user_id] = {
#             'hunger': 100,
#             'energy': 100,
#             'health': 100,
#             'actions': {'chicken': 0, 'meat': 0, 'water': 0, 'sleep': 0, 'heal': 0},  # Счётчики нажатий
#             'games_played': 0,  # Общий счётчик игр (новый)
#             'tennis_games': 0,  # Счётчик для тенниса (новый)
#             'puzzle_games': 0,  # Счётчик для пазлов (новый)
#             'target_games': 0    # Счётчик для цели (новый)
#         }

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