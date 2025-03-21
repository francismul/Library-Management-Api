# Library Management API

This project is a Django-based API backend for managing a library system. It provides endpoints for viewing, adding, updating, and deleting books, as well as borrowing and returning books.

## API Endpoints

### Public Endpoints

- **View books by page**
  - URL: `/api/books/?page=`
  - Method: `GET`
  - Description: Retrieve a paginated list of books.

- **View a single book**
  - URL: `/api/books/{slug}/`
  - Method: `GET`
  - Description: Retrieve details of a single book by its slug.

### Admin Endpoints

- **Add a new book**
  - URL: `/api/books/`
  - Method: `POST`
  - Description: Add a new book to the library. (Admin only)

- **Update book details**
  - URL: `/api/books/{slug}/`
  - Method: `PUT`
  - Description: Update the details of an existing book. (Admin only)

- **Delete a book**
  - URL: `/api/books/{slug}/`
  - Method: `DELETE`
  - Description: Delete a book from the library. (Admin only)

### Authenticated User Endpoints

- **Borrow a book**
  - URL: `/api/borrow/`
  - Method: `POST`
  - Description: Borrow a book from the library. (Authenticated users)

- **View borrowed books**
  - URL: `/api/borrow/`
  - Method: `GET`
  - Description: View a list of borrowed books. (Authenticated users)

- **Return a book**
  - URL: `/api/return/`
  - Method: `POST`
  - Description: Return a borrowed book to the library. (Authenticated users)

- **View returned books**
  - URL: `/api/return/`
  - Method: `GET`
  - Description: View a list of returned books. (Authenticated users)

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/library-management-api.git
    cd library-management-api
    ```

2. Create a virtual environment and activate it:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

4. Apply the migrations:
    ```sh
    python manage.py migrate
    ```

5. Create a superuser:
    ```sh
    python manage.py createsuperuser
    ```

6. Run the development server:
    ```sh
    python manage.py runserver
    ```

## Usage

- Access the API at `http://127.0.0.1:8000/api/`
- Use an API client like Postman to interact with the endpoints.

## License

This project is licensed under the MIT License.