# patients_crud_fastapi_postgresql_docker

## Overview
This project is a FastAPI application that provides a CRUD (Create, Read, Update, Delete) interface for managing patient records. It uses PostgreSQL as the database and is containerized using Docker.

## Project Structure
```
patients_crud_fastapi_postgresql_docker
├── app
│   ├── main.py
│   ├── models.py
│   ├── schemas.py
│   ├── crud.py
│   ├── database.py
│   ├── api
│   │   └── routes.py
│   └── core
│       └── config.py
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
└── README.md
```

## Setup Instructions

### Prerequisites
- Docker
- Docker Compose

### Installation
1. Clone the repository:
   ```
   git clone <repository-url>
   cd patients_crud_fastapi_postgresql_docker
   ```

2. Create a `.env` file in the root directory with the following content:
   ```
   DATABASE_URL=postgresql://user:password@db/patients_db
   ```

3. Build and run the application using Docker Compose:
   ```
   docker-compose up --build
   ```

### Usage
- The FastAPI application will be accessible at `http://localhost:8000`.
- You can interact with the API using tools like Postman or directly through the Swagger UI at `http://localhost:8000/docs`.

### Endpoints
- `POST /patients`: Create a new patient record.
- `GET /patients`: Retrieve all patient records.
- `GET /patients/{id}`: Retrieve a patient record by ID.
- `PUT /patients/{id}`: Update a patient record by ID.
- `DELETE /patients/{id}`: Delete a patient record by ID.

## License
This project is licensed under the MIT License.