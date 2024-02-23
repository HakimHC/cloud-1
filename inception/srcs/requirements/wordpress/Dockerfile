FROM alpine:3.18.3

COPY . /app

WORKDIR /app

RUN chmod +x ./tools/setup.sh

RUN apk update && apk add curl \
                         php-fpm \
                         php-phar \
                         php-mysqli \
                         mariadb-client \
                         php-mbstring \
                         php-session

COPY ./conf/php-fpm.conf /etc/php81/php-fpm.d/www.conf

CMD ["./tools/setup.sh"]
