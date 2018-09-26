all: install


develop: install
	pip install -e .[dev]

install:
	pip install -e .

lint:
	flake8 netcode

test:
	pytest tests
