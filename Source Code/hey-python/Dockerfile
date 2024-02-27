FROM python:3-alpine3.15

RUN apk update && apk add --no-cache build-base python3-dev py3-pip

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 3000

CMD ["python", "./index.py"]
