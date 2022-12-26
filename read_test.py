from beanie import Document, Indexed, init_beanie
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


async def read():
    await initiate_database()
    players = await Player.find({}).to_list()
    
    for player in players:
        print(player.name, player.back_num)


if __name__ == '__main__':
    asyncio.run(read())

