#!/usr/bin/env bash

# Migrate database
python3 votingbooth/manage.py migrate

if [ "$DEBUG" = 'true' ]
then
  # Also install fixtures
  python3 votingbooth/manage.py loaddata default
fi
