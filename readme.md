# Docker

 ## Using Docker Compose

    docker compose up -d
    docker compose exec web python manage.py migrate
    docker compose exec web python manage.py test


## Create superuser to login

    docker compose exec -it web python manage.py createsuperuser


## Take it down

    docker compose down


Note: docker compose is configured to use docker volume. This will persist between `docker up` and `docker down` and docker down commands.
