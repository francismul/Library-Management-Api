## Library Management Api
- This is an api made with django and djangorestframework
- It utilizes different technologies such as
- Mysql for database
- Redis for caching
- Django-ratelimit for rate limit (5request/sec)
- Nginx for reverse proxy
- Docker for containerization

## Running the project
- First you need to ensure you have docker on your machine (If not install it)
- There is ton of online resources that showcase how to install docker container for
- different operating systems

- The first command is cloning the repository
- Then cd to the directory
- The first docker command is
- docker-compose build
- on a successfull run
- docker-compose up -d (To run the docker containers)
- now the website is already alive but needs to be configured a little further
- docker-compose exec django_app python manage.py migrate
- docker-compose exec django_app python manage.py collectstatic

- Additional info
- Incase you would want to create a superuser so as to make it easier to log in into admin panel
- docker-compose exec django_app python manage.py createsuperuser
- 
- 
