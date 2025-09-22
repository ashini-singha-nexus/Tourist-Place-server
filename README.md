
# Tourist Place API

This is a FastAPI backend project for managing tourist places.

## Features

- JWT authentication (register, login)
- CRUD operations for places
- Pagination and sorting for getting all places
- Authorization: Only the creator of a place can update or delete it.

## Project Structure

```
├── app
│   ├── __init__.py
│   ├── database.py
│   ├── main.py
│   ├── models
│   │   ├── __init__.py
│   │   ├── place.py
│   │   └── user.py
│   ├── routers
│   │   ├── __init__.py
│   │   ├── auth.py
│   │   └── places.py
│   ├── schemas
│   │   ├── __init__.py
│   │   ├── place.py
│   │   └── user.py
│   ├── services
│   │   ├── __init__.py
│   │   ├── auth.py
│   │   └── places.py
│   └── utils
│       ├── __init__.py
│       ├── deps.py
│       └── security.py
├── migrations
├── .gitignore
├── README.md
└── requirements.txt
```

## Setup and Run

### Prerequisites

- Python 3.9+
- PostgreSQL

### 1. Create and activate a virtual environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Set up the database

1. Make sure you have PostgreSQL running.
2. Create a new database.
3. Update the `DATABASE_URL` in `app/database.py` with your database credentials:

   ```python
   DATABASE_URL = "postgresql://user:password@localhost/db_name"
   ```

### 4. Run the application

```bash
uvicorn app.main:app --reload
```

The API will be available at `http://127.0.0.1:8000`.

## Migrations (Alembic)

This project is set up to use Alembic for database migrations, but the migration scripts themselves are not yet created.

To initialize Alembic:

```bash
alembic init migrations
```

Then, you'll need to configure `migrations/env.py` to point to your SQLModel models.

## API Usage

### Authentication

- `POST /auth/register`: Create a new user.
- `POST /auth/login`: Authenticate and get a JWT token.

### Places

- `POST /places/`: Create a new place (requires authentication).
- `GET /places/`: Get all places with pagination and sorting.
- `GET /places/{id}`: Get a single place.
- `PUT /places/{id}`: Update a place (requires authentication, only creator can update).
- `DELETE /places/{id}`: Delete a place (requires authentication, only creator can delete).
