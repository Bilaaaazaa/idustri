FROM python:3.10-buster

RUN mkdir -p /usr/src/app

WORKDIR /usr/src/app

COPY requirements.txt /usr/src/app

RUN pip install --no-cache-dir -r requirements.txt

COPY . /usr/src/app

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]