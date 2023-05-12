FROM python:3.7-slim-buster

RUN apt-get -y update && apt-get -y install gcc

WORKDIR /app

COPY requirements.txt .

RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . .

CMD ["python", "src/tg-channel-to-rss.py"]