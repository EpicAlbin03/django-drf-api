from django.http import HttpRequest
from django.shortcuts import get_object_or_404, redirect, render

from .forms import StudentForm
from .models import Course, Student


def home(request: HttpRequest):
    """Home page — welcome message."""
    return render(request, "home.html")


def about(request: HttpRequest):
    """About page — course information."""
    return render(request, "about.html")


def student_list(request: HttpRequest):
    """List all students in a table."""
    students = Student.objects.all()
    return render(
        request, "student_list.html", {"students": students, "count": len(students)}
    )


def student_detail(request: HttpRequest, student_id: int):
    """Show details for a single student."""
    student = get_object_or_404(Student, id=student_id)
    return render(request, "student_detail.html", {"student": student})


def add_student(request: HttpRequest):
    """Show a form (GET) or process the submission (POST)."""
    if request.method == "POST":
        form = StudentForm(request.POST)  # creates new student on form.save()
        if form.is_valid():
            form.save()
            return redirect("student_list")
    else:
        form = StudentForm()

    return render(request, "add_student.html", {"form": form})


def delete_student(request: HttpRequest, student_id: int):
    """Delete a student and redirect to the list."""
    student = get_object_or_404(Student, id=student_id)
    if request.method == "POST":
        student.delete()
    return redirect("student_list")


def edit_student(request: HttpRequest, student_id: int):
    """Show a form pre-filled with existing data (GET) or process the submission (POST)."""
    student = get_object_or_404(Student, id=student_id)

    if request.method == "POST":
        form = StudentForm(
            request.POST, instance=student
        )  # updates student passed to instance on form.save()
        if form.is_valid():
            form.save()
            return redirect("student_detail", student_id=student_id)
    else:
        form = StudentForm(instance=student)

    return render(request, "edit_student.html", {"form": form, "student": student})


def course_list(request: HttpRequest):
    """List all courses in a table."""
    courses = Course.objects.all()
    return render(
        request, "course_list.html", {"courses": courses, "count": len(courses)}
    )


def course_detail(request: HttpRequest, course_id: int):
    """Show details for a single course."""
    course = get_object_or_404(Course, id=course_id)
    students = course.students.all()
    return render(
        request, "course_detail.html", {"course": course, "students": students}
    )
