# Django Detectives Blog

A simple Django blog application with Authors and Posts.

## Features

- Home page with recent posts
- List all posts
- Individual post details
- List all authors
- Author detail pages with their posts
- Admin interface for managing content

## Setup

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Run migrations:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

3. Create a superuser:
   ```bash
   python manage.py createsuperuser
   ```

4. Run the development server:
   ```bash
   python manage.py runserver
   ```

5. Visit http://127.0.0.1:8000/ to see the blog

## Models

- **Author**: Extends Django's User model with bio and website fields
- **Post**: Blog posts with title, content, author, and publication status

## Bugs

This project intentionally contains several bugs for debugging practice:

1. **NoReverseMatch Error**: There's a typo in a URL template tag
2. **Missing Context Data**: A view is missing data in its template context
3. **N+1 Query Problem**: Views are making inefficient database queries

Can you find and fix them all?
