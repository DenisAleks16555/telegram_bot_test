from config import DECREASE_PARAMS as dpar, TIME_INTERVAL
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.interval import IntervalTrigger
from db import pets, background_task  # Добавили background_task из db.py
import asyncio  # Добавлено для совместимости с APScheduler и create_task

scheduler = AsyncIOScheduler()

def start_scheduler():
    # Запуск APScheduler задачи
    scheduler.add_job(decrease_params, trigger=IntervalTrigger(seconds=TIME_INTERVAL))
    scheduler.start()
    
    # ДОБАВЛЕНО: Параллельный запуск background_task (если хотим обе версии; иначе удалить эту строку)
    asyncio.create_task(background_task())

async def decrease_params():
    print("Параметры уменьшены")  # Для проверки: печатает каждые TIME_INTERVAL секунд
    for pet in pets.values():
        hun = pet['hunger'] + dpar['hunger']  # Например, -5
        en = pet['energy'] + dpar['energy']    # Например, -5
        hap = pet['happiness'] + dpar['happiness']  # Например, -5
        hea = pet['health'] + (-2)  # ДОБАВЛЕНО: Уменьшение здоровья на -2 (как в background_task)
        
        # Ограничения (исправлено: hun для голода, en для энергии)
        hun = max(min(hun, 100), 0)
        en = max(min(en, 100), 0)
        hap = max(min(hap, 100), 0)
        hea = max(min(hea, 100), 0)  # ДОБАВЛЕНО: Ограничения для здоровья
        
        # Запись
        pet['hunger'] = hun
        pet['energy'] = en
        pet['happiness'] = hap
        pet['health'] = hea  # ДОБАВЛЕНО
    # Сохранение (если нужно)
    # save_pets_to_db(pets)  # Расскомментируй, если добавишь функцию






# from config import DECREASE_PARAMS as dpar, TIME_INTERVAL
# from apscheduler.schedulers.asyncio import AsyncIOScheduler
# from apscheduler.triggers.interval import IntervalTrigger
# from db import pets  # Убедись, что db.py импортирует pets как dict


# scheduler = AsyncIOScheduler()

# def start_scheduler():
#     scheduler.add_job(decrease_params, trigger=IntervalTrigger(seconds=TIME_INTERVAL))
#     scheduler.start()

# async def decrease_params():
#     print("Параметры уменьшены")  # Для проверки: печатает каждые TIME_INTERVAL секунд
#     for pet in pets.values():
#         hun = pet['hunger'] + dpar['hunger']
#         en = pet['energy'] + dpar['energy']
#         hap = pet['happiness'] + dpar['happiness']
#         # Ограничения
#         hun = max(min(hun, 100), 0)
#         en = max(min(en, 100), 0)
#         hap = max(min(hap, 100), 0)
#         # Запись
#         pet['hunger'] = hun
#         pet['energy'] = en
#         pet['happiness'] = hap
    # Сохранение (если нужно)
    # save_pets_to_db(pets)  # Раскомментируй, если добавишь функцию





# from config import DECREASE_PARAMS as dpar, TIME_INTERVAL
# from apscheduler.schedulers.asyncio import AsyncIOScheduler
# from apscheduler.triggers.interval import IntervalTrigger

# from db import pets

# scheduler = AsyncIOScheduler()

# def start_scheduler():
#     scheduler.add_job(decrease_params, trigger=IntervalTrigger(seconds=TIME_INTERVAL))
#     scheduler.start()

# async def decrease_params(): # Функция которая изменяет наши параметры
#     for pet in pets.values(): # Значения - это словарик с нашими питомцами вычитаем значения
#         hun = pet['hunger'] + dpar['hunger']
#         en = pet['energy'] + dpar['energy']
#         hap = pet['happiness'] + dpar['happiness']

# # Отфильтровали значения по максимуму минимуму
#         hun = max(min(hun, 100) ,0)
#         en = max(min(en, 100) ,0)
#         hap = max(min(hap, 100) ,0)
# # записали в словарь новые значения
#         pet['hunger'] = hun
#         pet['energy'] = en
#         pet['happiness'] = hap
       