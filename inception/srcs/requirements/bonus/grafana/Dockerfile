FROM alpine:3.18.3

RUN apk update && apk add grafana mariadb-client

COPY tools tools
RUN chmod +x ./tools/setup.sh

COPY ./conf/grafana.ini /etc/grafana/grafana.ini

CMD ["./tools/setup.sh"]
