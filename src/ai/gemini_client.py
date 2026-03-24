from google import genai
from src.utils.config import Config

class GeminiClient:
    def __init__(self):
        self.client = genai.Client(api_key=Config.GEMINI_API_KEY)
        self.chat_sessions = {}

    async def get_chat_response(self, user_id: str, prompt: str) -> str:
        """Kullanıcının geçmişini hatırlayarak yanıt üretir."""
        try:
            if user_id not in self.chat_sessions:
                self.chat_sessions[user_id] = []

            self.chat_sessions[user_id].append(
                {"role": "user", "parts": [{"text": prompt}]}
            )

            response = self.client.models.generate_content(
                model="gemini-2.5-flash",
                contents=self.chat_sessions[user_id]
            )

            reply_text = response.text if getattr(response, "text", None) else "Yanıt alınamadı."

            self.chat_sessions[user_id].append(
                {"role": "model", "parts": [{"text": reply_text}]}
            )

            return reply_text

        except Exception as e:
            print(f"AI Chat Error: {e}")
            return "Hafıza yönetimi sırasında bir hata oluştu."