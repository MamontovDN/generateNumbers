FROM python:3.8.5
WORKDIR /code
COPY requirements.txt /code
RUN pip install -r requirements.txt
COPY . /code
CMD  daphne -b 0.0.0.0 -p 8000 mysite.asgi:application
