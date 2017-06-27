# -*- coding: utf-8 -*-
from __future__ import unicode_literals

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
	
    #@python_2_unicode_compatible
    def __str__(self):
        return self.title + " - " + self.employer

