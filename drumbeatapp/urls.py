from django.urls import path
from . import views


app_name = 'drumbeatapp'

urlpatterns = [
  path('', views.index, name='index'),
  path('get_instruments', views.get_instruments, name='get_instruments')
]