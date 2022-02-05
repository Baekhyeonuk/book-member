from django.db import models
from django.utils import timezone

# Create your models here.

class Student(models.Model):
	student_name = models.CharField(max_length=200, unique=True)
	student_age = models.IntegerField(default=20)
	student_tel = models.CharField(max_length=200)
	student_addr = models.CharField(max_length=200)

	

	def __str__(self):
		return self.student_name


class Subject(models.Model):
	student = models.ForeignKey(Student, on_delete=models.CASCADE)
	subject_text = models.CharField(max_length=200)
	subject_date = models.DateTimeField(default=timezone.now)
	subject_ovew = models.TextField(null=True,default='')

	def __str__(self):
		return self.subject_text
