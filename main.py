from aiogram import Bot, Dispatcher
import asyncio 
from config import BOT_TOKEN
from handlers import register_handlers
from scheduler import start_scheduler



async def main():
    try:
        start_scheduler()
        print("Фоновые задачи запущены")

        bot = Bot(token=BOT_TOKEN)
        dp = Dispatcher()
        
        # Убрал await — register_handlers не async
        await register_handlers(dp)

        print("Бот запущен...")
        await dp.start_polling(bot)
    except Exception as e:
        print(f"Ошибка при запуске бота: {e}")  # Это поможет увидеть ошибку в терминале

if __name__ == "__main__":
    asyncio.run(main())











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