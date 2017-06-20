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
    skill = input("Enter the job skill level(junior, intermediate, or senior): ")
    employerName = input("Enter company name: ")
else:
    while line != "new job":
        line = raw_input("")

    jobID = raw_input("Enter a job ID: ")
    jobTitle = raw_input("Enter the job title: ")
    desc = raw_input("Enter the job description: ")
    skill = raw_input("Enter the job skill level(junior, intermediate, or senior): ")
    employerName = raw_input("Enter company name: ")

if skill == "junior":
    juniorBool = True
    intermediateBool = False
    seniorBool = False
elif skill == "intermediate":
    juniorBool = False
    intermediateBool = True
    seniorBool = False
elif skill == "senior":
    juniorBool = False
    intermediateBool = False
    seniorBool = True

a = Job(jobId=int(jobID), title=jobTitle, description=desc, junior=juniorBool, \
            intermediate=intermediateBool, senior=seniorBool, employer=employerName)
a.save()
    
    
    

