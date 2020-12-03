
from django.contrib import admin
from django.urls import path
from .views import helloworld, increment, decrement, reset

urlpatterns = [
    path('helloworld/',helloworld),
    path('increment/', increment),
    path('decrement/', decrement),
    path('reset/', reset)
]
