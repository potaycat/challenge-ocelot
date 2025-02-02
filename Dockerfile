ARG PYTHON_VERSION=3.12-slim-bullseye

FROM python:${PYTHON_VERSION}

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir -p /code

WORKDIR /code

COPY requirements.txt /tmp/requirements.txt
RUN set -ex && \
    pip install --upgrade pip && \
    pip install -r /tmp/requirements.txt uvicorn && \
    rm -rf /root/.cache/
COPY . /code

EXPOSE 8000

CMD ["gunicorn", "--worker-class=uvicorn.workers.UvicornWorker", "--bind=:8000", "--workers=2", "ocelot.asgi"]
