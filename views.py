"""
Session 4 — Student Management Platform (Phase 2)
core/views.py

Copy this into your core/views.py, replacing the old version.
Fill in the TODOs.
"""

from django.shortcuts import render, redirect, get_object_or_404
from .models import Student, Course


def home(request):
    return render(request, "home.html")


def about(request):
    return render(request, "about.html")


def student_list(request):
    # TODO: support filtering by course
    # Check request.GET.get("course") — if present, filter by course_id
    # If not, get all students
    # Pass students, courses (for filter links), and total count to template

    students = Student.objects.all()
    context = {
        "students": students,
        "total": students.count(),
    }
    return render(request, "student_list.html", context)


def student_detail(request, student_id):
    # TODO: use get_object_or_404 instead of the old for-loop
    student = get_object_or_404(Student, id=student_id)
    return render(request, "student_detail.html", {"student": student})


def add_student(request):
    if request.method == "POST":
        # TODO: get the Course object from request.POST.get("course_id")
        # TODO: use Student.objects.create(...) with the course FK
        # TODO: redirect to student_list
        pass

    # TODO: pass Course.objects.all() for the dropdown
    courses = Course.objects.all()
    return render(request, "add_student.html", {"courses": courses})


def course_list(request):
    # TODO: get all courses, render course_list.html
    pass


def course_detail(request, course_id):
    # TODO: get_object_or_404(Course, id=course_id)
    # TODO: pass course and course.students.all() to template
    pass


def delete_student(request, student_id):
    # TODO: get student, delete it, redirect to student_list
    pass


def edit_student(request, student_id):
    # TODO: GET — render edit form pre-filled with student data + all courses
    # TODO: POST — update fields from request.POST, save(), redirect to detail
    pass
