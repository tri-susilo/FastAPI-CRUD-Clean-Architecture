# 🚀 FastAPI CRUD API with SQLModel & MySQL

A clean, modular REST API built with **FastAPI**, **SQLModel**, and **MySQL**, following Clean Architecture and Object-Oriented Programming (OOP). It includes dependency injection, environment-based configuration, Docker support, and scalable code structure.

---

## 🗂 Project Structure

```
.
├── app/
│   ├── api/
│   │   └── v1/
│   │       └── user.py                # API routes
│   ├── core/
│   │   ├── config.py                  # Env config using dotenv
│   │   └── database.py                # SQLModel engine + session
│   ├── models/
│   │   └── users.py                   # SQLModel User table
│   ├── repositories/
│   │   └── user_repositories.py       # CRUD DB access logic
│   ├── schemas/
│   │   └── user_schemas.py            # Pydantic-based request/response models
│   ├── services/
│   │   └── users_services.py          # Business logic for user
│   └── main.py                        # App entrypoint
├── venv/                              # Virtual environment (ignored)
├── .dockerignore                      # Ignore files when building Docker image
├── .env                               # Environment variables
├── .gitignore                         # Ignore Python/artifacts/secrets
├── dockerfile                         # Docker image instructions
└── requirements.txt                   # Dependency list
```

---

## 🧰 Tech Stack

- **FastAPI** – High-performance web framework
- **SQLModel** – ORM combining SQLAlchemy and Pydantic
- **MySQL** – Relational database
- **Uvicorn** – ASGI server for FastAPI
- **Docker** – Containerization for deployment
- **python-dotenv** – Environment variable management

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/fastapi_clean_crud.git
cd fastapi_clean_crud
```

### 2. Create and Activate Virtual Environment

```bash
python -m venv venv
# On Unix or MacOS
source venv/bin/activate
# On Windows
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file in the project root:

```ini
DATABASE_URL=mysql+pymysql://your_user:your_password@localhost:3306/your_db_name
```

### 5. Run the Application

```bash
uvicorn app.main:app --reload
```

Access the interactive API docs: [http://localhost:8000/docs](http://localhost:8000/docs)

---

## 🐳 Docker Deployment

### 1. Build the Docker Image

```bash
docker build -t fastapi-crud .
```

### 2. Run the Container

```bash
docker run -d -p 8000:8000 --name fastapi-app fastapi-crud
```

You can pass environment variables using `--env-file .env` if needed.

---

## 🔄 Application Flowchart

```mermaid
flowchart TD
    A[Client Request] --> B[FastAPI Router]
    B --> C[Service Layer]
    C --> D[Repository Layer]
    D --> E[Database]
    E --> D
    D --> C
    C --> B
    B --> F[Response to Client]
```

---

## ✅ Features

- ✅ Clean architecture using services, repositories, and schemas
- ✅ SQLModel integration with MySQL
- ✅ Auto-generated Swagger and ReDoc docs
- ✅ Docker support for easy deployment
- ✅ Modular and production-ready layout

---

## 📄 License

This project is licensed under the **MIT License** — feel free to use and modify it as needed.
