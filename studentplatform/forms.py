from django import forms


class StudentForm(forms.Form):
    name = forms.CharField(label="Name", max_length=100)
    email = forms.EmailField(label="Email")
    course = forms.CharField(label="Course", max_length=100)
    grade = forms.CharField(
        label="Grade",
        max_length=2,
    )
