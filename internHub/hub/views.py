# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout, get_user
from django.conf import settings
from django.core.files.storage import FileSystemStorage

# Create your views here.
from .models import Job
from .models import Employer
from .models import Company
from .models import Student 
from .models import Documents

from .forms import DocumentForm

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
        new_user = User.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name, is_staff=False)
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
        new_user = User.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name, is_staff=False)
        new_user.save()
        new_student = Student(user=new_user)
        new_student.save()

        job_list = Job.objects.all().order_by('deadline')
        context = {
            'job_list': job_list,
        }
        return render(request, 'hub/index.html', context)

def model_form_upload(request, job_id):
    job = Job.objects.get(id=job_id)
    user = request.user
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)

        if form.is_valid():
            application = form.save(commit=False)  
            application.job = job
            application.user = user
            application.save()
            form.save_m2m()
            return redirect('job_view', job_id)
    else:
        form = DocumentForm()
    return render(request, 'hub/apply.html', {
        'form': form,
        'job': job,
        'user': user,
    })

def login_student(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)

        job_list = Job.objects.all().order_by('deadline')
        context = {
            'job_list': job_list,
        }
        return render(request, 'hub/index.html', context)
    else:
        return HttpResponse("Log in failed. Invalid credentials")
        
def login_student2(request):
    job_list = Job.objects.all().order_by('deadline')
    context = {
        'mesage': "Welcome",
    }
    return render(request, 'hub/student_login.html', context)

def logout_view(request):
    logout(request)
    # Redirect to a home page here.