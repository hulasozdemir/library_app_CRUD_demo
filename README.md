# Library Management CRUD App

This is a simple CRUD (Create, Read, Update, Delete) application for managing a library's book collection, built with Flask and SQLite, and containerized with Docker.

## Features

- Add new books
- View the list of books
- Update book details
- Delete books from the collection

## Project Structure

```
library_app/
├── app.py
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── add_book.html
│   ├── update_book.html
├── static/
│   ├── styles.css
├── database/
│   └── library.db
├── requirements.txt
├── Dockerfile
└── .dockerignore
```

## Prerequisites

- Docker installed on your machine

## Setup and Running

1. Clone the repository:

```bash
git clone https://github.com/hulasozdemir/library_app_CRUD_demo.git
cd library_app
```

2. Build the Docker image:

```bash
docker build -t library_app .
```

3. Run the Docker container:

```bash
docker run -d -p 5000:5000 --name library_app_container library_app
```

4. Open your browser and navigate to `http://localhost:5000`.

## Development

If you want to run the app without Docker, make sure you have Python installed and follow these steps:

1. Install the dependencies:

```bash
pip install -r requirements.txt
```

2. Run the application:

```bash
python app.py
```






