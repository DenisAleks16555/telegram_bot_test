FOOD_PARAMS = {
    'Курица': {'hunger': 20, 'health': 5},
    'Мясо': {'hunger': 30, 'health': 10},
    'Вода': {'hunger': 5, 'health': 0},
}

SLEEP_PARAMS = {'energy': 50, 'health': 10}
HEAL_PARAMS = {'health': 40}

START_STATS = {'hunger': 100, 'energy': 100, 'health': 100}
DECREASE_RATE = 5







# import os
# from dotenv import load_dotenv


# load_dotenv()
# BOT_TOKEN = os.getenv("TG_API_KEY")

# TIME_INTERVAL = 10 # Отвечает за интервал уменьшения показателей в секундах

# DECREASE_PARAMS = {
#     "hunger": -5, # параметр голод
#     "energy": -3, # параметр энергия
#     "happiness": -1, # параметр счастья
# }

# FOOD_PARAMS = {
#     'курица': {'hunger': 20, 'energy': 5},
#     'стейк': {'hunger': 25, 'energy': 10},
#     'яблоко': {'hunger': 10, 'happiness': 10},
#     'мясо': {'hunger': 20, 'energy': 5},
#     'хлеб': {'hunger': 15},
#     'печенье': {'hunger': 10, 'happiness': 15},
#     'вода': {'hunger': 5, 'health': 5}
# }