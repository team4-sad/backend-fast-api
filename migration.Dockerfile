FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .

# Устанавливаем системные зависимости
RUN apt-get update && apt-get install -y cron && apt-get clean

# Устанавливаем Python-зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Копируем приложение
COPY . /app

# Интервал (в минутах)
ENV INTERVAL_MINUTES=10

# Создаем стартовый скрипт, который запускает задачу напрямую в цикле
RUN echo '#!/bin/bash\n\
while true; do\n\
    /usr/local/bin/python /app/migration.py\n\
    echo "Migration completed at $(date)"\n\
    sleep ${INTERVAL_MINUTES}m\n\
done' > /app/start.sh

RUN chmod +x /app/start.sh

CMD ["/bin/bash", "/app/start.sh"]