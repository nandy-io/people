IMAGE=nandyio-people
VERSION?=0.1
ACCOUNT=klotio
NAMESPACE=people-nandy-io
VOLUMES=-v ${PWD}/lib:/opt/nandy-io/lib \
		-v ${PWD}/test:/opt/nandy-io/test \
		-v ${PWD}/setup.py:/opt/nandy-io/setup.py
.PHONY: build shell test install remove reset tag untag

build:
	docker build . -t $(ACCOUNT)/$(IMAGE):$(VERSION)

shell:
	docker run -it $(VOLUMES) $(ENVIRONMENT) $(ACCOUNT)/$(IMAGE):$(VERSION) sh

test:
	docker run -it $(VOLUMES) $(ENVIRONMENT) $(ACCOUNT)/$(IMAGE):$(VERSION) sh -c "coverage run -m unittest discover -v test && coverage report -m --include '*.py'"

setup:
	docker run -it $(VOLUMES) $(ENVIRONMENT) $(ACCOUNT)/$(IMAGE):$(VERSION) sh -c "python setup.py install"


install:
	-kubectl create ns $(NAMESPACE)

remove:
	-kubectl delete ns $(NAMESPACE)

reset: remove instal

tag:
	-git tag -a "v$(VERSION)" -m "Version $(VERSION)"
	git push origin --tags

untag:
	-git tag -d "v$(VERSION)"
	git push origin ":refs/tags/v$(VERSION)"
