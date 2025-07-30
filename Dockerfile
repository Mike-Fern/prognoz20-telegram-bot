FROM python:3.10-slim

# Установка зависимостей системы
RUN apt-get update && apt-get install -y build-essential gcc

# Установка зависимостей Python
WORKDIR /app
COPY . /app
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Запуск бота
CMD ["python", "main.py"]
