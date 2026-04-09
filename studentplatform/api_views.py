from rest_framework import generics

from studentplatform.serializers import CourseSerializer, StudentSerializer

from .models import Course, Student


# GET, POST
class StudentListCreateAPIView(generics.ListCreateAPIView[Student]):
    queryset = Student.objects.select_related("course").all()
    serializer_class = StudentSerializer


# GET, PUT, PATCH, DELETE
class StudentRetrieveUpdateDestroyAPIView(
    generics.RetrieveUpdateDestroyAPIView[Student]
):
    queryset = Student.objects.select_related("course").all()
    serializer_class = StudentSerializer


class CourseListCreateAPIView(generics.ListCreateAPIView[Course]):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class CourseRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView[Course]):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
