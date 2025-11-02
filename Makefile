#!/bin/bash

lint:
	uv run pre-commit run --all-files

test:
	cd src && python -m pytest ../tests/

test-v:
	cd src && python -m pytest ../tests/ -vv

migrate:
	cd src && python manage.py migrate

makemigrations:
	cd src && python manage.py makemigrations

shell:
	cd src && python manage.py shell

runserver:
	cd src && python manage.py runserver

seed:
	cd src && python manage.py seed_all

seed-users:
	cd src && python manage.py seed_users

seed-companies:
	cd src && python manage.py seed_companies

seed-clear:
	cd src && python manage.py seed_all --clear

