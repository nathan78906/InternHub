# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import datetime

from django.db import models
from django.utils.encoding import python_2_unicode_compatible

# Create your models here.
class Job(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    SKILL_CHOICES = (
        ('J', 'Junior'),
        ('I', 'Intermediate'),
        ('S', 'Senior'),
    )
    skill = models.CharField(max_length=1, choices=SKILL_CHOICES)
    employer = models.CharField(max_length=100)
    deadline = models.DateField(default=datetime.date.today)
	
    #@python_2_unicode_compatible
    def __str__(self):
        return self.title + " - " + self.employer

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
