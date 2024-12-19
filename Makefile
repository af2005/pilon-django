run:
	poetry run python manage.py runserver

test:
	poetry run pytest

black:
	poetry run black .

reset_db:
	poetry run python manage.py reset_db

migrate:
	poetry run python manage.py migrate

migrations:
	poetry run python manage.py makemigrations

linter:
	poetry run flakehell lint

compile_theme:
	sass ./www/static/www/theme.scss ./www/static/www/theme.css
