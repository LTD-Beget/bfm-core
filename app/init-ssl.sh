#!/usr/bin/with-contenv bash
set -e

cd /app/nginx/certs

if [ -s sprutio.key -a -s sprutio.crt ]; then
    exit 0
fi

openssl req -nodes -newkey rsa:4096 -keyout sprutio.key -out sprutio.csr -subj "/C=RU/O=Beget/CN=sprut.io"
openssl x509 -req -days 365 -in sprutio.csr -signkey sprutio.key -out sprutio.crt

chmod 700 ../certs
chmod 400 sprutio.key
