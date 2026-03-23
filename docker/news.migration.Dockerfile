FROM python:3.12-slim

WORKDIR /app

COPY ../requirements.txt .

# Установка системных зависимостей (cron)
RUN apt-get update && apt-get install -y cron && apt-get clean

# Установка Python-зависимостей
RUN pip install --no-cache-dir -r requirements.txt

# Копирование исходного кода
COPY .. /app

# Переменная окружения для интервала (по умолчанию 10 минут)
ENV INTERVAL_MINUTES=10

# Создаём пустой файл лога (для tail)
RUN touch /var/log/cron.log

CMD ["sh", "-c", "echo \"*/${INTERVAL_MINUTES} * * * * cd /app && PYTHONPATH=/app /usr/local/bin/python /app/migration/news.py --config /app/.env >> /var/log/cron.log 2>&1\" > /etc/cron.d/news-migration && chmod 0644 /etc/cron.d/news-migration && crontab /etc/cron.d/news-migration && cron && tail -f /var/log/cron.log"]