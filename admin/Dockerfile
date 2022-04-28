FROM python:3.9
ENV PYTHONUNBUFFERED 1
WORKDIR /app
COPY admin/requirements.txt /app/requirements.txt
RUN pip3 install -r requirements.txt
COPY /admin/ /app

