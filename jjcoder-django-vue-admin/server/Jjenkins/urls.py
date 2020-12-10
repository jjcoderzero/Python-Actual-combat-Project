from django.urls import path
from Jjenkins import views

app_name = 'Jjenkins'

urlpatterns = [
    path('<str:job_name>', views.job_name_info),
]