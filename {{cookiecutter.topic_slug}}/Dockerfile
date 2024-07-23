FROM {{ cookiecutter.base_image }}

WORKDIR /workspace
ENV PATH $PATH:/root/.local/bin

COPY tox.ini ./
RUN apt-get update && apt-get install -y --no-install-recommends \
        vim \
        python3 \
        pipx \
    && pipx install tox==4.16.0 \
    && tox --notest --workdir /tmp/tox && rm tox.ini

CMD ["bash"]
