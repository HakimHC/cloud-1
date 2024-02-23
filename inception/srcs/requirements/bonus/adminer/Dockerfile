FROM alpine:3.18.3

RUN apk update && apk add       wget \
                                php-fpm \
                                php-session \
                                php-mysqli \
                                mariadb-client 

COPY conf/php-fpm.conf /etc/php81/php-fpm.d/www.conf

COPY tools tools
RUN chmod +x ./tools/setup.sh

CMD ["./tools/setup.sh"]
