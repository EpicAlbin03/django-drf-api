from rest_framework import serializers

from .models import Course, Student


class StudentSerializer(serializers.ModelSerializer[Student]):
    class Meta:
        model = Student
        fields = "__all__"


class CourseSerializer(serializers.ModelSerializer[Course]):
    class Meta:
        model = Course
        fields = "__all__"
