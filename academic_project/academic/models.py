from django.db import models

# Modelo Teacher: representa a los docentes de la institución
class Teacher(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Course(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, related_name="courses")

    def __str__(self):
        return self.name


class Student(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class StudentCourse(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="enrollments")
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="enrollments")

    class Meta:
        unique_together = ("student", "course")

    def __str__(self):
        return f"{self.student} inscrito en {self.course}"
