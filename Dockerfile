FROM python:3.7.5

WORKDIR /app
COPY requirements.txt /app/requirements.txt
RUN pip3 install --upgrade pip
RUN pip install -r requirements.txt

COPY . /app

EXPOSE 5000
CMD gunicorn --worker-class gevent --workers 8 --bind 0.0.0.0:5000 wsgi:app --max-requests 10000 --timeout 5 --keep-alive 5 --log-level info

