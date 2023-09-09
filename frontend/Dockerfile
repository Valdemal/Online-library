FROM node:latest AS build

WORKDIR /usr/src/frontend

COPY . .

RUN npm install

CMD npm run build