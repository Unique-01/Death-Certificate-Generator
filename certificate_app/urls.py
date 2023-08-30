from django.urls import path
from . import views

urlpatterns = [
    path('',views.HomepageView.as_view(),name='home'),
    path('generate_certificate/',views.generate_certificate,name='certificate_form'),
    path('search-records/',views.search_records,name='search_records'),
]
