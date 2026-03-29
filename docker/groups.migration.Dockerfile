FROM python:3.12-slim

WORKDIR /app

COPY ../requirements.txt .

# Установка системных зависимостей (cron)
RUN apt-get update && apt-get install -y cron && apt-get clean

# Установка Python-зависимостей
RUN pip install --no-cache-dir -r requirements.txt

# Копирование исходного кода
COPY .. /app

# Расписание cron (по умолчанию каждое воскресенье в 00:00)
ENV CRON_SCHEDULE="0 0 * * 0"

# Создаём пустой файл лога (для tail)
RUN touch /var/log/cron.log

CMD ["sh", "-c", "\
echo '>>> Run on container start' && \
cd /app && PYTHONPATH=/app /usr/local/bin/python /app/migration/groups.py && \
echo \"${CRON_SCHEDULE} cd /app && PYTHONPATH=/app /usr/local/bin/python /app/migration/groups.py >> /var/log/cron.log 2>&1\" > /etc/cron.d/groups-migration && \
chmod 0644 /etc/cron.d/groups-migration && \
crontab /etc/cron.d/groups-migration && \
cron && \
tail -f /var/log/cron.log"]