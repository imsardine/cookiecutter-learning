FROM python:3.12.4

WORKDIR /workspace

COPY tox.ini ./
RUN apt-get update && apt-get install -y --no-install-recommends \
        vim \
    && pip install tox==4.16.0 \
    && tox --notest --workdir /tmp/tox && rm tox.ini

CMD ["bash"]
