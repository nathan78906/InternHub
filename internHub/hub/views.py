# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
from .models import Job

def index(request):
    job_list = Job.objects.all()
    context = {
        'job_list': job_list,
    }
    return render(request, 'hub/index.html', context)

def detail(request, job_id):
    return HttpResponse("You're looking at job %s." % job_id)
