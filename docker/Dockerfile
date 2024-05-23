FROM python:3.11.7-bookworm

WORKDIR /app

RUN pip install --upgrade pip "poetry==1.8.2"

COPY ../poetry.lock pyproject.toml ./

RUN poetry config virtualenvs.create false --local

RUN poetry install

ADD ../mus /app
ADD ../docker /app/docker

RUN mkdir -p /app/media
RUN  chmod a+x ./docker/runserver.sh

