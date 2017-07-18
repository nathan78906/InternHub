# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Job, Documents, Employer, Company

# Register your models here.

admin.site.register(Job)
admin.site.register(Documents)
admin.site.register(Employer)
admin.site.register(Company)