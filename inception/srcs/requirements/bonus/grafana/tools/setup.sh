#! /bin/sh

print_log() {
  echo "[ GRAFANA ]: $1"
}

check_connection() {
  mysql -u $MYSQL_USER -p$MYSQL_PASSWORD -h $MYSQL_HOST -e "SELECT 1;" 2>/dev/null
}

while true; do
  print_log "Trying to connect to MYSQL..."
  if check_connection >/dev/null 2>&1; then
    break
  fi
  sleep 1
done


print_log "Trying to connect to MYSQL..."
print_log "Starting Grafana server..."
grafana-server --config=/etc/grafana/grafana.ini --homepath=/usr/share/grafana > /dev/null 2>&1
