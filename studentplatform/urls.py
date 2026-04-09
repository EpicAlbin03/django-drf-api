from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [  # type: ignore
    path("admin/", admin.site.urls),
    path("", views.home, name="home"),
    path("students/", views.student_list, name="student_list"),
    path("students/<int:student_id>/", views.student_detail, name="student_detail"),
    path("students/add/", views.add_student, name="add_student"),
    path(
        "students/<int:student_id>/delete/", views.delete_student, name="delete_student"
    ),
    path("students/<int:student_id>/edit/", views.edit_student, name="edit_student"),
    path("courses/", views.course_list, name="course_list"),
    path("courses/<int:course_id>/", views.course_detail, name="course_detail"),
]
