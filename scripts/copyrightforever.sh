#!/bin/bash
NAME="copyright_dev_server"
DJANGODIR=/home/dev/project/Backend-Copyrightforever/src
VENVPATH=/home/dev/.cache/pypoetry/virtualenvs/backend-copyrightforever--UqOecWW-py3.11
SOC=//127.0.0.1:3005  # we will communicte using this unix socket
USER=dev                                        # the user to run as
GROUP=dev                                     # the group to run as
NUM_WORKERS=3                                     # how many worker processes s>
DJANGO_SETTINGS_MODULE=copyrightforever.settings  # which settings file >
DJANGO_WSGI_MODULE=copyrightforever.wsgi

echo "Starting $NAME as `whoami`"

# Activate the virtual environment
cd $VENVPATH
source ./bin/activate
cd $DJANGODIR
export DJANGO_SETTINGS_MODULE=$DJANGO_SETTINGS_MODULE
export PYTHONPATH=$DJANGODIR:$PYTHONPATH
export DJANGO_READ_DOT_ENV_FILE=True

exec gunicorn ${DJANGO_WSGI_MODULE}:application \
  --name $NAME \
  --workers $NUM_WORKERS \
  --user=$USER --group=$GROUP \
  --bind=127.0.0.1:3005 \
  --log-level=debug \
  --log-file=/home/dev/project/logs/copyrightforever_dev.log
