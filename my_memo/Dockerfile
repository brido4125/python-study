FROM python:3.8-slim

COPY . /app

RUN pip3 install flask

RUN pip3 install pymongo

RUN pip3 install uuid

WORKDIR /app

CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0"]