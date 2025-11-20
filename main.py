import asyncio
import logging
import os
from dotenv import load_dotenv  # Если установили python-dotenv
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from handlers import router
from db import background_task, pets

# Загрузка .env
load_dotenv()
BOT_TOKEN = os.getenv('TG_API_KEY')  # Или замените на BOT_TOKEN = 'ваш_реальный_токен'

# Логирование
logging.basicConfig(level=logging.INFO)

# Бот и диспетчер
bot = Bot(token=BOT_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(storage=storage)

# Регистрация роутера
dp.include_router(router)

async def main():
    # Фоновая задача
    task = asyncio.create_task(background_task())
    print("Фоновые задачи запущены")
    
    # Polling
    await dp.start_polling(bot)

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Бот остановлен")
    finally:
        for user_id in list(pets.keys()):
            del pets[user_id]
        print("Данные очищены")


#TG_API_KEY=8476904414:AAGXciy4hJ_kekJm22Go9D6V18Te87fLYqQ


















# import asyncio
# import logging
# import os  # Добавьте этот импорт для os.getenv
# from dotenv import load_dotenv; 
# load_dotenv()

# from aiogram import Bot, Dispatcher
# from aiogram.fsm.storage.memory import MemoryStorage
# from handlers import router  # Импорт роутера из handlers
# from db import background_task, pets

# # Загрузка токена из .env (убедитесь, что .env файл в той же папке с TG_API_KEY=ваш_реальный_токен)
# BOT_TOKEN = os.getenv('TG_API_KEY')  # Замените на это, если .env настроен

# # Если .env не работает, напрямую вставьте токен: BOT_TOKEN = 'ваш_реальный_токен_здесь' (например, '123456:ABC-DEF...')

# # Настройка логирования
# logging.basicConfig(level=logging.INFO)

# # Инициализация бота и диспетчера
# bot = Bot(token=BOT_TOKEN)
# storage = MemoryStorage()
# dp = Dispatcher(storage=storage)

# # Регистрация роутера
# dp.include_router(router)

# async def main():
#     # Запуск фоновой задачи
#     task = asyncio.create_task(background_task())
#     print("Фоновые задачи запущены")
    
#     # Запуск polling
#     await dp.start_polling(bot)

# if __name__ == '__main__':
#     try:
#         asyncio.run(main())
#     except KeyboardInterrupt:
#         print("Бот остановлен")
#     finally:
#         # Очистка
#         for user_id in list(pets.keys()):
#             del pets[user_id]
#         print("Данные очищены")














# import os# Импортировал для BOT_TOKEN
# import asyncio
# import logging
# from aiogram import Bot, Dispatcher
# from aiogram.fsm.storage.memory import MemoryStorage
# from handlers import router  # Импорт роутера из handlers
# from db import background_task, pets

# # Твой токен
# # BOT_TOKEN = 'TG_API_KEY'  # Замени на свой
# BOT_TOKEN = os.getenv("TG_API_KEY")

# bot = Bot(token=BOT_TOKEN)
# dp = Dispatcher()

# # Настройка логирования
# logging.basicConfig(level=logging.INFO)

# # Инициализация бота и диспетчера
# # Три строчки закомментировал
# # bot = Bot(token=BOT_TOKEN)
# # storage = MemoryStorage()
# # dp = Dispatcher(storage=storage)




# # Регистрация роутера
# dp.include_router(router)

# async def main():
#     # Запуск фоновой задачи
#     task = asyncio.create_task(background_task())
#     print("Фоновые задачи запущены")
    
#     # Запуск polling
#     await dp.start_polling(bot)

# if __name__ == '__main__':
#     try:
#         asyncio.run(main())
#     except KeyboardInterrupt:
#         print("Бот остановлен")
#     finally:
#         # Очистка
#         for user_id in list(pets.keys()):
#             del pets[user_id]
#         print("Данные очищены")






# from aiogram import Bot, Dispatcher
# import asyncio 
# from config import BOT_TOKEN
# from handlers import register_handlers
# from scheduler import start_scheduler

# async def main():
#     try:
#         start_scheduler()
#         print("Фоновые задачи запущены")

#         bot = Bot(token=BOT_TOKEN)
#         dp = Dispatcher()
        
#         # Убрал await — register_handlers не async
#         await register_handlers(dp)

#         print("Бот запущен...")
#         await dp.start_polling(bot)
#     except Exception as e:
#         print(f"Ошибка при запуске бота: {e}")  # Это поможет увидеть ошибку в терминале

# if __name__ == "__main__":
#     asyncio.run(main())



















# import asyncio
# from aiogram import Bot, Dispatcher
# from handlers import register_handlers
# from db import pets, background_task  # Предполагаю, что у тебя есть db.py с этими

# # Токен от BotFather
# TOKEN = "YOUR_TOKEN_HERE"  # Замени на свой

# bot = Bot(token=TOKEN)
# dp = Dispatcher()

# click_count = 0  # Глобальный счётчик для Top

# async def main():
#     register_handlers(dp)
#     print("Фоновые задачи запущены")
#     asyncio.create_task(background_task())  # Твоя фоновая задача
#     print("Бот запущен...")
#     await dp.start_polling(bot)

# if __name__ == "__main__":
#     asyncio.run(main())
















# from aiogram import Bot, Dispatcher

# import asyncio 
# from config import BOT_TOKEN
# from handlers import register_handlers
# from scheduler import start_scheduler




# async def main():

#     start_scheduler()
#     print("Фоновые задачи запущены")

#     bot = Bot(token=BOT_TOKEN)
#     dp = Dispatcher()
#     await register_handlers(dp)

#     print("Бот запущен...")
#     await dp.start_polling(bot)
   

# if __name__== "__main__":
#     asyncio.run(main())