from __future__ import unicode_literals

from django.db import models

from djangotoolbox.fields import ListField

# Create your models here.

class Job(models.Model):
    jobId = models.IntegerField()
    title = models.CharField()
    description = models.TextField()
    tags = ListField()
    employer = CharField()

class Employer(models.Model):
    employerId = models.IntegerField()
    name = models.CharField()
    tags = ListField()

class Student(models.Model):
    studentId = models.IntegerField()
    lastName = models.CharField()
    firstName = models.CharField()
    schoolId = models.IntegerField()

class School(models.Model):
    schoolId = models.IntegerField()
    name = models.CharField()
    coordinators = ListField()
    