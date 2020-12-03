from django.shortcuts import render, redirect
from .models import CounterModel

# Create your views here. 

obj = CounterModel.objects.filter(id = 1)[0]

def helloworld(request):
    ourNumber = int(obj.number)
    context = {'number': ourNumber}
    return render(request, "helloworld/helloworld.html", context)

def increment(request):
    ourNumber = int(obj.number)
    if ourNumber < 10:
        ourNumber = ourNumber + 1
        obj.number = ourNumber
    obj.save()
    return redirect(request.META['HTTP_REFERER'])

def decrement(request):
    ourNumber = int(obj.number)
    if ourNumber > 0:
        ourNumber = ourNumber - 1
        obj.number = ourNumber
    else:
        obj.number = 0
    obj.save()
    return redirect(request.META['HTTP_REFERER'])

def reset(request):
    obj.number = 0
    obj.save()
    return redirect(request.META['HTTP_REFERER'])