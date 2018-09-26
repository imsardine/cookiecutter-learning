TEST ?= tests/
TEST_ENVS ?=

docker_image = learning-{{cookiecutter.topic_slug}}.local
docker_opts =

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

shell:
	$(call docker_run)

test: docker_opts += --env TEST=$(TEST)
test: docker_opts += --env TOXENV=$(TEST_ENVS)
test:
	$(call docker_run,tox)

clean:
	git clean -Xdf
