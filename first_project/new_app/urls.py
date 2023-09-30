from django.urls import path
from .views import index,contact,project,resume

urlpatterns = [
    path('',index, name='index'),
    path('contact/',contact, name='conatct'),
    path('project/',project, name='projects'),
    path('resume/',resume, name='resume'),
]
