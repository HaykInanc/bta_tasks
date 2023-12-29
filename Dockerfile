# Используйте официальный образ Python
FROM python:3.8

# Устанавливаем зависимости
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Копируем код в контейнер
COPY ./ ./

# Устанавливаем переменные окружения, если необходимо
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

# Запускаем приложение
CMD ["flask", "run"]
