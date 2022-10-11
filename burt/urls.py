from django.urls import path
from . import views

urlpatterns = [
    path('', views.new_home, name='new_home'),
    path('select_type', views.home, name='home'),
    path('burt', views.burt_, name='burt_'),
    path('burt2/<int:pk>', views.burt__, name='burt__'),
    path('query_boss/<int:num_of_tables>/<int:number_of_rows>/<int:number_of_columns>', views.query_boss, name='query_boss')
]