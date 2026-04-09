from django.urls import path

from .api_views import (
    CourseListCreateAPIView,
    CourseRetrieveUpdateDestroyAPIView,
    CourseStudentListAPIView,
    StudentListCreateAPIView,
    StudentRetrieveUpdateDestroyAPIView,
)

# pk = primary key
urlpatterns = [
    path(
        "students/",
        StudentListCreateAPIView.as_view(),
    ),
    path(
        "students/<int:pk>/",
        StudentRetrieveUpdateDestroyAPIView.as_view(),
    ),
    path(
        "courses/",
        CourseListCreateAPIView.as_view(),
    ),
    path(
        "courses/<int:pk>/",
        CourseRetrieveUpdateDestroyAPIView.as_view(),
    ),
    path(
        "courses/<int:pk>/students/",
        CourseStudentListAPIView.as_view(),
    ),
]
