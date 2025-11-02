# DRF Project

Django REST Framework project with local authentication, following the same architecture as the engine project but simplified.

## Description

A Django REST API project built with:
- **Local Authentication**: JWT-based authentication using Django's built-in auth
- **Same Stack**: Django 5.2.2, PostgreSQL, Redis, Celery
- **Same Architecture**: Split settings, modular structure
- **Docker Support**: Full Docker Compose setup for development and production

## Technologies

- **Backend**: Django 5.2.2 + Django REST Framework
- **Database**: PostgreSQL 16
- **Authentication**: JWT (djangorestframework-simplejwt)
- **API Documentation**: drf-spectacular (OpenAPI/Swagger)
- **WSGI Server**: Granian
- **Containerization**: Docker + Docker Compose
- **Python Version**: 3.12+
- **Task Queue**: Celery + Redis

## Main Dependencies

- `django` - Main web framework
- `djangorestframework` - REST API framework
- `djangorestframework-simplejwt` - JWT authentication
- `psycopg2-binary` - PostgreSQL driver
- `redis` - Caching and Celery broker
- `celery` - Asynchronous task queue
- `drf-spectacular` - API documentation

## Quick Start

### Using Docker Compose

```bash
# Clone the repository
git clone <repository-url>
cd drf

# Create .env file from example
cp env.example .env

# Start all services
docker-compose up -d

# Run database migrations
docker-compose exec web python manage.py migrate

# Create a superuser
docker-compose exec web python manage.py createsuperuser
```

### Local Development

```bash
# Install dependencies
uv sync

# Install test dependencies
uv sync --group test

# Set up environment variables
export SECRET_KEY="your-secret-key"
export DEBUG=True
export POSTGRES_DB=drf
export POSTGRES_PASSWORD=postgres
export POSTGRES_USER=postgres
export REDIS_URL=redis://127.0.0.1:6379/0

# Run migrations
cd src && python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Run development server
python manage.py runserver
```

## Access Points

After starting the application:

- **REST API**: http://localhost:8000/api/v1/
- **API Documentation**: http://localhost:8000/api/docs/
- **Admin Panel**: http://localhost:8000/admin/
- **Health Check**: http://localhost:8000/health/

## Project Structure

```
src/
├── server/           # Django settings and configuration
│   ├── settings/     # Split settings (components/, environments/)
│   ├── engine/       # Project-specific views and utilities
│   └── urls.py       # Main URL configuration
├── users/            # User management app
│   ├── models/       # User model
│   └── api/v1/       # API endpoints
├── utils/            # Shared utilities and base models
├── sgi/              # WSGI/ASGI configuration
└── manage.py         # Django management script
```

## API Endpoints

### Authentication
- `POST /api/v1/users/register/` - Register a new user
- `POST /api/v1/users/login/` - Login and get JWT tokens

### Users
- `GET /api/v1/users/` - Get current user info
- `GET /api/v1/users/{id}/` - Get user details

## Environment Variables

See `env.example` for all available environment variables.

## Seeding Data

Seed the database with sample data for development:

```bash
# Seed all modules
make seed

# Seed specific modules
make seed-users      # Seed users only
make seed-companies  # Seed companies only

# Clear existing data and reseed
make seed-clear

# Or using Docker
docker compose exec web python manage.py seed_all
docker compose exec web python manage.py seed_users --count 10
docker compose exec web python manage.py seed_companies --count 5
```

**Default seed data:**
- **Admin user**: `admin` / `admin123` (superuser)
- **Test users**: `user1`, `user2`, etc. / `password123`
- **Sample companies**: TechCorp Inc., Global Services Ltd., StartupXYZ
- **Offices**: Main office and branch office for each company
- **Company hierarchy**: Subsidiary company example

## Development

### Running Tests

```bash
cd src && python -m pytest ../tests/
```

### Code Linting

```bash
uv run pre-commit run --all-files
```

