# pull official base image
FROM python:3.8.0-alpine

# set work directory
WORKDIR /usr/src/verticals

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install thrirdparty libraries dependencies
RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev
RUN apk add build-base python-dev py-pip jpeg-dev zlib-dev
ENV LIBRARY_PATH=/lib:/usr/lib

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt /usr/src/verticals/requirements.txt
RUN pip install -r requirements.txt

# copy project
COPY . /usr/src/verticals/

# run entrypoint.sh
ENTRYPOINT ["/usr/src/verticals/entrypoint.sh"]