.DEFAULT_GOAL = .venv

PATH ::= .venv/bin:${PATH}

.venv: pyproject.toml
	python3 -m venv --system-site-packages .venv
	.venv/bin/pip install poetry poethepoet
	poetry install
	touch .venv

lint: | .venv
	poe lint

test: | .venv
	poe test

debug: | .venv
	poe test --pdb

serve: | .venv
	poe serve

.PHONY: serve test lint debug
