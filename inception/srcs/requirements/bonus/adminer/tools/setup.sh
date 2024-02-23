#! /bin/sh

print_log() {
  echo "[ ADMINER ]: $1"
}

check_user() {
  id "$1" >/dev/null 2>&1
}

if [ ! -d "/adminer/adminer" ]; then
	mkdir -p /adminer/adminer
	print_log "Creating /adminer directory..."
fi

if [ ! -f "/adminer/adminer/index.php" ]; then
        print_log "Downloading adminer files..."
        wget --quiet -O /adminer/adminer/index.php \
        https://github.com/vrana/adminer/releases/download/v4.8.1/adminer-4.8.1.php
fi

if ! check_user "$ADMINER_USER"; then
        print_log "Creating ADMINER user..."
        adduser -h /adminer hakim >/dev/null 2>&1 << EOF
$ADMINER_PASSWORD
$ADMINER_PASSWORD
EOF
fi

chown -R nobody:nogroup /adminer
chown -R "$ADMINER_USER":"$ADMINER_USER" /adminer

sed -i "s/\$ADMINER_USER/$ADMINER_USER/" /etc/php81/php-fpm.d/www.conf

print_log "Adminer is ready!"

php-fpm81 --nodaemonize
