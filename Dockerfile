FROM python:3.10-slim

RUN apt-get update \ 
    && apt-get install -y gcc postgresql-server-dev-all

ADD . /app

WORKDIR /app

RUN pip install --upgrade pip \ 
    && pip install -r requirements.txt

EXPOSE 5000

CMD ["python", "app.py"]