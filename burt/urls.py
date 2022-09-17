from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('burt', views.burt_, name='burt_')
]