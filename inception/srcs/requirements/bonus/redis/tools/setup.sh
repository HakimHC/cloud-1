#! /bin/sh

print_log() {
  echo "[ REDIS ]: $1"
}

print_log "Starting redis server..."
redis-server /etc/redis.conf
