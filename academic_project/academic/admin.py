# academic/admin.py
from django.contrib import admin
from .models import Teacher, Course, Student, StudentCourse

# Registrar cada modelo para que aparezca en el panel de administración
admin.site.register(Teacher)
admin.site.register(Course)
admin.site.register(Student)
admin.site.register(StudentCourse)
