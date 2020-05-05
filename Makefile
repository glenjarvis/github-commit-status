.PHONY: clean clean-test clean-pyc clean-build docs help
.DEFAULT_GOAL := help
SHELL := /bin/bash

define PRINT_HELP_PYSCRIPT
import re, sys

for line in sys.stdin:
	match = re.match(r'^([a-zA-Z_-]+):.*?## (.*)$$', line)
	if match:
		target, help = match.groups()
		print("%-20s %s" % (target, help))
endef
export PRINT_HELP_PYSCRIPT


define BROWSER_PYSCRIPT
import os, webbrowser, sys
try:
	from urllib import pathname2url
except:
	from urllib.request import pathname2url

webbrowser.open("file://" + pathname2url(os.path.abspath(sys.argv[1])))
endef
export BROWSER_PYSCRIPT
BROWSER := python -c "$$BROWSER_PYSCRIPT"

DOCKER_VERSION = latest

help:
	@python -c "$$PRINT_HELP_PYSCRIPT" < $(MAKEFILE_LIST)

clean: clean-build clean-pyc clean-test ## remove all build, test, coverage and Python artifacts

clean-build: ## Remove build artifacts
	rm -fr build/
	rm -fr dist/
	rm -fr .eggs/
	find . -name '*.egg-info' -exec rm -fr {} +
	find . -name '*.egg' -exec rm -f {} +

clean-containers: ## Remove all docker containers
	docker container ls -a  | cut -d' ' -f 1  | grep -v CONTAINER | xargs docker container rm

clean-images: ## Clean github_commit_status images
	# Please help me learn how to DRY this up
	docker image rm glenjarvis/github_commit_status:${DOCKER_VERSION} || true
	docker image rm glenjarvis/github_commit_status:py-3.5.9-${DOCKER_VERSION} || true
	docker image rm glenjarvis/github_commit_status:py-3.6.10-${DOCKER_VERSION} || true
	docker image rm glenjarvis/github_commit_status:py-3.7.7-${DOCKER_VERSION} || true
	docker image ls -a | grep none| awk '{print $$3}' | xargs docker image rm

clean-pyc: ## remove Python file artifacts
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +

clean-test: ## remove test and coverage artifacts
	rm -fr .tox/
	rm -f .coverage
	rm -fr htmlcov/
	rm -fr .pytest_cache

docker_setup:
	docker-compose build
	
docker-build-all: docker_setup  ## Build docker images for all supported versions

intra-container-test:  ## Tests from inside our docker containers
	poetry env list --full-path | cut -d' ' -f1 > /tmp/python_base
	`cat /tmp/python_base`/bin/python tests/test_github_commit_status.py

image: docker_setup  ## Build docker image

lint: ## check style with flake8
	flake8 github_commit_status tests

reqs: ## Update all requirements
	poetry update
	poetry export --without-hashes -f requirements.txt -o requirements.txt
	poetry export --without-hashes --dev -f requirements.txt -o requirements_dev.txt
	poetry show --tree > requirements_graph.txt

test: ## run tests quickly with the default Python
	python tests/test_github_commit_status.py

test-all: ## Run tests in all containers
	# TODO: Please help me learn to make this more DRY
	docker-compose build
	docker run --rm -it github_commit_status:latest /bin/bash -c 'make intra-container-test'
	docker run --rm -it github_commit_status:py-3.5.9-latest /bin/bash -c 'make intra-container-test'
	docker run --rm -it github_commit_status:py-3.6.10-latest /bin/bash -c 'make intra-container-test'
	docker run --rm -it github_commit_status:py-3.7.7-latest /bin/bash -c 'make intra-container-test'

tag:
	if [ -z $${VERSION+x} ]; then echo "make tag VERSION=<<version>>"; exit 1; fi
	git tag -s v$(VERSION) -m 'Release $(VERSION)'

coverage: ## check code coverage quickly with the default Python
	coverage run --source github_commit_status python tests/test_github_commit_status.py
	coverage report -m
	coverage html

run: ## Build docker image and run it
	# TODO: Break out so that we don't have to build all images to run
	docker-compose up
	# TODO: Please help me get past need to manually type 'poetry shell'
	echo "At prompt ==> poetry shell"
	docker run -it github_commit_status bash

git-hook:
	cp githooks/pre-commit  .git/hooks/
	echo "Git hook installed."

git-hooks: git-hook

hook-go-away:
	rm .git/hooks/pre-commit || true
	echo "Git hook is gone. You can commit now."

hooks-go-away: hook-go-away

docs: ## generate Sphinx HTML documentation, including API docs
	@echo "+ $@"
	@rm -f docs/github_commit_status.rst
	@sphinx-apidoc -o docs/ github_commit_status
	@rm -f docs/modules.rst
	@$(MAKE) -C docs clean
	@$(MAKE) -C docs html
	@$(BROWSER) docs/_build/html/index.html

servedocs: docs ## compile the docs watching for changes
	watchmedo shell-command -p '*.rst' -c '$(MAKE) -C docs html' -R -D .

release: dist ## package and upload a release
	twine upload dist/*

dist: clean ## builds source and wheel package
	poetry build
	ls -l dist

install: clean ## install the package to the active Python's site-packages
	poetry install

