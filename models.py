"""
Session 4 — Student Management Platform (Phase 2)
core/models.py

Copy this into your core/models.py and fill in the TODOs.
"""

from django.db import models


class Course(models.Model):
    """A course that students can enrol in."""

    # TODO: add fields
    # name — CharField, max_length=100
    # code — CharField, max_length=10, unique=True
    # description — TextField, blank=True

    def __str__(self):
        # TODO: return f"{self.code} — {self.name}"
        pass


class Student(models.Model):
    """A student enrolled in a course."""

    # TODO: add fields
    # name — CharField, max_length=100
    # email — EmailField, unique=True
    # date_of_birth — DateField, null=True, blank=True
    # grade — CharField, max_length=2, default="N/A"
    # is_active — BooleanField, default=True
    # course — ForeignKey(Course, on_delete=models.CASCADE, related_name="students")
    # created_at — DateTimeField, auto_now_add=True

    def __str__(self):
        # TODO: return self.name
        pass
