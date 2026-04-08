# Student Management Platform — Phase 2

## Overview

Upgrade your student platform from **hardcoded Python lists** to a **real database** using Django's ORM.

After this exercise your data will persist across server restarts, you'll manage it through the Django admin panel, and you'll add new features: courses, editing, deleting, and filtering.

---

## What Changes From Yesterday

| Yesterday (Phase 1)                             | Today (Phase 2)                           |
| ----------------------------------------------- | ----------------------------------------- |
| Data hardcoded in `views.py` as a list of dicts | Data stored in a SQLite database          |
| Students disappear on restart                   | Students persist permanently              |
| No Course model                                 | Course model with ForeignKey from Student |
| Can only add students                           | Can add, edit, and delete students        |
| No filtering                                    | Filter students by course                 |

---

## Step-by-Step Instructions

### 1. Update your models (`core/models.py`)

Replace the contents of `core/models.py` with the models from `models.py` in this repo. Fill in the TODOs.

You need two models:

**Course:**

- `name` — CharField, max_length=100
- `code` — CharField, max_length=10, unique=True
- `description` — TextField, blank=True
- `__str__` → `"CS101 — Computer Science"`

**Student:**

- `name` — CharField, max_length=100
- `email` — EmailField, unique=True
- `date_of_birth` — DateField, null=True, blank=True
- `grade` — CharField, max_length=2, default="N/A"
- `is_active` — BooleanField, default=True
- `course` — ForeignKey(Course, on_delete=models.CASCADE, related_name="students")
- `created_at` — DateTimeField, auto_now_add=True
- `__str__` → the student's name

### 2. Run migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 3. Set up the admin

Replace your `core/admin.py` with the `admin.py` from this repo. Then:

```bash
python manage.py createsuperuser
```

Go to http://127.0.0.1:8000/admin/ and add:

- At least **2 courses** (e.g. Computer Science / CS101, Mathematics / MATH201)
- At least **4 students** across the courses

### 4. Update your views (`core/views.py`)

Use `views.py` from this repo as a starting point — it has all the view stubs with TODOs.

Key changes:

- **Delete** the hardcoded `STUDENTS` list — you don't need it anymore
- **Import** your models: `from .models import Student, Course`
- **student_list** → `Student.objects.all()` instead of the hardcoded list
- **student_detail** → `get_object_or_404(Student, id=student_id)` instead of the for-loop
- **add_student** → `Student.objects.create(...)` — remember to get the Course object for the FK

### 5. Update your URLs (`core/urls.py`)

Use `urls.py` from this repo — it has the existing routes plus new ones for courses, delete, and edit (commented out for you to uncomment).

### 6. Add new templates

Copy the new templates from `templates/` in this repo into your `core/templates/` folder:

- `course_list.html` — table of courses with student counts
- `course_detail.html` — course info + enrolled students
- `edit_student.html` — pre-filled edit form

### 7. Update existing templates

**`base.html`** — add a "Courses" link to the navigation:

```html
<a href="{% url 'course_list' %}">Courses</a>
```

**`student_detail.html`** — add edit and delete links:

```html
<a href="{% url 'edit_student' student.id %}">Edit</a>
<a href="{% url 'delete_student' student.id %}" onclick="return confirm('Are you sure?')">Delete</a>
```

**`student_list.html`** — show the student's course in the table:

```html
<td>{{ student.course.name }}</td>
```

**`add_student.html`** — replace the course text input with a dropdown:

```html
<label>Course:</label>
<select name="course_id">
  {% for course in courses %}
  <option value="{{ course.id }}">{{ course.name }}</option>
  {% endfor %}
</select>
```

---

## Features to Implement

### Core (required)

- [x] Course and Student models with ForeignKey
- [x] Migrations and admin setup
- [x] All views using ORM instead of hardcoded data
- [x] Course list page (`/courses/`)
- [x] Course detail page (`/courses/<id>/`) showing enrolled students

### New features (required)

- [x] **Delete student** — button on detail page, removes from DB, redirects to list
- [x] **Edit student** — form pre-filled with existing data, updates on submit
- [ ] **Filter by course** — links on student list to show only students in a specific course
- [x] **Student count** — show number of enrolled students on the course list page

---

**Tomorrow**: APIs and REST — we'll expose this data as a JSON API using Django REST Framework.
