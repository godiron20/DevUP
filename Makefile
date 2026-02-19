SHELL := /bin/bash

all: migration-upgrade run_api

.PHONY: requirements
requirements: pyproject.toml
	poetry lock
	poetry install --no-root


.PHONY: migration-generate
migration-generate: requirements
	poetry run alembic revision --autogenerate -m "$(ARGS)"


.PHONY: migration-upgrade
migration-upgrade: requirements
	poetry run alembic upgrade head


.PHONY: run_api
run_api: requirements
	poetry run python starter.py

.PHONY: starter_db
starter_db:
	./docker_start.sh
