# Ticketing system

Practice project for a ticketing system using Django and database in postgres. 

## Docker

 ### Using Docker Compose

```bash
docker compose up -d
docker compose exec web python manage.py migrate
docker compose exec web python manage.py test
```

### Create superuser to login

```bash
docker compose exec -it web python manage.py createsuperuser
```

### Take it down

```bash
docker compose down
```

Note: docker compose is configured to use docker volume. This will persist between `docker up` and `docker down` commands.
