#stage 1 solo compila el proyecto de angular
FROM node:latest as node
WORKDIR /app
COPY . .
RUN npm install -g @angular/cli@15.0.1
RUN npm install
RUN ng build --configuration production


#stage 2
FROM httpd:2.4.51-alpine
COPY --from=node /app/dist/angular /usr/local/apache2/htdocs/
COPY .htaccess /usr/local/apache2/htdocs/
#COPY httpd.config /usr/local/apache2/conf/httpd.conf
RUN service httpd restart
