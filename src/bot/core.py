import discord
from discord.ext import commands
from src.utils.config import Config
from src.ai.gemini_client import GeminiClient
from src.utils.logger import bot_logger

class NexusBot(commands.Bot):
    def __init__(self):
        # Botun temel yetkilerini (Intents) tanımlıyoruz
        intents = discord.Intents.default()
        intents.message_content = True  # Mesajları okuyabilmek için şart
        
        super().__init__(command_prefix="!", intents=intents)
        self.ai_client = GeminiClient()  # GeminiClient'i burada başlatıyoruz
        self.logger = bot_logger

    async def setup_hook(self):
        self.logger.info("System modules are being loaded...")
        try:
            await self.load_extension("src.bot.cogs.chat")
            await self.load_extension("src.bot.cogs.image")
            self.logger.info("All extensions loaded successfully.")
        except Exception as e:
            self.logger.error(f"Failed to load extension: {e}")

    async def on_ready(self):
        self.logger.info(f'Logged in as {self.user.name} (ID: {self.user.id})')