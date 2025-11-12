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

help:
	@python -c "$$PRINT_HELP_PYSCRIPT" < $(MAKEFILE_LIST)

clean: clean-build clean-pyc clean-test ## remove all build, test, coverage and Python artifacts

clean-build: ## Remove build artifacts
	rm -fr build/
	rm -fr dist/
	rm -fr .eggs/
	find . -name '*.egg-info' -exec rm -fr {} +
	find . -name '*.egg' -exec rm -f {} +

clean-pyc: ## remove Python file artifacts
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +

clean-test: ## remove test and coverage artifacts
	rm -f .coverage
	rm -fr htmlcov/
	rm -fr .pytest_cache

lint: ## check style with pylint and black
	pylint github_commit_status tests
	black --check --line-length=80 github_commit_status tests

black: ## reformat code with black at 80 characters
	black --line-length=80 github_commit_status tests

reqs: ## Update all requirements with pip-compile
	pip-compile --upgrade pyproject.toml -o requirements/requirements.txt
	pip-compile --upgrade pyproject.toml --extra dev -o requirements/development.txt
	pip list --format=freeze > requirements/freeze.txt

test: ## run tests quickly with the default Python
	python tests/test_github_commit_status.py

tag:
	if [ -z $${VERSION+x} ]; then echo "make tag VERSION=<<version>>"; exit 1; fi
	git tag -s v$(VERSION) -m 'Release $(VERSION)'

coverage: ## check code coverage quickly with the default Python
	coverage run --source github_commit_status python tests/test_github_commit_status.py
	coverage report -m
	coverage html

git-hook:
	cp githooks/pre-commit  .git/hooks/
	echo "Git hook installed."

git-hooks: git-hook

hook-go-away:
	rm .git/hooks/pre-commit || true
	echo "Git hook is gone. You can commit now."

hooks-go-away: hook-go-away

docs: ## generate MkDocs HTML documentation
	@echo "+ $@"
	mkdocs build
	@$(BROWSER) site/index.html

servedocs: ## serve the docs watching for changes
	mkdocs serve

release: dist ## package and upload a release
	twine upload dist/*

dist: clean ## builds source and wheel package
	python -m build
	ls -l dist

install: ## install the package in editable mode for development
	pip install -e ".[dev]"

