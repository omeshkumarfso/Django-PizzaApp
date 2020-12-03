
from django.contrib import admin
from django.urls import path
from .views import todoview, addtask, deletetask, updatetaskview, updatetask

urlpatterns = [
    path('', todoview, name ='homepage'),
    path('addtask/', addtask),
    path('deletetask/<int:taskpk>/', deletetask),
    path('updatetaskview/<int:taskpk>/', updatetaskview),
    path('updatetask/<int:taskpk>/update/', updatetask)
]
