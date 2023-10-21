FROM node:latest AS build

WORKDIR /usr/src/frontend

COPY . .

RUN npm install --force

CMD npm run build