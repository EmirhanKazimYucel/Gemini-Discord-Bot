import logging
import os
from logging.handlers import RotatingFileHandler

def setup_logger():
    # Logların kaydedileceği klasörü oluştur
    if not os.path.exists('data'):
        os.makedirs('data')

    logger = logging.getLogger('GeminiBot')
    logger.setLevel(logging.INFO)

    # Format: Zaman - İsim - Seviye - Mesaj
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    # 1. Dosyaya Kaydetme (Maksimum 5MB, 3 yedek dosya tutar)
    file_handler = RotatingFileHandler('data/bot.log', maxBytes=5*1024*1024, backupCount=3)
    file_handler.setFormatter(formatter)

    # 2. Terminale Basma
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(stream_handler)

    return logger

# Global logger nesnesi
bot_logger = setup_logger()