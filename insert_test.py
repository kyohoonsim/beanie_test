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


async def insert():
    await initiate_database()

    son = Player(name="손흥민", back_num=7)
    hwang = Player(name="황희찬", back_num=11)
    lee = Player(name="이강인", back_num=19)

    await son.insert()
    await hwang.insert()
    await lee.insert()


if __name__ == '__main__':
    asyncio.run(insert())

