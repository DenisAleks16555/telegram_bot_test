from config import DB_NAME 
import aiosqlite


async def init_db(): # Инициализирует нашу базу данных
    async with aiosqlite.connect(DB_NAME) as db: 
        await db.execute( 
            '''
            CREATE TABLE IF NOT EXISTS pets (
                user_id INTEGER PRIMARY KEY
                name TEXT,
                hunger INTEGER,
                happiness INTEGER,
                energy INTEGER              
            )
            '''
        )

        await db.commit()

async def create_pet(user_id: int, pet_name: str):
    async with aiosqlite.connect(DB_NAME) as db: 
        await db.execute(
            """
            INSERT INTO pets ( user_id,
                name,
                hunger,
                happiness,
                energy)  
            VALUES (?,?,?,?,)           
            """,
            (user_id, pet_name, 50, 50, 50) # Стартовые показатели жизни питомца
        )
        await db.commit()


async def get_pet(user_id: int):
    async with aiosqlite.connect(DB_NAME) as db:# Соединение с базой данных
        async with db.execute("SELECT * FROM pets WHERE pets.user_id = ?", (user_id,)) as cursor:
            pet = await cursor.fetchone() # Получить одну запись
            # pet = (12124, "baks", 50, 34, 12) 
            if not pet:
                return None
            return {
                "user_id": pet[0],
                "name": pet[1],
                "hunger": pet[2],
                "happiness": pet[3],
                "energy": pet[4]  
            }
            