#!/usr/bin/env bash
set -o errexit
#cd myproject-when cd
pip install -r requirements.txt
python manage.py collectstatic --no-input
python manage.py create_deploy_superuser || true
python manage.py migrate
