# Django Detectives Blog 🕵️‍♂️

Welcome to **Django Detectives** - a hands-on debugging exercise designed to help you master common Django issues! This project is a simple blog application with Authors and Posts that contains **intentional bugs** for you to find and fix.

## 🎯 What is this project?

This is a **learning exercise** where you'll practice debugging real-world Django problems. The application is a basic blog with:
- **Authors** who can write posts
- **Posts** with titles, content, and publication status
- **Navigation** between different pages
- **Admin interface** for content management

## 🐛 Your Mission: Find the Bugs!

This project contains **3 distinct bugs** that are commonly encountered in Django development:

1. **🔗 Routing Bug**: A NoReverseMatch error caused by a typo in a URL template tag
2. **📊 Data Bug**: A page that loads but is missing data due to incomplete view logic
3. **⚡ Performance Bug**: An N+1 query problem that causes inefficient database queries

Your task is to:
1. **Run the application** and explore it
2. **Identify each bug** by testing different features
3. **Fix the bugs** one by one
4. **Understand why** each bug occurred and how to prevent it

## 🚀 Getting Started

### Prerequisites
- Python 3.8 or higher
- Basic knowledge of Django
- Git (for cloning) or a web browser (for downloading)

### Step 1: Get the Project on Your Computer

You have two options to get this project on your computer:

#### Option A: Clone with Git (Recommended)

1. **Open your terminal/command prompt**

2. **Navigate to where you want to save the project**:
   ```bash
   cd Desktop  # or wherever you want to save it
   ```

3. **Clone the repository**:
   ```bash
   git clone https://github.com/YOUR_USERNAME/django_detectives.git
   cd django_detectives
   ```
   Replace `YOUR_USERNAME` with the actual GitHub username of the repository owner.

#### Option B: Download as ZIP

1. **Go to the GitHub repository** in your web browser

2. **Click the green "Code" button** in the top-right corner

3. **Select "Download ZIP"** from the dropdown menu

4. **Extract the ZIP file** to your desired location (e.g., Desktop)

5. **Open your terminal/command prompt** and navigate to the extracted folder:
   ```bash
   cd Desktop/django_detectives-main  # or wherever you extracted it
   ```

### Step 2: Set Up the Environment

1. **Create a virtual environment** (recommended):
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. **Install Django**:
   ```bash
   pip install -r requirements.txt
   ```

### Step 3: Set Up the Database

1. **Create database migrations**:
   ```bash
   python manage.py makemigrations
   ```

2. **Apply migrations**:
   ```bash
   python manage.py migrate
   ```

### Step 4: Create a Superuser

Create an admin user to access the Django admin interface:

```bash
python manage.py createsuperuser
```

Follow the prompts to create your admin account (username, email, password).

### Step 5: Seed the Database with Sample Data

Run this command to create sample authors and posts for testing:

```bash
python manage.py shell
```

Then paste and run this code in the Django shell:

```python
from django.contrib.auth.models import User
from blog.models import Author, Post

# Create sample users and authors
user1 = User.objects.create_user('john', 'john@example.com', 'password123', first_name='John', last_name='Doe')
user2 = User.objects.create_user('jane', 'jane@example.com', 'password123', first_name='Jane', last_name='Smith')

author1 = Author.objects.create(user=user1, bio='A passionate blogger who loves Django', website='https://johndoe.com')
author2 = Author.objects.create(user=user2, bio='Tech enthusiast and developer', website='https://janesmith.dev')

# Create sample posts
Post.objects.create(
    title='Getting Started with Django',
    content='Django is a high-level Python web framework that encourages rapid development and clean, pragmatic design. Built by experienced developers, it takes care of much of the hassle of web development, so you can focus on writing your app without needing to reinvent the wheel.',
    author=author1,
    published=True
)

Post.objects.create(
    title='Understanding Django Models',
    content='Django models are the single, definitive source of information about your data. They contain the essential fields and behaviors of the data you\'re storing. Generally, each model maps to a single database table.',
    author=author1,
    published=True
)

Post.objects.create(
    title='Django Views and Templates',
    content='A view is a Python function that takes a Web request and returns a Web response. This response can be the HTML contents of a Web page, or a redirect, or a 404 error, or an XML document, or an image, or anything.',
    author=author2,
    published=True
)

Post.objects.create(
    title='Django URL Configuration',
    content='A clean, elegant URL scheme is an important detail in a high-quality Web application. Django lets you design URLs however you want, with no framework limitations.',
    author=author2,
    published=True
)

print('Sample data created successfully!')
exit()
```

### Step 6: Run the Application

Start the Django development server:

```bash
python manage.py runserver
```

Visit **http://127.0.0.1:8000/** in your browser to see the blog!

## 🧪 Testing the Application

### Available Pages:
- **Home** (/) - Shows recent posts
- **All Posts** (/posts/) - Lists all published posts
- **Authors** (/authors/) - Lists all authors
- **Admin** (/admin/) - Django admin interface

### What to Test:
1. **Navigation**: Click through all the navigation links
2. **Post Lists**: View the home page and all posts page
3. **Author Pages**: Click on author names to see their detail pages
4. **Admin Interface**: Log in with your superuser account

## 🐛 Bug Hunting Guide

### Bug 1: NoReverseMatch Error
- **Where to look**: Navigation menu
- **What to test**: Click the "Authors" link
- **Expected behavior**: Should navigate to authors page
- **Actual behavior**: You'll get an error page

### Bug 2: Missing Data
- **Where to look**: Author detail pages
- **What to test**: Click on any author's name from a post
- **Expected behavior**: Should show the author's posts
- **Actual behavior**: Page loads but shows "No posts by this author yet"

### Bug 3: Performance Issue
- **Where to look**: Home page and posts list page
- **What to test**: Load these pages and check browser developer tools
- **Expected behavior**: Should load quickly
- **Actual behavior**: May be slow due to multiple database queries

## 🛠️ Debugging Tips

1. **Check the Django console** for error messages
2. **Use browser developer tools** to see network requests
3. **Enable Django Debug Toolbar** (optional) to see database queries
4. **Read error messages carefully** - they often tell you exactly what's wrong
5. **Check the Django documentation** for the correct syntax

## 📚 Learning Objectives

After completing this exercise, you should understand:

- How Django's URL system works and common mistakes
- The relationship between views and templates
- Database query optimization techniques
- Common debugging strategies for Django applications

## 🎉 Success Criteria

You've successfully completed the exercise when:
- ✅ All navigation links work without errors
- ✅ Author detail pages show the author's posts
- ✅ Pages load efficiently without unnecessary database queries
- ✅ You understand why each bug occurred and how to prevent it

## 📖 Additional Resources

- [Django Documentation](https://docs.djangoproject.com/)
- [Django Debug Toolbar](https://django-debug-toolbar.readthedocs.io/)
- [Django Best Practices](https://docs.djangoproject.com/en/stable/topics/db/optimization/)

---

**Happy Debugging!** 🐛➡️✅
