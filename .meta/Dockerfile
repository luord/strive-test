FROM python:alpine

WORKDIR /app

ADD ./ ./

RUN pip install . gunicorn

CMD gunicorn -b :$PORT -w 2 'server:create_app()'
