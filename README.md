# REROUTE Base Template

<div align="center">

**[FastAPI](https://fastapi.tiangolo.com) + [REROUTE](https://github.com/cbsajan/reroute) = Modern File-Based Routing**

A minimal, production-ready Cookiecutter template for building FastAPI applications with REROUTE's intuitive file-based routing system.

[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](LICENSE)
[![REROUTE](https://img.shields.io/badge/REROUTE-0.4.0%2B-green.svg)](https://github.com/cbsajan/reroute)
[![Python](https://img.shields.io/badge/Python-3.9%2B-blue.svg)](https://www.python.org)

[Features](#features) • [Quick Start](#quick-start) • [Documentation](#documentation) • [Contributing](#contributing)

</div>

---

## Overview

**REROUTE Base** is a minimal Cookiecutter template that generates a clean, well-structured FastAPI application with REROUTE's file-based routing. No boilerplate, no bloat - just the essentials for building modern APIs.

**Perfect for:**
- RESTful APIs and microservices
- Quick prototypes and MVPs
- Learning REROUTE's routing system
- Building custom applications from a clean foundation

## Features

- **File-Based Routing** - Routes auto-discovered from `app/routes/` directory structure
- **FastAPI Integration** - Full OpenAPI/Swagger documentation at `/docs`
- **Modern Tooling** - UV package manager, pyproject.toml, Python 3.9+
- **Database Support** - Optional PostgreSQL, MySQL, SQLite, or MongoDB integration
- **Production Ready** - Configuration management, logging, error handling
- **Testing Setup** - Optional test suite with pytest
- **Decorator System** - Built-in rate limiting, caching, and custom decorators
- **Flexible Configuration** - Environment-based config with `.env` support

### REROUTE Routing Magic

```python
# File: app/routes/users/page.py
class UsersRoutes(RouteBase):
    def get(self):
        return {"users": []}

# Automatically creates: GET /users
```

**Nested routes work too:**
```bash
app/routes/
├── users/
│   ├── [id]/page.py      # GET /users/{id}
│   └── posts/
│       └── page.py       # GET /users/posts
```

## Quick Start

### Option 1: Using REROUTE CLI (Recommended)

```bash
# Install REROUTE with FastAPI support
pip install reroute[fastapi]

# Create a new project
reroute init myapi --template gh:cbsajan/reroute-base

# Navigate and run
cd myapi
uv sync
uv run main.py
```

**Your API is now running at:** http://localhost:7376

Interactive API docs: http://localhost:7376/docs

### Option 2: Using Cookiecutter Directly

```bash
# Install cookiecutter
pip install cookiecutter

# Generate project
cookiecutter gh:cbsajan/reroute-base

# Follow the prompts
cd myapi
uv venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python main.py
```

```bash
# Install REROUTE
pip install reroute[fastapi]

# Create a new project using this template
reroute init myproject --template gh:cbsajan/reroute-base

# Or with custom options
reroute init myproject --template gh:cbsajan/reroute-base --database postgresql
```

### Via Cookiecutter Directly

```bash
# Install cookiecutter
pip install cookiecutter

# Create a new project
cookiecutter gh:cbsajan/reroute-base
```

## Template Variables

| Variable | Description | Default | Options |
|----------|-------------|---------|---------|
| `project_name` | Name of the project | `myapi` | Any valid Python name |
| `description` | Project description | `My API` | Free text |
| `framework` | Backend framework | `fastapi` | fastapi |
| `host` | Server host | `0.0.0.0` | Any valid host |
| `port` | Server port | `7376` | 1024-65535 |
| `reload` | Enable auto-reload | `true` | true/false |
| `include_tests` | Generate test files | `Yes` | Yes/No |
| `database` | Database type | `none` | postgresql/mysql/sqlite/mongodb/none |
| `package_manager` | Package manager | `uv` | uv/pip |

## Database Options

- `none` - No database
- `postgresql` - PostgreSQL with SQLAlchemy
- `mysql` - MySQL with SQLAlchemy
- `sqlite` - SQLite with SQLAlchemy
- `mongodb` - MongoDB with Motor

## Generated Project Structure

```
myapi/
├── app/
│   ├── routes/
│   │   ├── __init__.py
│   │   ├── root.py          # Root and health endpoints
│   │   └── hello/
│   │       └── page.py      # Example CRUD route
│   ├── db_models/           # Database models (if database enabled)
│   │   └── user.py
│   ├── database.py          # Database configuration (if database enabled)
│   └── __init__.py
├── tests/
│   ├── __init__.py
│   └── test_main.py         # Test suite (if enabled)
├── config.py                # Application configuration
├── logger.py                # Logging setup
├── main.py                  # Application entry point
├── pyproject.toml           # Python project configuration
├── requirements.txt         # Dependencies
└── .env.example             # Environment variables template
```

## Next Steps

After creating a project:

```bash
cd myapi

# Create virtual environment and install dependencies
uv venv
uv sync

# Copy environment file and configure
cp .env.example .env

# Run the development server
uv run main.py
```

Visit http://localhost:7376/docs for API documentation.

---

## Documentation

- **REROUTE Docs**: https://cbsajan.github.io/reroute
- **FastAPI Docs**: https://fastapi.tiangolo.com
- **Cookiecutter Docs**: https://cookiecutter.readthedocs.io

### Project Structure

```
myapi/
├── app/
│   ├── routes/
│   │   ├── __init__.py
│   │   ├── root.py              # GET /, GET /health
│   │   └── hello/
│   │       └── page.py          # GET /hello, POST /hello
│   ├── db_models/               # Database models (if database enabled)
│   │   └── user.py
│   ├── database.py              # Database configuration (if database enabled)
│   └── __init__.py
├── tests/                       # Test suite (if enabled)
│   ├── __init__.py
│   └── test_main.py
├── config.py                    # Application configuration
├── logger.py                    # Logging setup
├── main.py                      # Application entry point
├── pyproject.toml               # Python project configuration
├── requirements.txt             # Dependencies
└── .env.example                 # Environment variables template
```

### Key Files

- **`main.py`** - Application entry point, initializes REROUTE adapter
- **`config.py`** - Environment-based configuration management
- **`logger.py`** - Structured logging setup
- **`app/routes/`** - File-based routing (auto-discovered)
- **`app/database.py`** - Database session management (if database enabled)

### Creating Routes

**Simple route:**
```python
# app/routes/hello/page.py
from reroute import RouteBase

class HelloRoutes(RouteBase):
    def get(self):
        return {"message": "Hello, World!"}
```

**With parameters:**
```python
from fastapi import Query
from reroute import RouteBase

class HelloRoutes(RouteBase):
    def get(self, name: str = Query("stranger")):
        return {"message": f"Hello, {name}!"}
```

**With decorators:**
```python
from reroute import RouteBase
from reroute.decorators import rate_limit, cache

class HelloRoutes(RouteBase):
    @cache(duration=60)
    @rate_limit("10/min")
    def get(self):
        return {"message": "Cached and rate limited!"}
```

---

## Examples

### Basic CRUD API

```python
# app/routes/tasks/page.py
from fastapi import Body
from reroute import RouteBase

class TasksRoutes(RouteBase):
    def __init__(self):
        super().__init__()
        self.tasks = {}

    def get(self):
        """List all tasks"""
        return {"tasks": list(self.tasks.values())}

    def post(self, task: dict = Body(...)):
        """Create a new task"""
        task_id = len(self.tasks) + 1
        self.tasks[task_id] = {**task, "id": task_id}
        return self.tasks[task_id], 201
```

### Dynamic Routes

```bash
# app/routes/users/[id]/page.py
# Creates: GET /users/{id}, PUT /users/{id}, DELETE /users/{id}

from fastapi import Path
from reroute import RouteBase

class UserDetailRoutes(RouteBase):
    def get(self, id: int = Path(...)):
        return {"user_id": id}
```

---

## Configuration

Environment variables (create `.env` from `.env.example`):

```bash
# Application
REROUTE_HOST=0.0.0.0
REROUTE_PORT=7376
REROUTE_DEBUG=False

# Database (if enabled)
REROUTE_DATABASE_URL=postgresql://user:pass@localhost:5432/mydb

# CORS
REROUTE_ENABLE_CORS=True
REROUTE_CORS_ORIGINS=http://localhost:3000
```

---

## Development

### Running Tests

```bash
# Install test dependencies
uv sync --extra test

# Run tests
pytest

# Run with coverage
pytest --cov=app tests/
```

### Adding Dependencies

```bash
# With UV (recommended)
uv add requests

# Or manually edit pyproject.toml
uv sync
```

---

## Troubleshooting

**Port already in use?**
```bash
# Change port in .env
REROUTE_PORT=7377
```

**Database connection issues?**
```bash
# Check DATABASE_URL in .env
# Ensure database server is running
# Verify credentials and host
```

**Routes not discovered?**
```bash
# Ensure files are named page.py
# Check directory structure matches URL pattern
# Verify classes inherit from RouteBase
```

---

## Contributing

Contributions welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

---

## Support

- **Documentation**: https://cbsajan.github.io/reroute
- **Issues**: https://github.com/cbsajan/reroute/issues
- **Discussions**: https://github.com/cbsajan/reroute/discussions

---

## License

Apache-2.0 © [Sajan](https://github.com/cbsajan)
