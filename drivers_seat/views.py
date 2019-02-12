from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def drivers_view(request):
    return render(request, "drivers_seat/view.html", {})


def forward(request):
    # Code to run
    # More code to run
    print("forward function is called")
    return HttpResponse('Return data to ajax call')
