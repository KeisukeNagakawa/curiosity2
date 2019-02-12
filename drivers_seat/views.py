from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def drivers_view(request):
    return render(request, "drivers_seat/view.html", {})


def forward(request):
    print("forward function is called in view.py")
    return HttpResponse('Return data to ajax call')


def backward(request):
    print("backward function is called in view.py")
    return HttpResponse('Return data to ajax call')


def left(request):
    print("left function is called in view.py")
    return HttpResponse('Return data to ajax call')


def right(request):
    print("right function is called in view.py")
    return HttpResponse('Return data to ajax call')


def stop(request):
    print("stop function is called in view.py")
    return HttpResponse('Return data to ajax call')
