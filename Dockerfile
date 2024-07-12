FROM python:3.9.7-slim

RUN pip install -U pip

COPY requirements.txt /tmp/requirements.txt

RUN pip install -r /tmp/requirements.txt

WORKDIR /app

COPY [ "flask_app.py", "functions.py", "./" ]

EXPOSE 9696

ENTRYPOINT [ "gunicorn", "--bind=0.0.0.0:9696", "flask_app:app" ]