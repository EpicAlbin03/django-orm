"""
Session 3 — Student Management Platform (Phase 1)
core/views.py

Complete the views below. Each view should:
1. Prepare any data needed (from the STUDENTS list)
2. Return render() with the appropriate template and context
"""

from django.http import HttpRequest
from django.shortcuts import get_object_or_404, redirect, render

from studentplatform.forms import StudentForm
from studentplatform.models import Students

# class Student(TypedDict):
#     id: int
#     name: str
#     email: str
#     course: str
#     grade: str


# STUDENTS: list[Student] = [
#     {
#         "id": 1,
#         "name": "Ada Lovelace",
#         "email": "ada@example.com",
#         "course": "Computer Science",
#         "grade": "A",
#     },
#     {
#         "id": 2,
#         "name": "Alan Turing",
#         "email": "alan@example.com",
#         "course": "Mathematics",
#         "grade": "A+",
#     },
#     {
#         "id": 3,
#         "name": "Grace Hopper",
#         "email": "grace@example.com",
#         "course": "Engineering",
#         "grade": "B+",
#     },
#     {
#         "id": 4,
#         "name": "Linus Torvalds",
#         "email": "linus@example.com",
#         "course": "Operating Systems",
#         "grade": "A",
#     },
# ]


def home(request: HttpRequest):
    """Home page — welcome message."""
    return render(request, "home.html")


def about(request: HttpRequest):
    """About page — course information."""
    return render(request, "about.html")


def student_list(request: HttpRequest):
    """List all students in a table."""
    students = Students.objects.all()
    return render(
        request, "student_list.html", {"students": students, "count": len(students)}
    )


def student_detail(request: HttpRequest, student_id: int):
    """Show details for a single student."""
    # student = next((s for s in students if s["id"] == student_id), None)

    # student = Students.objects.filter(id=student_id).first()
    # if student is None:
    #     return HttpResponse("Student not found", status=404)
    student = get_object_or_404(Students, id=student_id)

    if request.method == "POST":
        # STUDENTS.remove(student)
        student.delete()
        return redirect("student_list")
    return render(request, "student_detail.html", {"student": student})


def add_student(request: HttpRequest):
    """Show a form (GET) or process the submission (POST)."""
    if request.method == "POST":
        # STUDENTS.append(
        #     {
        #         "id": len(STUDENTS) + 1,
        #         "name": request.POST.get("name", ""),
        #         "email": request.POST.get("email", ""),
        #         "course": request.POST.get("course", ""),
        #         "grade": request.POST.get("grade", ""),
        #     }
        # )
        Students.objects.create(
            name=request.POST.get("name", ""),
            email=request.POST.get("email", ""),
            course=request.POST.get("course", ""),
            grade=request.POST.get("grade", ""),
        )
        return redirect("student_list")

    form = StudentForm()
    return render(request, "add_student.html", {"form": form})


def edit_student(request: HttpRequest, student_id: int):
    """Show a form pre-filled with existing data (GET) or process the submission (POST)."""
    # student = next((s for s in STUDENTS if s["id"] == student_id), None)

    # student = Students.objects.filter(id=student_id).first()
    # if student is None:
    #     return HttpResponse("Student not found", status=404)
    student = get_object_or_404(Students, id=student_id)

    if request.method == "POST":
        # student["name"] = request.POST.get("name", "")
        # student["email"] = request.POST.get("email", "")
        # student["course"] = request.POST.get("course", "")
        # student["grade"] = request.POST.get("grade", "")
        student.name = request.POST.get("name", "")
        student.email = request.POST.get("email", "")
        student.course = request.POST.get("course", "")
        student.grade = request.POST.get("grade", "")
        student.save()
        return redirect("student_detail", student_id=student_id)

    form = StudentForm(initial=student.__dict__)
    return render(request, "edit_student.html", {"form": form, "student": student})
