# 1. Adım: Hafif bir Python imajı kullan
FROM python:3.10-slim

# 2. Adım: Çalışma dizinini oluştur
WORKDIR /app

# 3. Adım: Kütüphane listesini kopyala ve yükle
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. Adım: Tüm proje dosyalarını içeri kopyala
COPY . .

# 5. Adım: Botu çalıştır
CMD ["python", "main.py"]