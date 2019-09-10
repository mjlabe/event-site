#!/bin/bash
set -e

psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" <<-EOSQL
    CREATE USER user with password 'eventspassword';
    CREATE DATABASE ev_db;
    GRANT ALL PRIVILEGES ON DATABASE events TO user;
EOSQL
