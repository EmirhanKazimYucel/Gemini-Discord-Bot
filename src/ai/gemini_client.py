from google import genai
from src.utils.config import Config
from src.utils.logger import bot_logger

class GeminiClient:
    def __init__(self):
        # Yeni SDK yapısı ile client başlatma
        self.client = genai.Client(api_key=Config.GEMINI_API_KEY)
        # Her kullanıcı için ayrı bir sohbet oturumu tutan sözlük
        self.chat_sessions = {}
        # Kullanılacak model ismi
        self.model_id = "gemini-2.5-flash"

    def _get_or_create_session(self, user_id: str):
        """Kullanıcıya özel sohbet oturumunu döndürür veya yeni oluşturur."""
        if user_id not in self.chat_sessions:
            # SDK'nın kendi chat yönetimini kullanmak daha güvenli ve kolaydır
            self.chat_sessions[user_id] = self.client.chats.create(model=self.model_id)
            bot_logger.info(f"New AI session created for user: {user_id}")
        return self.chat_sessions[user_id]

    async def get_chat_response(self, user_id: str, prompt: str) -> str:
        """Kullanıcının geçmişini hatırlayarak yanıt üretir."""
        try:
            # Oturumu al
            chat = self._get_or_create_session(user_id)
            
            # Mesajı gönder ve yanıtı al
            response = chat.send_message(prompt)
            
            # Yanıt kontrolü
            if response and response.text:
                bot_logger.info(f"AI successfully responded to user {user_id}")
                return response.text
            else:
                bot_logger.warning(f"Empty response received for user {user_id}")
                return "AI yanıt üretemedi, lütfen tekrar deneyin."

        except Exception as e:
            bot_logger.error(f"AI Chat Error for user {user_id}: {str(e)}")
            return "Üzgünüm, şu an teknik bir sorun nedeniyle yanıt veremiyorum."

    async def analyze_image(self, user_id: str, prompt: str, image_data):
        """Görsel analizi yapar (Vision yeteneği)."""
        try:
            # Görsel analizinde genellikle geçmişe bakılmaz, tekil işlem yapılır
            response = self.client.models.generate_content(
                model=self.model_id,
                contents=[prompt, image_data]
            )
            bot_logger.info(f"Image analysis completed for user {user_id}")
            return response.text
        except Exception as e:
            bot_logger.error(f"AI Vision Error for user {user_id}: {str(e)}")
            return "Görseli analiz ederken bir hata oluştu."