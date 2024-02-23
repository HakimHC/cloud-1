FROM alpine:3.18.3

RUN apk update && \
    apk add nginx openssl

RUN mkdir /app && mkdir /www && mkdir /etc/nginx/ssl

WORKDIR /app

COPY tools ./tools
COPY conf/nginx.conf /etc/nginx/nginx.conf

RUN chmod +x tools/setup.sh

EXPOSE 443

ENTRYPOINT ["./tools/setup.sh"]
