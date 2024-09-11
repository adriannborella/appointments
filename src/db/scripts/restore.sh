export PGPASSWORD=desarrollo

dropdb -U aborella -h 127.0.0.1 db_develop
createdb -U aborella -h 127.0.0.1 db_develop
psql -U aborella -h 127.0.0.1 db_develop < backup.sql
