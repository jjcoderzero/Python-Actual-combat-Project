from django.urls import path, include

urlpatterns = [
    path('jenkins/', include('Jjenkins.urls')),
]
