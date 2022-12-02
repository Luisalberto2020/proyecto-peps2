#stage 1 solo compila el proyecto de angular
FROM node:latest as node
WORKDIR /app
COPY . .
RUN npm install
RUN npm run build --prod


#stage 2
FROM httpd:2.4.51-alpine
COPY --from=node /app/dist/angular /usr/local/apache2/htdocs/