from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import HttpRequest
from django.shortcuts import get_object_or_404, redirect, render

from .forms import StudentForm
from .models import Course, Student


def login_view(request: HttpRequest):
    """Login page"""
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('student_list')
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    return render(request, 'login.html')


@login_required
def logout_view(request: HttpRequest):
    """Logout view"""
    logout(request)
    return redirect('home')


def home(request: HttpRequest):
    """Home page — welcome message."""
    return render(request, 'home.html')


def about(request: HttpRequest):
    """About page — course information."""
    return render(request, 'about.html')


@login_required
def student_list(request: HttpRequest):
    """List all students in a table."""
    search_query = request.GET.get('q', '').strip()
    student_queryset = Student.objects.select_related('course')

    if search_query:
        students = student_queryset.filter(Q(name__icontains=search_query) | Q(email__icontains=search_query))
    else:
        students = student_queryset.all()

    return render(
        request,
        'student_list.html',
        {
            'students': students,
            'count': students.count(),
            'search_query': search_query,
        },
    )


@login_required
def student_detail(request: HttpRequest, student_id: int):
    """Show details for a single student."""
    student = get_object_or_404(Student, id=student_id)
    return render(request, 'student_detail.html', {'student': student})


@login_required
def add_student(request: HttpRequest):
    """Show a form (GET) or process the submission (POST)."""
    if request.method == 'POST':
        form = StudentForm(request.POST)  # creates new student on form.save()
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm()

    return render(request, 'add_student.html', {'form': form})


@login_required
def delete_student(request: HttpRequest, student_id: int):
    """Delete a student and redirect to the list."""
    student = get_object_or_404(Student, id=student_id)
    if request.method == 'POST':
        student.delete()
    return redirect('student_list')


@login_required
def edit_student(request: HttpRequest, student_id: int):
    """Show a form pre-filled with existing data (GET) or process the submission (POST)."""
    student = get_object_or_404(Student, id=student_id)

    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)  # updates student passed to instance on form.save()
        if form.is_valid():
            form.save()
            return redirect('student_detail', student_id=student_id)
    else:
        form = StudentForm(instance=student)

    return render(request, 'edit_student.html', {'form': form, 'student': student})


@login_required
def course_list(request: HttpRequest):
    """List all courses in a table."""
    courses = Course.objects.all()
    return render(request, 'course_list.html', {'courses': courses, 'count': len(courses)})


@login_required
def course_detail(request: HttpRequest, course_id: int):
    """Show details for a single course."""
    course = get_object_or_404(Course, id=course_id)
    students = course.students.all()
    return render(request, 'course_detail.html', {'course': course, 'students': students})
