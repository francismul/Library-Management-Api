# Francismul Library Management API Documentation

## Overview

Library Management API is a Django-powered application designed to manage a library of books. It includes features such as book management, user authentication, and rate limiting. This API serves as a backend for library-related operations, leveraging Docker for easy deployment.

## Table of Contents

1. [Directory Structure](#directory-structure)
2. [Requirements](#requirements)
3. [Setup Instructions](#setup-instructions)
4. [Configuration](#configuration)
5. [Endpoints](#endpoints)
6. [Running the Project](#running-the-project)
7. [Management Commands](#management-commands)

---

## Directory Structure

```
francismul-library-management-api/
├── README.md
├── docker-compose.yml
├── mysite/
│   ├── Dockerfile
│   ├── manage.py
│   ├── requirements.txt
│   ├── .dockerignore
│   ├── core/
│   │   ├── admin.py
│   │   ├── models.py
│   │   ├── serializers.py
│   │   ├── urls.py
│   │   ├── views.py
│   │   ├── management/
│   │   │   ├── commands/
│   │   │   │   ├── import_books.py
│   │   │   │   └── import_users.py
│   │   └── migrations/
│   │       ├── 0001_initial.py
│   └── mysite/
│       ├── settings.py
│       └── .env
└── nginx/
    ├── default.conf
    └── Dockerfile
```

## Requirements

To run the application, you need the following:

- Docker
- Docker Compose
- Python 3.11 or above (for local development)
- Django 5.1.7
- Other dependencies are specified in `requirements.txt`.

## Setup Instructions

1. **Clone the repository:**

   ```bash
   git clone <repository_url>
   cd francismul-library-management-api
   ```

2. **Change into the repository directory.**

3. **Set up the Docker environment:**

   - Ensure Docker and Docker Compose are installed on your machine.
   - Adjust any environment variables in the `.env` file under `mysite/mysite/.env` if necessary.

4. **Start the application:**

   ```bash
   docker-compose build
   docker-compose up -d
   ```

5. **Run Important Commands:**

   ```bash
   docker-compose exec django_app python manage.py migrate
   docker-compose exec django_app python manage.py collectstatic
   ```

6. **Access the application:**
   The application will be available at `http://localhost` once all containers have started.

## Configuration

### Environment Variables

The application's configuration is primarily managed via the `.env` file in the `mysite/mysite/` directory. Here are the important variables to configure:

```env
SECRET_KEY=your_secret_key
DEBUG=True
DATABASE_NAME=booksdb
DATABASE_USER=root
DATABASE_HOST=db
DATABASE_PORT=3306
DATABASE_PASSWORD=your_password
DATABASE_ENGINE=django.db.backends.mysql
REDIS_URL_DEFAULT=redis://redis:6379/1
REDIS_URL_SESSION=redis://redis:6379/2
```

### Nginx Configuration

Nginx is used as a reverse proxy for the Django application. The configuration can be found in `nginx/default.conf`.

## Endpoints

The following API endpoints are available in the application:

1. **Books API**

   - **GET /api/books/**: List all books (pagination applies).
   - **POST /api/books/**: Create a new book.
   - **GET /api/books/{slug}/**: Retrieve a book by slug.
   - **PUT /api/books/{slug}/**: Update a book.
   - **DELETE /api/books/{slug}/**: Delete a book.

2. **Token Authentication**
   - **POST /api/token/**: Obtain an authentication token.

## Running the Project

Use the following command to run the server in development:

```bash
docker-compose up
```

To run the Django management commands related to importing data, you can access the Django container and execute commands like this:

```bash
docker exec -it library_django_container bash
python manage.py import_books
python manage.py import_users
```

## Management Commands

### Import Books

1. **Add Required File:**  
   The CSV file must be located in the same directory as the management command file. Place it in `mysite/core/management/commands`.

2. **Build The Project:**

   ```bash
   docker-compose stop
   docker-compose build
   ```

3. **Start the Project:**

   ```bash
   docker-compose up -d
   ```

4. **Import Books:**

   ```bash
   docker-compose exec django_app python manage.py import_books
   ```

   Ensure the books CSV file is formatted correctly with the required field names in the proper structure.

### Import Users

1. **Add Required File:**  
   The CSV file must be located in the same directory as the management command file. Place it in `mysite/core/management/commands`.

2. **Build The Project:**

   ```bash
   docker-compose stop
   docker-compose build
   ```

3. **Start the Project:**

   ```bash
   docker-compose up -d
   ```

4. **Import Users:**

   ```bash
   docker-compose exec django_app python manage.py import_users
   ```

   Ensure the users CSV file is formatted correctly with the required field names in the proper structure.
