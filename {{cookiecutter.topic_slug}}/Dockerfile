FROM python:3.7.0

WORKDIR /workspace

COPY tox.ini ./
RUN apt-get update && apt-get install -y --no-install-recommends \
        python2.7-dev \
        vim \
    && pip install tox==3.9.0 \
    && tox --notest --workdir /tmp/tox && rm tox.ini

CMD ["bash"]