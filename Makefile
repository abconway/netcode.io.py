all: install

clean:
	rm -rf venv

develop: venv install
	venv/bin/pip install -e .[dev]

install:
	pip install -e .

lint:
	venv/bin/flake8 netcode

run:
	venv/bin/honcho start

test:
	venv/bin/pytest tests

venv:
	virtualenv venv -p $(shell which python3)
