FROM python:3

WORKDIR /code

RUN pip install django
RUN pip install djangorestframework
RUN pip install celery
RUN pip install redis
RUN pip install pillow
RUN pip install django-celery-beat
RUN pip install djangorestframework-simplejwt
RUN pip install drf-yasg
RUN pip install eventlet
RUN pip install eventlet
RUN pip install python-dotenv
RUN pip install psycopg2

COPY . .

CMD python manage.py runserver 0.0.0.0:8000