from django.urls import path
from . import views

urlpatterns = [
    path('generate_certificate/',views.generate_certificate,name='certificate_form')
]
