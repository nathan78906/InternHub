# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Job, Documents

# Register your models here.

admin.site.register(Job)
admin.site.register(Documents)