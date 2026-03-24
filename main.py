import asyncio
from src.bot.core import NexusBot
from src.utils.config import Config

async def main():
    bot = NexusBot()
    async with bot:
        await bot.start(Config.DISCORD_TOKEN)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Bot kapatılıyor...")