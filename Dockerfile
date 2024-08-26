FROM python:3.11-alpine

WORKDIR /src

RUN apk update && apk add --no-cache \
    gcc \
    musl-dev \
    libffi-dev \
    && rm -rf /var/cache/apk/*

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

ENTRYPOINT ["uvicorn", "server:app"]

