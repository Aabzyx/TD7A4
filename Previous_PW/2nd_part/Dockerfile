FROM python:latest
COPY . /app
WORKDIR /app

Run pip install --upgrade pip
Run pip install -r requirements.txt

EXPOSE 5000

CMD ["python", "app.py"]