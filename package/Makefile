IMAGE=module
ACCOUNT=nandyio
DEBUG_PORT=5678
TTY=$(shell if tty -s; then echo "-it"; fi)
VOLUMES=-v ${PWD}/lib:/opt/service/lib \
		-v ${PWD}/test:/opt/service/test
ENVIRONMENT=-e PYTHONDONTWRITEBYTECODE=1 \
			-e PYTHONUNBUFFERED=1

.PHONY: build mysql shell debug test

build:
	docker build . -t $(ACCOUNT)/$(IMAGE)

shell:
	docker run $(TTY) $(VOLUMES) $(ENVIRONMENT) $(ACCOUNT)/$(IMAGE) sh

debug:
	docker run $(TTY) $(VOLUMES) $(ENVIRONMENT) -p 127.0.0.1:$(DEBUG_PORT):5678 $(ACCOUNT)/$(IMAGE) sh -c "python -m ptvsd --host 0.0.0.0 --port 5678 --wait -m unittest discover -v test"

test:
	docker run $(TTY) $(VOLUMES) $(ENVIRONMENT) $(ACCOUNT)/$(IMAGE) sh -c "coverage run -m unittest discover -v test && coverage report -m --include 'lib/*.py'"
