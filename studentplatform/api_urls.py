from django.urls import path

from .api_views import (
    CourseListCreateAPIView,
    CourseRetrieveUpdateDestroyAPIView,
    StudentListCreateAPIView,
    StudentRetrieveUpdateDestroyAPIView,
)

urlpatterns = [  # type: ignore
    path(
        "students/",
        StudentListCreateAPIView.as_view(),
    ),
    path(
        "students/<int:student_id>/",
        StudentRetrieveUpdateDestroyAPIView.as_view(),
    ),
    path(
        "courses/",
        CourseListCreateAPIView.as_view(),
    ),
    path(
        "courses/<int:course_id>/",
        CourseRetrieveUpdateDestroyAPIView.as_view(),
    ),
]
