FROM node:18.17.0-alpine as build-stage

WORKDIR /app

COPY package*.json ./
RUN npm install -g npm@10.2.5 -g
RUN npx npm install

COPY . .

RUN npx npm run build
#RUN npm run dev
#RUN npx npm run dev

FROM nginx:1.21-alpine

COPY --from=build-stage /app/dist /usr/share/nginx/html

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
