from django.urls import path
from . import views

urlpatterns=[
    path('',views.home),
    path('home/',views.home),
    path('about/',views.about),
    path('contactus/',views.contactus),
    path('services/',views.services),
    path('adminlogin/',views.adminlogin),
    path('ourplacement/',views.ourplacement),
    path('gallery/',views.imagegallery),
    path('recruiters/', views.ourrecruiters),
    path('course/',views.course),
    path('faculty/',views.faculty),


]