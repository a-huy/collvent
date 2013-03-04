#!/bin/sh

# Empty the database so if you need to run the filler script it
# won't give you any errors (like entires already existing)
psql -d collvent  -c '
TRUNCATE accounts_user RESTART IDENTITY CASCADE;
TRUNCATE events_place RESTART IDENTITY CASCADE;'
