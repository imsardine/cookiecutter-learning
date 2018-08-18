export TEST ?= tests/
export PYTHONDONTWRITEBYTECODE = 1
export TOX_TESTENV_PASSENV = PYTHONDONTWRITEBYTECODE

docker_image = learning-{{cookiecutter.topic_slug}}.local

define docker_run
	docker run --rm -it \
	  --volume $(PWD):/workspace \
	  --env TEST=$(TEST) \
	  $(docker_image) $(1)
endef

run:
	$(call docker_run)

setup:
	docker build -t $(docker_image) .

test:
	$(call docker_run,tox)

test-py2:
	$(call docker_run,tox -e py2)

test-py3:
	$(call docker_run,tox -e py3)
