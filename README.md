# Django Detectives Blog

A simple Django blog application with Authors and Posts designed for learning debugging skills.

## Features

- Home page with recent posts
- List all posts
- Individual post details
- List all authors
- Author detail pages with their posts
- Admin interface for managing content

## Setup

1. Create and activate a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run migrations:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

4. Create a superuser:
   ```bash
   python manage.py createsuperuser
   ```

5. Run the development server:
   ```bash
   python manage.py runserver
   ```

6. Visit http://127.0.0.1:8000/ to see the blog

## Models

- **Author**: Extends Django's User model with bio and website fields
- **Post**: Blog posts with title, content, author, and publication status

## Bug Analysis & Solutions

This project contains three common Django bugs that students often encounter. Here's a detailed breakdown of each bug, why it occurs, and how to fix it:

### Bug 1: NoReverseMatch Error (URL Template Tag)

**What was wrong:**
```html
<!-- In blog/templates/blog/base.html -->
<a href="{% url 'author_lists' %}">Authors</a>  <!-- ❌ WRONG -->
```

**The Problem:**
- The URL name `'author_lists'` doesn't exist in our URL configuration
- Django's `{% url %}` template tag looks for a URL pattern with this exact name
- When it can't find it, Django raises a `NoReverseMatch` exception

**Why this happens:**
- Simple typos in URL names are very common
- URL names must match exactly between `urls.py` and templates
- Django is case-sensitive and doesn't provide helpful suggestions for typos

**The Fix:**
```html
<!-- Corrected version -->
<a href="{% url 'author_list' %}">Authors</a>  <!-- ✅ CORRECT -->
```

**How to debug this:**
1. Check the error message - it will tell you which URL name is missing
2. Look at your `urls.py` file to see the correct name
3. Use `python manage.py show_urls` (if you have django-extensions) to see all URL patterns

### Bug 2: Missing Context Data (View Logic)

**What was wrong:**
```python
# In blog/views.py - author_detail function
def author_detail(request, author_id):
    author = get_object_or_404(Author, id=author_id)
    # Bug: Forgot to pass posts to template context
    return render(request, 'blog/author_detail.html', {'author': author})
```

**The Problem:**
- The template expects a `posts` variable to display the author's posts
- The view only passes the `author` object to the template
- The template tries to loop over `posts` but it doesn't exist, so it shows "No posts by this author yet"

**Why this happens:**
- Easy to forget to pass all required data to templates
- Templates fail silently when variables are missing (they just show empty content)
- No immediate error - the page loads but is missing data

**The Fix:**
```python
def author_detail(request, author_id):
    author = get_object_or_404(Author, id=author_id)
    posts = Post.objects.filter(author=author, published=True).order_by('-created_at')
    return render(request, 'blog/author_detail.html', {'author': author, 'posts': posts})
```

**How to debug this:**
1. Check what variables your template expects
2. Look at the view's context dictionary
3. Use Django Debug Toolbar to see what context variables are available
4. Add `{{ posts|length }}` to your template to test if the variable exists

### Bug 3: N+1 Query Problem (Database Performance)

**What was wrong:**
```python
# In blog/views.py - home and post_list functions
def home(request):
    posts = Post.objects.filter(published=True).order_by('-created_at')[:5]
    return render(request, 'blog/home.html', {'posts': posts})

def post_list(request):
    posts = Post.objects.filter(published=True).order_by('-created_at')
    return render(request, 'blog/post_list.html', {'posts': posts})
```

**The Problem:**
- When the template accesses `post.author` for each post, Django makes a separate database query
- If you have 10 posts, Django makes 1 query for posts + 10 queries for authors = 11 total queries
- This is called the "N+1 query problem" and can severely impact performance

**Why this happens:**
- Django's ORM is lazy - it only fetches data when you actually access it
- Foreign key relationships aren't automatically loaded
- This is a very common performance issue in Django applications

**The Fix:**
```python
def home(request):
    posts = Post.objects.filter(published=True).select_related('author').order_by('-created_at')[:5]
    return render(request, 'blog/home.html', {'posts': posts})

def post_list(request):
    posts = Post.objects.filter(published=True).select_related('author').order_by('-created_at')
    return render(request, 'blog/post_list.html', {'posts': posts})
```

**How to debug this:**
1. Use Django Debug Toolbar to see the number of queries
2. Enable query logging in settings:
   ```python
   LOGGING = {
       'version': 1,
       'disable_existing_loggers': False,
       'handlers': {
           'console': {
               'class': 'logging.StreamHandler',
           },
       },
       'loggers': {
           'django.db.backends': {
               'level': 'DEBUG',
               'handlers': ['console'],
           },
       },
   }
   ```
3. Use `select_related()` for foreign keys and `prefetch_related()` for many-to-many relationships

## Learning Outcomes

After working through these bugs, you should understand:

1. **URL Configuration**: How Django's URL system works and common mistakes
2. **Template Context**: The relationship between views and templates
3. **Database Optimization**: How to write efficient Django queries
4. **Debugging Techniques**: Tools and methods for finding and fixing Django bugs

## Branches

- `main`: Contains the original code with bugs
- `dd_sln`: Contains the fixed code with detailed explanations

## Additional Resources

- [Django URL Dispatcher](https://docs.djangoproject.com/en/stable/topics/http/urls/)
- [Django Template Language](https://docs.djangoproject.com/en/stable/topics/templates/)
- [Django Database Optimization](https://docs.djangoproject.com/en/stable/topics/db/optimization/)
- [Django Debug Toolbar](https://django-debug-toolbar.readthedocs.io/)
