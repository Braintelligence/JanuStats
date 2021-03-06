#!/bin/sh
# this is a very simple script that tests the docker configuration for JanuStats
# it is meant to be run from the root directory of the repository, eg:
# sh tests/test_docker.sh

# install test requirements
# pip install -r requirements/local.txt

# FOSSA
curl -H 'Cache-Control: no-cache' https://raw.githubusercontent.com/fossas/fossa-cli/master/install.sh | sudo bash
fossa

# run the project's tests
docker-compose -f local.yml run django python manage.py pytest

# return non-zero status code if there are migrations that have not been created
docker-compose -f local.yml run django python manage.py makemigrations --dry-run --check || { echo "ERROR: there were changes in the models, but migration listed above have not been created and are not saved in version control"; exit 1; }

# Test support for translations
docker-compose -f local.yml run django python manage.py makemessages
