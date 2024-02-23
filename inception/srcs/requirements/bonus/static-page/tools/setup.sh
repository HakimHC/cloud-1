#! /bin/sh

print_log() {
  echo "[ STATIC-PAGE ]: $1"
}

print_log "Stating NGINX webserver."

nginx
