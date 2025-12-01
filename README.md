# PashuBreed AI

This is a full-stack web application that predicts cattle breeds from uploaded images.

## Setup

### Prerequisites

- Python 3.8+
- PostgreSQL
- Node.js (for `npx`)

### Database Setup

1.  Install PostgreSQL.
2.  Create a database named `ai_breed_db`.
3.  Create a user `postgres` with password `123456` and grant all privileges on the `ai_breed_db` database.

    ```sql
    CREATE DATABASE ai_breed_db;
    CREATE USER postgres WITH PASSWORD '123456';
    GRANT ALL PRIVILEGES ON DATABASE ai_breed_db TO postgres;
    ```

### Backend Setup

1.  Navigate to the `backend` directory:
    ```bash
    cd backend
    ```
2.  Create and activate a virtual environment:
    ```bash
    python -m venv venv
    venv\Scripts\activate
    ```
3.  Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```
4.  Start the backend server:
    ```bash
    uvicorn app.main:app --reload --port 8000
    ```

### Frontend Setup

1.  Navigate to the `frontend` directory:
    ```bash
    cd frontend
    ```
2.  Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```
3.  Start the frontend server:
    ```bash
    streamlit run main_app.py
    ```

## Lovable Deployment

To run the application with Lovable, use the following command:

```bash
npx lovable@latest dev
```
