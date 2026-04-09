from rest_framework import generics

from studentplatform.serializers import StudentSerializer

from .models import Student


class StudentListCreateAPIView(generics.ListCreateAPIView):
    queryset = Student.objects.select_related("course").all()
    serializer_class = StudentSerializer


class StudentRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.select_related("course").all()
    serializer_class = StudentSerializer
