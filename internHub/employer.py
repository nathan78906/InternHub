import django
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "internHub.settings")
django.setup()


from sys import version_info
from hub.models import Job

py3 = version_info[0] > 2

line = ""

if py3:
    while line != "new job":
        line = input("")

    jobID = input("Enter a job ID: ")
    jobTitle = input("Enter the job title: ")
    desc = input("Enter the job description: ")
    juniorBool = input("Is this a junior job?(True or False): ")
    intermediateBool = input("Is this an intermediate job?(True or False): ")
    seniorBool = input("Is this a senior job?(True or False): ")
    employerName = input("Enter company name: ")
else:
    while line != "new job":
        line = raw_input("")

    jobID = raw_input("Enter a job ID: ")
    jobTitle = raw_input("Enter the job title: ")
    desc = raw_input("Enter the job description: ")
    juniorBool = raw_input("Is this a junior job?(True or False): ")
    intermediateBool = raw_input("Is this an intermediate job?(True or False): ")
    seniorBool = raw_input("Is this a senior job?(True or False): ")
    employerName = raw_input("Enter company name: ")

a = Job(jobId=int(jobID), title=jobTitle, description=desc, junior=juniorBool, \
            intermediate=intermediateBool, senior=seniorBool, employer=employerName)
a.save()
    
    
    

