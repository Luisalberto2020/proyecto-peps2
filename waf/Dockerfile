FROM ubuntu:20.04
RUN apt update
RUN DEBIAN_FRONTEND=noninteractive apt install -y apache2
RUN apt install -y libapache2-mod-security2
RUN a2enmod security2
RUN service apache2 restart
COPY modsecurity.conf /etc/modsecurity/modsecurity.conf
RUN service apache2 restart
RUN mkdir /etc/apache2/modsecurity-crs/
COPY coreruleset-3.3.0/ /etc/apache2/modsecurity-crs/
RUN service apache2 restart

RUN DEBIAN_FRONTEND=noninteractive apt-get -y install libapache2-mod-evasive
COPY evasive.conf /etc/apache2/mods-enabled/evasive.conf
RUN mkdir /var/log/mod_evasive && chown www-data:www-data /var/log/mod_evasive
RUN service apache2 restart
EXPOSE 80
CMD ["apachectl", "-D", "FOREGROUND"]