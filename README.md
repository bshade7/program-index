# Program Index

Example program that is intended to index programs located in SVN repositories.  Will also eventually contain pages to describe functions for each program as well as a "tagging" ability to allow category searching.

## Running Locally
Clone the git repository.
```bash
git clone https://github.com/bshade7/program-index.git
```

Install pipenv package for virtualenvironment and dependency management.
```bash
pip install pipenv
```

Move into cloned project directory.
```bash
cd program-index
```

Create virtual environment in the local directory.
```bash
pipenv install
```

Activate your new virtual environment
```bash
pipenv shell
```

Migrate the database changes required.
```bash
python manage.py migrate
```

Run the development web server.
```bash
python manage.py runserver
```
