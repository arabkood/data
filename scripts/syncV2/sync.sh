#!/bin/bash

export DB_HOST="192.168.1.69"
export DB_PORT="5432"
export DB_USER="postgres"
export DB_PASSWORD="admin"
export DB_NAME="arabkood_3"
export DB_SSLMODE="disable"
export DATABASE_URL="postgres://$DB_USER:$DB_PASSWORD@$DB_HOST:$DB_PORT/$DB_NAME?sslmode=$DB_SSLMODE"

pnpm run sync
