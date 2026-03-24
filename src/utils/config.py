import os
from dotenv import load_dotenv

# .env dosyasındaki verileri yükle
load_dotenv()

class Config:
    """Proje genelindeki ayarların yönetildiği sınıf."""
    DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
    
    # Hata kontrolü: Anahtarlar yoksa sistemi durdur
    @classmethod
    def validate(cls):
        if not cls.DISCORD_TOKEN or not cls.GEMINI_API_KEY:
            raise ValueError("HATA: .env dosyasında API anahtarları eksik!")

# Ayarları doğrula
Config.validate()