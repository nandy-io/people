VERSION?=0.1
TILT_PORT=26580
IMAGE=arm32v7/python:3.8.5-alpine3.12
VOLUMES=-v ${PWD}/module/:/opt/nandy-io/module \
		-v ${PWD}/setup.py:/opt/nandy-io/setup.py
.PHONY: up down setup tag untag

up:
	mkdir -p config
	echo "- op: add\n  path: /spec/template/spec/volumes/0/hostPath/path\n  value: $(PWD)/config" > tilt/config.yaml
	kubectx docker-desktop
	tilt --port $(TILT_PORT) up

down:
	kubectx docker-desktop
	tilt down

setup:
	docker run -it $(VOLUMES) $(IMAGE) sh -c "cd /opt/nandy-io/ && python setup.py install"

tag:
	-git tag -a "v$(VERSION)" -m "Version $(VERSION)"
	git push origin --tags

untag:
	-git tag -d "v$(VERSION)"
	git push origin ":refs/tags/v$(VERSION)"