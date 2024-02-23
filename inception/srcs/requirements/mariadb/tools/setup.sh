#! /bin/sh

print_log() {
  echo "[ MARIADB ]: $1"
}

function add_query_line {
  echo "$1" >> "$MYSQL_INIT_FILE"
}

chown -R mysql: /var/lib/mysql
chmod 777 /var/lib/mysql

mysql_install_db >/dev/null 2>&1

if [ ! -d "/var/lib/mysql/$MYSQL_DATABASE" ]; then
  rm -f "$MYSQL_INIT_FILE"
  add_query_line "CREATE DATABASE $MYSQL_DATABASE;"
  add_query_line "CREATE DATABASE $GRAFANA_DATABASE;"
  add_query_line "CREATE USER $MYSQL_USER@'%' IDENTIFIED BY '$MYSQL_PASSWORD';"
  add_query_line "CREATE USER $MYSQL_USER@'localhost' IDENTIFIED BY '$MYSQL_PASSWORD';"
  add_query_line "GRANT ALL PRIVILEGES ON $MYSQL_DATABASE.* TO $MYSQL_USER@'%' WITH GRANT OPTION;"
  add_query_line "GRANT ALL PRIVILEGES ON $GRAFANA_DATABASE.* TO $MYSQL_USER@'%' WITH GRANT OPTION;"
  add_query_line "GRANT ALL PRIVILEGES ON $MYSQL_DATABASE.* TO $MYSQL_USER@'localhost' WITH GRANT OPTION;"
  add_query_line "FLUSH PRIVILEGES;"
  add_query_line "DROP USER 'root'@'localhost';"
  add_query_line "CREATE USER 'root'@'localhost' IDENTIFIED BY '$MYSQL_ROOT_PASSWORD';"
  add_query_line "GRANT ALL PRIVILEGES ON *.* TO 'root'@'localhost' WITH GRANT OPTION;"
  add_query_line "FLUSH PRIVILEGES;"
  print_log "Starting MariDB server..."
  mysqld_safe --init-file=$MYSQL_INIT_FILE >/dev/null 2>&1
else
  print_log "Starting MariDB server..."
  mysqld_safe >/dev/null 2>&1
fi
