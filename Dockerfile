# syntax=docker/dockerfile:1
FROM python:slim-buster

RUN apt-get update \
&& apt-get install gcc -y \
&& apt-get clean

ARG NB_USER=jovyan
ARG NB_UID=1000
ENV USER ${NB_USER}
ENV NB_UID ${NB_UID}
ENV HOME /home/${NB_USER}

ENV PATH="/home/jovyan/.local/bin:${PATH}"

RUN adduser --disabled-password \
    --gecos "Default user" \
    --uid ${NB_UID} \
    ${NB_USER}

# Make sure the contents of our repo are in ${HOME}
USER root
RUN chown -R ${NB_UID} ${HOME}
USER ${NB_USER}

RUN pip install --pre netket
RUN pip install --no-cache-dir notebook==5.*
RUN pip install --no-cache-dir jupyterhub

WORKDIR . ${HOME}/crc183_summer_school_2021/
COPY . . 

ENTRYPOINT []
