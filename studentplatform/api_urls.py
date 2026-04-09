from django.urls import path

from .api_views import StudentListCreateAPIView, StudentRetrieveUpdateDestroyAPIView

urlpatterns = [  # type: ignore
    path(
        "students/",
        StudentListCreateAPIView.as_view(),
        name="student_detail",
    ),
    path(
        "students/<int:student_id>/",
        StudentRetrieveUpdateDestroyAPIView.as_view(),
        name="student_detail",
    ),
]
