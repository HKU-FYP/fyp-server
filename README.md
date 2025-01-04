# 1. Set up

### 1. Set up MySQL server

Install MySQL if not installed.

```
brew install mysql
```

Create database named `fyp`.

```
create database fyp;
use fyp;
```

### 2. Install poetry

```
brew install pipx
pipx install poetry
```

### 3. Activate virtualenv & Install dependencies

```
poetry shell
poetry install
```

### 4. Run the FastAPI server

```
python -m src
```

It auto-creates DB tables.

### 5. View Docs

Type `localhost:8888/docs` in your browser.
