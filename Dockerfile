FROM python:3.9.7-slim

#work dir
WORKDIR /app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV USE_CUDA 0
ENV USE_ROCM 0

# install dependencies
RUN pip install --upgrade pip
RUN pip install --pre torch --index-url https://download.pytorch.org/whl/nightly/cpu

COPY ./requirements.txt .

RUN pip install -r requirements.txt

#copy the proejct files
COPY . .

EXPOSE 8000

CMD [ "gunicorn", "--bind", "0.0.0.0:8000" ,"models_gateway.wsgi"]