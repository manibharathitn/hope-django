from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=200)
    dob = models.DateField()
    address = models.CharField(max_length=200)
    class Meta:
        db_table = 'student'

class Mark(models.Model):
    student = models.ForeignKey('Student', db_column='student_id', on_delete=models.SET_NULL, null=True)
    subject = models.CharField(max_length=200)
    mark = models.IntegerField()
    class Meta:
        db_table = 'mark'


