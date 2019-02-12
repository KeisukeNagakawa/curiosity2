from django.urls import path
from . import views
from . import test
urlpatterns = [
    path('', views.drivers_view, name='drivers_view'),
    # path('forward', views.forward, name='forward')
    path('forward', views.forward, name='test')
]