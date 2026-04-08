"""
Session 5 — Student Management Platform (Phase 3)
core/api_views.py — NEW FILE

Create this in your core/ folder.
Use DRF generic views: ListCreateAPIView and RetrieveUpdateDestroyAPIView.
"""

from rest_framework import generics
from .models import Student, Course
from .serializers import StudentSerializer, CourseSerializer


# ──── Student endpoints ────

class StudentListCreateAPIView(generics.ListCreateAPIView):
    # TODO: set queryset and serializer_class
    pass


class StudentRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    # TODO: set queryset and serializer_class
    pass


# ──── Course endpoints ────

class CourseListCreateAPIView(generics.ListCreateAPIView):
    # TODO: set queryset and serializer_class
    pass


class CourseRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    # TODO: set queryset and serializer_class
    pass


# ──── Bonus: nested endpoint ────

# class CourseStudentListAPIView(generics.ListAPIView):
#     # TODO: list students for a specific course
#     # Hint: override get_queryset() to filter by course pk
#     pass
