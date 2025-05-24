import asyncio
from aiogram import Bot, Dispatcher
from settings.token import BOT_TOKEN
from handlers import routers


async def main():
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()

    for router in routers:
        dp.include_router(router)

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
