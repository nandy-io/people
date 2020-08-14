VERSION?=0.1
INSTALL=klotio/sqlalchemy:0.2
TILT_PORT=26580
TTY=$(shell if tty -s; then echo "-it"; fi)
VOLUMES=-v ${PWD}/package/:/opt/service/package \
		-v ${PWD}/setup.py:/opt/service/setup.py
ENVIRONMENT=-e PYTHONDONTWRITEBYTECODE=1 \
			-e PYTHONUNBUFFERED=1
.PHONY: up down verify tag untag

up:
	mkdir -p config
	echo "- op: add\n  path: /spec/template/spec/volumes/0/hostPath/path\n  value: $(PWD)/config" > tilt/config.yaml
	kubectx docker-desktop
	tilt --port $(TILT_PORT) up

down:
	kubectx docker-desktop
	tilt down

verify:
	docker run $(TTY) $(VOLUMES) $(ENVIRONMENT) $(INSTALL) sh -c "cp -r /opt/service /opt/install && cd /opt/install/ && python setup.py install && python -m nandyio_people_integrations && python -m nandyio_people_unittest"

tag:
	-git tag -a "v$(VERSION)" -m "Version $(VERSION)"
	git push origin --tags

untag:
	-git tag -d "v$(VERSION)"
	git push origin ":refs/tags/v$(VERSION)"
