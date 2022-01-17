#!/usr/bin/env bash

# Migrate database
python3 mainsite/manage.py migrate

if [ "$DEBUG" = 'true' ]
then
  # Also install fixtures
  python3 mainsite votingbooth/manage.py loaddata default
fi
