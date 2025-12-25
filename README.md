# django-todo

## Setup

```bash
# Create virtual environment
uv venv

# Activate virtual environment
source .venv/bin/activate

# Install dependencies
uv sync

# Run migrations
python manage.py migrate

# Load fixtures (optional)
python manage.py loaddata fixtures/tasks.json
```

## Run

```bash
python manage.py runserver
# or run on another port 
python manage.py runserver <your-port>
```

Visit `http://127.0.0.1:8000/`