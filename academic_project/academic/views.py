from django.shortcuts import render
from rest_framework import viewsets
from .models import Teacher, Course, Student, StudentCourse
from .serializers import TeacherSerializer, CourseSerializer, StudentSerializer, StudentCourseSerializer

# --- Endpoints API con DRF ---
class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentCourseViewSet(viewsets.ModelViewSet):
    queryset = StudentCourse.objects.all()
    serializer_class = StudentCourseSerializer


# --- Vistas HTML ---
def home(request):
    return render(request, "academic/base.html")

def courses_view(request):
    return render(request, "academic/courses.html")

def students_view(request):
    return render(request, "academic/students.html")

def teachers_view(request):
    return render(request, "academic/teachers.html")

def studentcourses_view(request):
    return render(request, "academic/studentcourses.html")
