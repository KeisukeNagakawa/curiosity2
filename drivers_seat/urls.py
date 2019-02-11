from django.urls import path
from . import views
urlpatterns = [
    path('', views.drivers_view, name='drivers_view'),
]