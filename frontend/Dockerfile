# Используйте образ Node.js для сборки приложения
FROM node:18.17.0-alpine as build-stage

# Установите рабочую директорию
WORKDIR /app

# Копирование зависимостей и установка
COPY package*.json ./
RUN npm install -g npm@10.2.5 -g
RUN npx npm install

# Копирование остальных файлов
COPY . .

# Сборка приложения
RUN npx npm run build
#RUN npm run dev
#RUN npx npm run dev

# Используйте образ Nginx для запуска приложения
FROM nginx:1.21-alpine

# Копирование собранного приложения из предыдущего этапа
COPY --from=build-stage /app/dist /usr/share/nginx/html

# Экспонировать порт 80
EXPOSE 80

# Команда для запуска Nginx
CMD ["nginx", "-g", "daemon off;"]
