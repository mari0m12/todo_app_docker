# تأكد أنك تعمل من صورة بايثون الرسمية
FROM python:3.10-slim

# تثبيت أدوات البناء المطلوبة
RUN apt-get update && apt-get install -y \
    build-essential \
    libssl-dev \
    libffi-dev \
    python3-dev \
    gcc \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/*

# نسخ وتثبيت المتطلبات
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# ثم باقي إعدادات الحاوية...
