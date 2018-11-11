migrate:
	@python manage.py migrate

run:
	@python manage.py runserver 0.0.0.0:8000

migrations:
	@python manage.py makemigrations

clean:
	@find . -name "*.pyc" -delete

dev_deps:
	@pip install -r ../requirements/local.txt

prod_deps:
	@pip install -r ../requirements/production.txt

dev_enviroment:
	@make dev_deps
	@make migrate

prod_enviroment:
	@make prod_deps
	@make migrate
