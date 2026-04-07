"""
Session 4 — Student Management Platform (Phase 2)
core/urls.py

Copy this into your core/urls.py, replacing the old version.
Uncomment the new routes as you implement them.
"""

from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("students/", views.student_list, name="student_list"),
    path("students/add/", views.add_student, name="add_student"),
    path("students/<int:student_id>/", views.student_detail, name="student_detail"),

    # Uncomment these as you implement them:
    # path("courses/", views.course_list, name="course_list"),
    # path("courses/<int:course_id>/", views.course_detail, name="course_detail"),
    # path("students/<int:student_id>/delete/", views.delete_student, name="delete_student"),
    # path("students/<int:student_id>/edit/", views.edit_student, name="edit_student"),
]
