FROM python:3.11-slim-bullseye
RUN apt update
RUN apt install -qy git

# ENV PYTHONPATH=/src
WORKDIR /src

ADD $project_name $project_name

