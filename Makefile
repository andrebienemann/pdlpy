# CONFIG

SHELL := /bin/bash
DIR := $(shell pwd)

# DEVELOPMENT & TESTING

.PHONY: venv
venv:
	@ \
	virtualenv -p python3 $(DIR)/venv; \
	source $(DIR)/venv/bin/activate; \
	pip install -e $(DIR)[dev]; \

.PHONY: format
format:
	@ \
	source $(DIR)/venv/bin/activate; \
	isort $(DIR)/pdlpy; \
	black $(DIR)/pdlpy; \
	isort $(DIR)/tests; \
	black $(DIR)/tests; \

.PHONY: test
test:
	@ \
	source $(DIR)/venv/bin/activate; \
	python -B -m coverage run --source $(DIR)/pdlpy -m unittest discover $(DIR)/tests; \

.PHONY: coverage
coverage:
	@ \
	source $(DIR)/venv/bin/activate; \
	coverage report -m; \

# PUBLISHING

.PHONY: publish
publish:
	@ \
	rm -r build && rm -r dist; \
	source $(DIR)/venv/bin/activate; \
	python $(DIR)/setup.py sdist bdist_wheel; \
	twine upload $(DIR)/dist/*; \
