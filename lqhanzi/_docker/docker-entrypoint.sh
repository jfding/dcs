#!/bin/sh

if [ -f /settings_staging.py ]; then
    cp /settings_staging.py /src/lqhanzi/project/lqconfig/
fi

pip install -r /src/lqhanzi/requirements.txt

cd /src/lqhanzi/project/
./manage.py makemigrations
./manage.py migrate

./manage.py runscript init_db
./manage.py runscript init_rbac

./manage.py runserver 0.0.0.0:8000
