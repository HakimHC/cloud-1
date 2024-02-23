FROM alpine:3.18.3

RUN apk update && apk add nginx

COPY ./conf/nginx.conf /etc/nginx/nginx.conf
COPY content /static

WORKDIR /static

COPY tools/setup.sh /tmp/setup.sh
RUN chmod +x /tmp/setup.sh

CMD ["/tmp/setup.sh"]
