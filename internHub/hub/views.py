# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User

# Create your views here.
from .models import Job
from .models import Employer
from .models import Company
from .models import Student 

def index(request):
    job_list = Job.objects.all().order_by('deadline')
    context = {
        'mesage': "Welcome",
    }
    return render(request, 'hub/register.html', context)

def job_view(request, job_id):
    job = Job.objects.get(id=job_id)
    context = {
        'job': job,
    }
    return render(request, 'hub/job.html', context)

def skill_filter(request, skill):
    job_list = Job.objects.filter(skill=skill)
    context = {
        'job_list': job_list,
    }
    return render(request, 'hub/index.html', context)

def register_employer(request):
    try:
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        company_name = request.POST['company_name']
        title = request.POST['title']
    except:
        return HttpResponse("Missing a required field")
    else:
        new_user = User(username=username, password=password, email=email, first_name=first_name, last_name=last_name, is_staff=False)
        new_user.save()
        company = Company.objects.filter(company_name=company_name)
        new_employer = Employer(user=new_user, company=company)
        new_employer.save()

        return HttpResponse("Your new employer account was successfully created!")
        
def register_student(request):
    try:
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        school = request.POST['school']
    except:
        return HttpResponse("Missing a required field")
    else:
        new_user = User(username=username, password=password, email=email, first_name=first_name, last_name=last_name, is_staff=False)
        new_user.save()
        new_student = Student(user=new_user)
        new_student.save()

        job_list = Job.objects.all().order_by('deadline')
        context = {
            'job_list': job_list,
        }
        return render(request, 'hub/index.html', context)
