FROM alpine:3.18.3

RUN apk update && apk add redis

COPY tools tools
RUN chmod +x ./tools/setup.sh

COPY conf/redis.conf /etc/redis.conf

CMD ["./tools/setup.sh"]
