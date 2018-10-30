MAKEFLAGS=--warn-undefined-variables

# Parameters
-include Makefile.credentials
-include Makefile.settings
TEST ?= tests/
TEST_ENVS ?=
TEST_MARK ?=

# Internal Variables
docker_image = learning-{{cookiecutter.topic_slug}}.local
docker_opts =
pytest_opts = -vvv -o log_cli=true

ifneq ($(TEST_MARK),)
  pytest_opts += -m '$(TEST_MARK)'
endif

define docker_run
	docker run --rm -it \
	  --volume $(PWD):/workspace \
	  --volume $(PWD)/tmp:/tmp \
	  $(docker_opts) \
	  $(docker_image) $(1)
endef

setup:
	docker build -t $(docker_image) .
	$(call docker_run,tox --notest)

shell: docker_opts += --volume ~/.vimrc:/root/.vimrc
shell:
	$(call docker_run,)

test: docker_opts += --env TEST=$(TEST)
test: docker_opts += --env TOXENV=$(TEST_ENVS)
test: docker_opts += --env PYTEST_OPTS="$(pytest_opts)"
test:
	$(call docker_run,tox)

clean:
	git clean -Xdf
