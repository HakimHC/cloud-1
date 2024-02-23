#! /bin/sh

print_log() {
  echo "[ VSFTPD ]: $1"
}

check_user() {
  id "$1" >/dev/null 2>&1
}

if ! check_user "$VSFTPD_USER"; then
        print_log "Creating FTP user..."
        adduser -h $WORDPRESS_DIR hakim >/dev/null 2>&1 << EOF
$VSFTPD_PASSWORD
$VSFTPD_PASSWORD
EOF
fi

echo "$VSFTPD_USER"|tee -a /etc/vsftpd.userlist > /dev/null

chown -R nobody:nogroup $WORDPRESS_DIR
chown -R "$VSFTPD_USER":"$VSFTPD_USER" $WORDPRESS_DIR

print_log "Starting FTP server..."
vsftpd
