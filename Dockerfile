FROM python:3.9-slim-buster

#work dir
WORKDIR /app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip

COPY ./requirements.txt .

RUN pip install -r requirements.txt

#copy the proejct files
COPY . .

EXPOSE 8000

CMD [ "gunicorn", "models_gateway.wsgi"]