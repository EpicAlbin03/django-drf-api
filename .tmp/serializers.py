"""
Session 5 — Student Management Platform (Phase 3)
core/serializers.py — NEW FILE

Create this in your core/ folder.
"""

from rest_framework import serializers
from .models import Student, Course


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        # TODO: set fields
        fields = []


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        # TODO: set fields
        fields = []
