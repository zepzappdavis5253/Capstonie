from django.urls import path
from . import views


app_name = 'drumbeatapp'

urlpatterns = [
    path('', views.index, name='index'),
    path('get_instruments/', views.get_instruments, name='get_instruments'),
    path('get_scores/', views.get_scores, name='get_scores'),
    path('save_score', views.save_score, name='save_score'),
    path('login_page/', views.login_page, name='login_page'),
    path('protected/', views.protected, name='protected'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout, name='logout'),
    path('register_page/', views.register_page, name='register_page')
]