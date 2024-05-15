PROJECT_NAME = $(shell basename $(CURDIR))
DOCKER_IMAGE = $(PROJECT_NAME)
DOCKER_IMAGE_FULL = $(DOCKER_IMAGE):latest
GITHUB_DOCKER = docker.pkg.github.com/$(shell echo ${GITHUB_REPOSITORY} | tr A-Z a-z)/$(DOCKER_IMAGE_FULL)

# For GitHub CI
export DOCKER_BUILDKIT = 1

.PHONY: build
build:
	docker build --pull -t $(DOCKER_IMAGE_FULL) --build-arg project_name=$(PROJECT_NAME) .


.PHONY: bash
bash:
	docker run -it --rm $(DOCKER_IMAGE_FULL) bash


.PHONY: run
run:
	docker run --rm -e API_KEY $(DOCKER_IMAGE_FULL) python -m $(PROJECT_NAME).main


.PHONY: build_with_github
build_with_github_cache:
	docker build --pull -t $(DOCKER_IMAGE_FULL) --build-arg BUILDKIT_INLINE_CACHE=1 --cache-from=$(GITHUB_DOCKER) --build-arg project_name=$(PROJECT_NAME) .

.PHONY: push
push:
	docker tag $(DOCKER_IMAGE_FULL) $(GITHUB_DOCKER)
	docker push $(GITHUB_DOCKER)

