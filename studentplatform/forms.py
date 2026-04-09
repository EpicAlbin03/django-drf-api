from typing import cast

from django import forms
from django.db import models

from .models import Course, Student


class CourseChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj: models.Model) -> str:
        return cast(Course, obj).name


class StudentForm(forms.ModelForm):
    course = CourseChoiceField(
        queryset=Course.objects.all(),
        empty_label=None,
    )

    class Meta:
        model = Student
        fields = ["name", "email", "date_of_birth", "grade", "is_active", "course"]
        widgets = {
            "date_of_birth": forms.DateInput(attrs={"type": "date"}),
            "is_active": forms.CheckboxInput(
                attrs={
                    "class": "size-4 shrink-0 rounded-sm bg-primary text-primary-foreground accent-primary border border-primary ring-offset-background focus-visible:outline-hidden focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 disabled:cursor-not-allowed disabled:opacity-50"
                }
            ),
        }
