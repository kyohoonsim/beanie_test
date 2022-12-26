from beanie import Document, Indexed, init_beanie
from beanie.odm.operators.update.general import Set
import asyncio


class Player(Document):
    name: Indexed(str)
    back_num: int

    class Settings:
        name = "Player"


async def initiate_database():
    await init_beanie(
        connection_string=f"mongodb://root:root@localhost:27017/players?authSource=admin",
        document_models=[Player]
    )


async def delete():
    await initiate_database()

    await Player.find_one(Player.name == "쏘니").delete()


if __name__ == '__main__':
    asyncio.run(delete())

