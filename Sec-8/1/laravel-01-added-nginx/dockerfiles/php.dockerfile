FROM php:7.4-fpm-apline

WORKDIR /var/www/html

RUN docker-php-ext-install pdo pdo_mysql