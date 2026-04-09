"""
Session 5 — Student Management Platform (Phase 3)
core/api_urls.py — NEW FILE

Create this in your core/ folder.
Wire up your API views with path() patterns.
"""

from django.urls import path
from .api_views import (
    StudentListCreateAPIView,
    StudentRetrieveUpdateDestroyAPIView,
    CourseListCreateAPIView,
    CourseRetrieveUpdateDestroyAPIView,
    # CourseStudentListAPIView,  # uncomment when implementing bonus
)

urlpatterns = [
    # TODO: add student endpoints
    # path('students/', ..., name='api-student-list'),
    # path('students/<int:pk>/', ..., name='api-student-detail'),

    # TODO: add course endpoints
    # path('courses/', ..., name='api-course-list'),
    # path('courses/<int:pk>/', ..., name='api-course-detail'),

    # Bonus: students in a course
    # path('courses/<int:pk>/students/', ..., name='api-course-students'),
]
