import discord
from discord.ext import commands
import PIL.Image
import io
import aiohttp
from src.ai.gemini_client import GeminiClient

class ImageCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.ai = GeminiClient()

    @commands.command(name="bak")
    async def analyze_image(self, ctx, *, soru: str = "Bu görselde ne görüyorsun?"):
        """Görseli analiz eder. Kullanım: Fotoğraf yükle + Mesaj kısmına !bak [soru]"""
        
        # Mesajda ek (attachment) var mı kontrol et
        if not ctx.message.attachments:
            await ctx.send("Lütfen analiz etmem için bir fotoğraf yükle!")
            return

        attachment = ctx.message.attachments[0]
        
        # Sadece resim dosyalarını kabul et
        if not any(attachment.filename.lower().endswith(ext) for ext in ['png', 'jpg', 'jpeg', 'webp']):
            await ctx.send("Lütfen geçerli bir resim formatı (png, jpg, webp) kullan.")
            return

        async with ctx.typing():
            try:
                # Resmi indir
                async with aiohttp.ClientSession() as session:
                    async with session.get(attachment.url) as resp:
                        if resp.status != 200:
                            return await ctx.send("Resim indirilirken bir hata oluştu.")
                        data = io.BytesIO(await resp.read())
                        img = PIL.Image.open(data)

                # Gemini'ye hem resmi hem soruyu gönder
                # Not: Gemini 1.5 Flash modeli hem resmi hem metni aynı anda işleyebilir.
                response = self.ai.model.generate_content([soru, img])
                await ctx.reply(response.text)

            except Exception as e:
                print(f"Görsel Analiz Hatası: {e}")
                await ctx.send("Görseli işlerken bir sorun oluştu.")

async def setup(bot):
    await bot.add_cog(ImageCog(bot))