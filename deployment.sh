python3 manage.py migrate
rm -r /var/www/django-restql-playground/static/*
python3 manage.py collectstatic
