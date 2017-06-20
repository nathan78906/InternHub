import django
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "internHub.settings")
django.setup()


from sys import version_info
from hub.models import Job

py3 = version_info[0] > 2


if py3:
    skill = input("What is your skill level?(junior, intermediate, senior)? ")
else:
    skill = raw_input("What is your skill level?(junior, intermediate, senior)? ")
    
if skill == "junior":
    results = Job.objects.filter(junior=True)   
elif skill == "intermediate":
    results = Job.objects.filter(intermediate=True)
elif skill == "senior":
    results = Job.objects.filter(senior=True)

ret_string = ""
for row in results:
    ret_string += "Title: " + row.title 
    ret_string += ", Description: " + row.description
    ret_string += ", Employer: " + row.employer
    ret_string += "\n"
print(ret_string)
