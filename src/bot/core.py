import discord
from discord.ext import commands
from src.utils.config import Config
from src.ai.gemini_client import GeminiClient

class NexusBot(commands.Bot):
    def __init__(self):
        # Botun temel yetkilerini (Intents) tanımlıyoruz
        intents = discord.Intents.default()
        intents.message_content = True  # Mesajları okuyabilmek için şart
        
        super().__init__(command_prefix="!", intents=intents)
        self.ai_client = GeminiClient()  # GeminiClient'i burada başlatıyoruz

    async def setup_hook(self):
        print("Sistem modülleri yükleniyor...")
        await self.load_extension("src.bot.cogs.chat")
        await self.load_extension("src.bot.cogs.image") # Bu satırı ekledik!

    async def on_ready(self):
        """Bot başarıyla bağlandığında tetiklenir."""
        print(f'Giriş yapıldı: {self.user.name} (ID: {self.user.id})')
        print('------')