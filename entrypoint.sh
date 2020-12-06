python manage.py makemigrations answer
python manage.py makemigrations question
python manage.py migrate
gunicorn -b 0.0.0.0:8000 askwer.wsgi:application
