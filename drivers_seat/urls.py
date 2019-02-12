from django.urls import path
from . import views
from . import test

urlpatterns = [
    path('', views.drivers_view, name='drivers_view'),
    path('forward', views.forward, name='forward'),
    path('backward', views.backward, name='backward'),
    path('left', views.left, name='left'),
    path('right', views.right, name='right'),
    path('stop', views.stop, name='stop'),
]
