#! /bin/sh

print_log() {
  echo "[ NGINX ]: $1"
}

if [ ! -f $PRIVKEY_PATH ]; then
        openssl genpkey -algorithm RSA -out $PRIVKEY_PATH > /dev/null 2>&1
        print_log "Private key generated."
fi

if [ ! -f $CERT_PATH ]; then
        openssl req -new -x509 -key $PRIVKEY_PATH -out $CERT_PATH -days 365 > /dev/null 2>&1 << EOF 
$COUNTRY
$PROVINCE
$LOCALITY
$ORGANIZATION
$UNIT
$COMMON_NAME
$EMAIL_ADDR
EOF
        print_log "TLS certificate generated."
fi

sed -i "s~\$CERT_PATH~$CERT_PATH;~g" /etc/nginx/nginx.conf
sed -i "s~\$PRIVKEY_PATH~$PRIVKEY_PATH;~g" /etc/nginx/nginx.conf

print_log "Starting wordpress' NGINX webserver..."

nginx
