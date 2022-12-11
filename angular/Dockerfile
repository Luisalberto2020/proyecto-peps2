#stage 1 solo compila el proyecto de angular
FROM node:latest as node
WORKDIR /app
RUN npm install -g @angular/cli@15.0.1
COPY package.json .
RUN npm install
COPY . .
RUN ng build --configuration production


#stage 2
FROM nginx
COPY --from=node /app/dist/angular /usr/share/nginx/html
COPY ./nginx.conf  /etc/nginx/conf.d/default.conf
