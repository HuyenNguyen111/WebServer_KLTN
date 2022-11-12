FROM python:3.8

ENV PYTHONUNBUFFERED 1

RUN mkdir /code
WORKDIR /code
ADD . /code/
RUN cd /code/
RUN apt update -y && apt install python3-dev \
                          gcc \
                          libc-dev \
                          libffi-dev gunicorn -y
RUN pip3 install -r requirements.txt
RUN ls
CMD exec gunicorn webserver.wsgi:application --bind 0.0.0.0:8000 --workers 3 
