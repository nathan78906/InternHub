from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Job(models.Model):
    jobId = models.IntegerField()
    title = models.CharField(max_length=100)
    description = models.TextField()
    junior = models.BooleanField()
    intermediate = models.BooleanField()
    senior = models.BooleanField()
    employer = models.CharField(max_length=100)

class Employer(models.Model):
    employerId = models.IntegerField()
    name = models.CharField(max_length=50)
    tags = models.CharField(max_length=20)

class Student(models.Model):
    studentId = models.IntegerField()
    lastName = models.CharField(max_length=30)
    firstName = models.CharField(max_length=30)
    schoolId = models.IntegerField()

class School(models.Model):
    schoolId = models.IntegerField()
    name = models.CharField(max_length=70)
    coordinator = models.CharField(max_length=50)
    