from django.http import HttpRequest
from django.shortcuts import get_object_or_404, redirect, render

from .forms import StudentForm
from .models import Student


def home(request: HttpRequest):
    """Home page — welcome message."""
    return render(request, "home.html")


def about(request: HttpRequest):
    """About page — course information."""
    return render(request, "about.html")


def student_list(request: HttpRequest):
    """List all students in a table."""
    students = Student.objects.all()
    return render(
        request, "student_list.html", {"students": students, "count": len(students)}
    )


def student_detail(request: HttpRequest, student_id: int):
    """Show details for a single student."""
    student = get_object_or_404(Student, id=student_id)

    if request.method == "POST":
        student.delete()
        return redirect("student_list")
    return render(request, "student_detail.html", {"student": student})


def add_student(request: HttpRequest):
    """Show a form (GET) or process the submission (POST)."""
    if request.method == "POST":
        form = StudentForm(request.POST)  # creates new student on form.save()
        if form.is_valid():
            form.save()
            return redirect("student_list")
    else:
        form = StudentForm()

    return render(request, "add_student.html", {"form": form})


def edit_student(request: HttpRequest, student_id: int):
    """Show a form pre-filled with existing data (GET) or process the submission (POST)."""
    student = get_object_or_404(Student, id=student_id)

    if request.method == "POST":
        form = StudentForm(
            request.POST, instance=student
        )  # updates student passed to instance on form.save()
        if form.is_valid():
            form.save()
            return redirect("student_detail", student_id=student_id)
    else:
        form = StudentForm(instance=student)

    return render(request, "edit_student.html", {"form": form, "student": student})
