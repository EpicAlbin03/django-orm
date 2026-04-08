from django import forms

from .models import Student


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ["name", "email", "date_of_birth", "grade", "is_active", "course"]
        widgets = {
            "date_of_birth": forms.DateInput(attrs={"type": "date"}),
        }
