from django.urls import path

from . import views


urlpatterns = [
    path('', views.index ,name='index'),
    path('contact/', views.index ,name='index'),
    path('aboutus/', views.aboutus ,name='index'),
    path('jobsforyou/', views.index ,name='index'),
    path('cvpackage/', views.index ,name='index'),
    path('jobpackage/', views.index ,name='index'),
    path('login/', views.user_login ,name='register'),
    path('sucess/', views.sucess ,name='register'),
    path('logout/', views.user_logout ,name='register'),
    path('register/', views.register ,name='register'),


    
]