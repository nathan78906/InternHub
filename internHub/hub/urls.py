from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^student/$', views.index, name='index'),
    url(r'^student/register/$', views.reg_student, name='reg_student'),
    url(r'^student/login/$', views.login_stu, name='login_stu'),
    url(r'^student/registered/$', views.register_student, name='register_student'),
    url(r'^student/redirect/$', views.login_student, name='login_student'),
    url(r'^student/job/(?P<job_id>[0-9]+)/$', views.job_view, name='job_view'),
    url(r'^student/job/(?P<job_id>[0-9]+)/apply/$', views.model_form_upload, name='model_form_upload'),
    url(r'^student/skill/(?P<skill>[\w-]+)/$', views.skill_filter, name='skill_filter'),
    url(r'^student/applications/$', views.student_applications, name='student_applications'),
    url(r'^student/applications/(?P<job_id>[0-9]+)/$', views.job_desc_view, name='job_desc_view'),
    url(r'^student/logout/$', views.logout_stu, name='student_logout'),
    url(r'^employer/$', views.index_emp, name='index_emp'),
    url(r'^employer/register/$', views.reg_employer, name='reg_employer'),
    url(r'^employer/registered/$', views.register_employer, name='register_employer'),
    url(r'^employer/login/$', views.login_emp, name='login_emp'),
    url(r'^employer/logout/$', views.logout_emp, name='employer_logout'),
    url(r'^employer/redirect/$', views.login_employer, name='login_employer'),
    url(r'^employer/skill/(?P<skill>[\w-]+)/$', views.skill_filter_emp, name='skill_filter_emp'),
    url(r'^employer/job/(?P<job_id>[0-9]+)/$', views.job_view_emp, name='job_view_emp'),
    url(r'^employer/job/(?P<job_id>[0-9]+)/applications/$', views.job_applications, name='job_applications'),
    url(r'^employer/new_job/$', views.create_job, name='create_job'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

