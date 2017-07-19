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

def home(request):
    return render(request, 'hub/home.html')

def reg_employer(request):
    job_list = Job.objects.all().order_by('deadline')
    context = {
        'mesage': "Welcome new Employer",
    }
    return render(request, 'hub/register_employer.html', context)

def reg_student(request):
    job_list = Job.objects.all().order_by('deadline')
    context = {
        'mesage': "Welcome",
    }
    return render(request, 'hub/register_student.html', context)

def index(request):
    job_list = Job.objects.all().order_by('deadline')
    context = {
        'job_list': job_list,
    }
    return render(request, 'hub/index.html', context)

def index_emp(request):
    employer = Employer.objects.all().filter(user=request.user)
    job_list = Job.objects.all().filter(employer=employer)
    context = {
        'job_list': job_list,
    }
    return render(request, 'hub/employer_home.html', context)
    
def job_view(request, job_id):
    job = Job.objects.get(id=job_id)
    context = {
        'job': job,
    }
    return render(request, 'hub/job.html', context)

def job_view_emp(request, job_id):
    job = Job.objects.get(id=job_id)
    context = {
        'job': job,
    }
    return render(request, 'hub/job_emp.html', context)

def job_applications(request, job_id):
    job = Job.objects.get(id=job_id)
    applications = Documents.objects.filter(job=job)
    context = {
        'applications': applications,
    }
    return render(request, 'hub/job_applications.html', context)
    
def job_desc_view(request, job_id):
    job = Job.objects.get(id=job_id)
    context = {
        'job': job,
    }
    return render(request, 'hub/job_desc.html', context)

def skill_filter(request, skill):
    job_list = Job.objects.filter(skill=skill)
    context = {
        'job_list': job_list,
    }
    return render(request, 'hub/index.html', context)
    
def skill_filter_emp(request, skill):
    employer = Employer.objects.all().filter(user=request.user)
    job_list = Job.objects.all().filter(skill=skill, employer=employer)
    context = {
        'job_list': job_list,
    }
    return render(request, 'hub/employer_home.html', context)

def student_applications(request):
    job_list = Documents.objects.filter(user=request.user)
    context = {
        'job_list': job_list,
    }
    return render(request, 'hub/student_applications.html', context)

def register_employer(request):
    try:
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        company_name = request.POST['company']
    except:
        return HttpResponse("Missing a required field")
    else:
        new_user = User.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name, is_staff=False)
        new_user.save()
        try:
            company = Company.objects.get(company_name=company_name)
        except:
            company = Company(company_name=company_name)
            company.save()
        new_employer = Employer(user=new_user, company=company)
        new_employer.save()
        
        job_list = Job.objects.all().order_by('deadline')
        context = {
            'job_list': job_list,
        }
        return render(request, 'hub/employer_login.html', context)
        
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
        return render(request, 'hub/student_login.html', context)

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
    username = request.POST.get("username", "")
    password = request.POST.get("password", "")
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
        
def login_stu(request):
    context = {
        'mesage': "Welcome",
    }
    return render(request, 'hub/student_login.html', context)

def login_emp(request):
    context = {
        'mesage': "Welcome",
    }
    return render(request, 'hub/employer_login.html', context)

def login_employer(request):
    username = request.POST.get("username", "")
    password = request.POST.get("password", "")
    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)

        employer = Employer.objects.all().filter(user=request.user)
        job_list = Job.objects.all().filter(employer=employer)
        context = {
            'job_list': job_list,
        }
        return render(request, 'hub/employer_home.html', context)
    else:
        return HttpResponse("Log in failed. Invalid credentials")

def logout_stu(request):
    logout(request)
    # Redirect to a home page here.
    return redirect('home')
    
def logout_emp(request):
    logout(request)
    # Redirect to a home page here.
    return redirect('home')
