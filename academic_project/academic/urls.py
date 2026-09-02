from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('courses/', views.courses_view, name="courses"),
    path('students/', views.students_view, name="students"),
    path('teachers/', views.teachers_view, name="teachers"),
    path('studentcourses/', views.studentcourses_view, name="studentcourses"),
]
