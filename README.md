# taskflow-api

A REST API for task management built with FastAPI, SQLAlchemy and JWT authentication.

## Features

- User registration and login with JWT tokens
- Full CRUD for tasks (create, read, update, delete)
- Tasks are scoped per user
- Filter tasks by status and priority
- Pagination support

## Tech Stack

- **FastAPI** — async web framework
- **SQLAlchemy** — ORM and database toolkit
- **SQLite** — lightweight database (easy to swap for Postgres)
- **Pydantic v2** — data validation
- **python-jose** — JWT token handling
- **passlib + bcrypt** — password hashing

## Getting Started

```bash
# clone the repo
git clone https://github.com/zspirit/taskflow-api.git
cd taskflow-api

# create a virtual environment
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

# install dependencies
pip install -r requirements.txt

# run the server
uvicorn main:app --reload
```

The API will be available at `http://localhost:8000`.

Interactive docs at `http://localhost:8000/docs`.

## API Endpoints

### Auth
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/auth/register` | Create a new account |
| POST | `/auth/login` | Login and get JWT token |

### Tasks (requires auth)
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/tasks` | List your tasks (supports filtering & pagination) |
| POST | `/tasks` | Create a new task |
| GET | `/tasks/{id}` | Get a specific task |
| PATCH | `/tasks/{id}` | Update a task |
| DELETE | `/tasks/{id}` | Delete a task |

### Query Parameters for GET /tasks
- `status` — filter by status (`todo`, `in_progress`, `done`)
- `priority` — filter by priority (`low`, `medium`, `high`)
- `skip` — offset for pagination (default: 0)
- `limit` — max results per page (default: 20, max: 100)

## License

MIT
