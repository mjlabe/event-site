#!/bin/sh

./wait-for.sh db echo Database Ready && \
  python manage.py migrate && \
  python manage.py collectstatic --noinput && \
  python create_su.py | python manage.py shell && \
  gunicorn events.wsgi:application --bind 0.0.0.0:8000 --workers 3
