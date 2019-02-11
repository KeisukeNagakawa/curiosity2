from django.shortcuts import render


# Create your views here.
def drivers_view(request):
    return render(request, "drivers_seat/view.html", {})
