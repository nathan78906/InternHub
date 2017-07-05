from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^job/(?P<job_id>[0-9]+)/$', views.job_view, name='job_view'),
    url(r'^skill/(?P<skill>[\w-]+)/$', views.skill_filter, name='skill_filter'),
    url(r'^register/employer/$', views.register_employer, name='register_employer'),
    url(r'^register/student/$', views.register_student, name='register_student'),
]
