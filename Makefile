MIGRATION_NAME ?= ''


run:
	python manage.py runserver --noreload
migrations:
	python manage.py makemigrations
migrate:
	python manage.py migrate
migrations-snippets:
	python manage.py makemigrations snippets
migrate-snippets:
	python manage.py migrate snippets
superuser:
# python manage.py createsuperuser
	python manage.py createsuperuser --username admin --email admin@root.com
shell:
	python manage.py shell
collstatic:
	python manage.py collectstatic
clean:
	rm -f db.sqlite3 && rm -r snippets/migrations