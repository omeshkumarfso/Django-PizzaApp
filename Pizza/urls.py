from django.contrib import admin
from django.urls import path, include
from .views import adminloginview, adminhomepageview, authenticationadmin, logoutadmin, addpizza,deletepizza, homepageview

urlpatterns = [
    path('admin/', adminloginview,name='adminloginpage'),
    path('adminauthenticate/', authenticationadmin),
    path('admin/homepage/', adminhomepageview, name='adminhomepage'),
    path('adminlogout/',logoutadmin),
    path('addpizza/', addpizza),
    path('deletepizza/<int:pizzapk>/',deletepizza),
    path('',homepageview)
]
