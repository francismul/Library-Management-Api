# Library Management API

This project is a Django-based API backend for managing a library system. It provides endpoints for viewing, adding, updating, and deleting books, as well as borrowing and returning books.

## API Endpoints

### Public Endpoints

- **View books by page**
  - URL: `/api/books/`
  - URL: `/api/books/?page=/`
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

## Data
- I have made two python files in the core/management/commands directory
- (import_books.py, import_users.py) 
- This two files helps in populating the database with initial working data.
- You'll need to find a csv file containing books, and ensure the csv header has the following fields, (Title, Authors, Published Date), drop the csv file called books.csv inside core/management/commands folder
- For users, get a csv file with the following in its header (username, first_name, last_name, password, email), call the csv file, users.csv

1. Add csv file (books.csv, users.csv)
2. Populate the database
   - for books

   ```sh
   python manage.py import_books
   ```
   - for users

   ```sh
   python manage.py import_users
   ```


## Usage

- Access the API at `http://127.0.0.1:8000/api/`
- Use an API client like Postman to interact with the endpoints.

## License

This project is licensed under the MIT License.
