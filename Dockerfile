FROM python:3.9.7-slim

USER dev1

COPY requirements.txt /tmp/requirements.txt

RUN pip install --user -r /tmp/requirements.txt

WORKDIR /app

COPY [ "flask_app.py", "./" ]

EXPOSE 9696

ENTRYPOINT [ "gunicorn", "--bind=0.0.0.0:9696", "simple_web:app" ]