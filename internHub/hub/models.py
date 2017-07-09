# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import datetime

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.contrib.auth.models import User

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

class Company(models.Model):
    company_name = models.CharField(max_length=50)
    
class Employer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=None)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, default=None)

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=None)
    program = models.CharField(max_length=150, null=True)
    year_of_study = models.IntegerField(null=True)
    year_of_graduation = models.IntegerField(null=True)

class School(models.Model):
    name = models.CharField(max_length=100)

class Documents(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE, default=None)
    resume = models.FileField(upload_to='resumes/')
    cover_letter = models.FileField(upload_to='cover_letters/', blank=True, null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    
    #@python_2_unicode_compatible
    def __str__(self):
        return self.job.title + " - " + str(self.uploaded_at)