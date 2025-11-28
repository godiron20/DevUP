SHELL := /bin/bash


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


.PHONY: run_uvcorn
run_uvcorn: requirements
	poetry run python src/main.py

.PHONY: starter_db
starter_db:
	./docker_start.sh
