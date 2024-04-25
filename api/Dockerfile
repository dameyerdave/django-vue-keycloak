FROM python:3.11-bookworm

# Optimise python and debian in docker
ENV PYTHONUNBUFFERED 1
ENV PIP_BREAK_SYSTEM_PACKAGES 1
ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV DEBIAN_FRONTEND noninteractive

# Update pip
RUN pip install --upgrade pip

# Global python requirements
COPY ./requirements.txt /
RUN pip install -r /requirements.txt

# COPY ./app /app

WORKDIR /app

ENTRYPOINT [ "/app/entrypoint.sh" ]