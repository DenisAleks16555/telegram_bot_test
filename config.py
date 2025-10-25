import os
from dotenv import load_dotenv


load_dotenv()
BOT_TOKEN = os.getenv("TG_API_KEY")
DB_NAME = "pet_bot.db" 

TIME_INTERVAL = 10 # Отвечает за интервал уменьшения показателей в секундах

DECREASE_PARAMS = {
    "hunger": -5, # параметр голод
    "energy": -3, # параметр энергия
    "happiness": -1, # параметр счастья
}