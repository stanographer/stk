# syntax=docker/dockerfile:1
FROM python:3.8-slim-buster
LABEL MAINTAINER="STK, Stanley Sakai <stanley@stanographer.com>"
ENV GROUP_ID=1000  \
    GROUP_NAME=app \
    USER_ID=1000   \
    USERNAME=stkrooty
WORKDIR /home/app
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY . /home/app
RUN addgroup --gid "$GROUP_ID" "$GROUP_NAME"
RUN adduser "$USERNAME" --uid "$USER_ID" --ingroup "$GROUP_NAME" --disabled-password --shell /bin/sh
USER "$USERNAME"
EXPOSE 3001
CMD ["python3", "-m" , "flask", "run", "--host=0.0.0.0"]
