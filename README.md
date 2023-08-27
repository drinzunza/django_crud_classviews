# Django CRUD Movie Project

## Overview

This is a simple Django project that demonstrates CRUD (Create, Read, Update, Delete) operations using Django's Class-Based Views. It's intended to serve as a template for further development and experimentation.

## Features

- List Movies
- View Movie Details
- Add New Movies
- Update Movie Details
- Delete Movies
- Upload Movie Posters

## Recommendations

- **Styling**: The project uses basic HTML and Bootstrap for styling. We recommend enhancing it with more sophisticated CSS or using a frontend framework like React or Angular.
  
- **Crispy Forms**: Currently, the project uses Django's built-in form rendering. For better form styling and control, consider integrating Django Crispy Forms.

## Running the Project Locally

### Prerequisites

- Python 3.x
- Pip
- Virtualenv (Optional)

### Steps

1. **Clone the repository**

    ```bash
    git clone https://github.com/yourusername/django-crud-movie.git
    ```

2. **Navigate to the project directory**

    ```bash
    cd django-crud-movie
    ```

3. **Create and Activate Virtual Environment (Optional)**

    ```bash
    virtualenv venv
    source venv/bin/activate  # On Windows, use `venv\\Scripts\\activate`
    ```

4. **Install Dependencies**

    ```bash
    pip install -r requirements.txt
    ```

5. **Apply Migrations**

    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

6. **Run the Development Server**

    ```bash
    python manage.py runserver
    ```

7. Open your web browser and go to `http://127.0.0.1:8000/`
