all: install

install:
	pip install -e .

develop: install
	pip install -r requirements-dev.txt

test:
	pytest
