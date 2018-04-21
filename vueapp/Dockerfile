FROM node:7.4-alpine

RUN  mkdir /code
WORKDIR /code
COPY ./vueapp/package*.json ./
RUN npm install
COPY ./vueapp /code/
