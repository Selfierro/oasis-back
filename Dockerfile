# Используем более новую версию Python
FROM python:3.11-slim

# Устанавливаем переменные окружения
ENV PYTHONUNBUFFERED=1

# Устанавливаем зависимости
RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y \
        git \
        libpq-dev \
        libxslt-dev \
        libxml2-dev \
        libpam-dev \
        libedit-dev \
        tk-dev \
        tcl-dev \
        libcurl4-openssl-dev \
        curl \
        libssl-dev \
        nginx \
        supervisor && \
    rm -rf /var/lib/apt/lists/*

# Создаем рабочую директорию
RUN mkdir /code
WORKDIR /code

# Конфигурируем nginx
RUN echo "daemon off;" >> /etc/nginx/nginx.conf
COPY production/docker_nginx.conf /etc/nginx/sites-available/default

# Конфигурируем Supervisor
COPY production/docker_supervisor.conf /etc/supervisor/conf.d/

# Устанавливаем зависимости Python
ADD requirements/base.txt /code/requirements/base.txt
RUN pip install --no-cache-dir -r requirements/base.txt

# Копируем код приложения
ADD . /code/

# Открываем порты
EXPOSE 80
EXPOSE 443

# Запускаем Supervisor
CMD ["supervisord", "-n"]
