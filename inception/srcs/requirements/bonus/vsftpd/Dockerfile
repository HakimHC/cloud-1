FROM alpine:3.18.3

EXPOSE 21

COPY ./conf/vsftpd.conf /etc/vsftpd.conf
COPY ./conf/vsftpd.conf /etc/vsftpd/vsftpd.conf

RUN apk update && apk add vsftpd

COPY ./tools/ tools
RUN chmod +x ./tools/setup.sh

CMD ["./tools/setup.sh"]
