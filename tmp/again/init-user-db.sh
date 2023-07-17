#!/bin/bash
set -e

psql -v ON_ERROR_STOP=1 --username postgres --dbname postgres <<-EOSQL
	CREATE USER crm_tables;
	CREATE DATABASE crm_tables;
	GRANT ALL PRIVILEGES ON DATABASE crm_tables TO postgres;
EOSQL
pg_restore -c -U postgres -d crm_tables -v "tmp/plain_dump.sql" -W