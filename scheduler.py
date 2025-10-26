from config import DECREASE_PARAMS as dpar, TIME_INTERVAL
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.interval import IntervalTrigger

from db import get_pets_list, update_pet

scheduler = AsyncIOScheduler()

def start_scheduler():
    scheduler.add_job(decrease_params, trigger=IntervalTrigger(seconds=TIME_INTERVAL))
    scheduler.start()

async def decrease_params(): # Функция которая изменяет наши параметры
    pets_list = await get_pets_list()
    if not pets_list:
        return None
    
    for pet in pets_list: # Значения - это словарик с нашими питомцами вычитаем значения
        hun = pet['hunger'] + dpar['hunger']
        en = pet['energy'] + dpar['energy']
        hap = pet['happiness'] + dpar['happiness']

# Отфильтровали значения по максимуму минимуму
        hun = max(min(hun, 100) ,0)
        en = max(min(en, 100) ,0)
        hap = max(min(hap, 100) ,0)
# записали в словарь новые значения
        pet['hunger'] = hun
        pet['energy'] = en
        pet['happiness'] = hap

        await update_pet(
            user_id=pet["user_id"],
            name=pet["name"],
            hunger=pet["hunger"],
            happiness=pet["happiness"],
            energy=pet["energy"]
        )
       