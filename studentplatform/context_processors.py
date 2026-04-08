from django.http import HttpRequest

# from studentplatform.views import STUDENTS
from studentplatform.models import Students


def students_context(request: HttpRequest):
    students = Students.objects.all()
    return {"students_count": len(students)}
