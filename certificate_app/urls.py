from django.urls import path
from . import views
from django.views import generic

urlpatterns = [
    path('',views.HomepageView.as_view(),name='home'),
    path('generate_certificate/',views.generate_certificate,name='certificate_form'),
    path('search-records/',views.search_records,name='search_records'),
    path('certificate-detail/<int:id>/',views.certificate_detail,name='certificate_detail')
]
