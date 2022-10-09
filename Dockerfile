FROM python:3.9-alpine

WORKDIR /usr/src

COPY ./requirements.txt ./

RUN apk add build-base

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

WORKDIR /usr/src/app

# todo 0.0.0.0으로 했을 때 문제는 없는지? CORS 등등
ENTRYPOINT ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000","--reload"]
