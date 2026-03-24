import discord
from discord.ext import commands
from src.ai.gemini_client import GeminiClient

class ChatCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        # GeminiClient içindeki get_chat_response metodunu kullanacağız

    @commands.command(name="sor")
    async def ask_gemini(self, ctx, *, soru: str):
        async with ctx.typing():
            # Kullanıcının benzersiz ID'sini gönderiyoruz (Hafıza karışmasın diye)
            user_id = str(ctx.author.id)
            cevap = await self.bot.ai_client.get_chat_response(user_id, soru)
            await ctx.reply(cevap)

async def setup(bot):
    await bot.add_cog(ChatCog(bot))