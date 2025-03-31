FROM node:20-alpine

WORKDIR /app

# Установка curl и bash
RUN apk add --no-cache curl bash

# Установка Bun
RUN curl -fsSL https://bun.sh/install | bash && \
    ln -s /root/.bun/bin/bun /usr/local/bin/bun

# Копируем файлы зависимостей
COPY package.json bun.lock ./

# Устанавливаем зависимости
RUN bun install

# Копируем исходный код
COPY . .

# Экспонируем порт Vite (по умолчанию 5173)
EXPOSE 5173

# Запускаем Vite в режиме разработки
CMD ["bun", "run", "dev", "--host", "0.0.0.0", "--port", "5173"]