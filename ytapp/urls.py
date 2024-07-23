"""
URL configuration for ythead project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from ytapp import views

from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', views.home, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('dashboard/home/', views.dashboard, name='dashboard'),
    path('dashboard/redditvideo/', views.dashboard_reddit, name='dashboard_reddit'),
    
    path('api/v0/getstory/', views.getstory, name='getstory'),
    path('api/v0/getstory/<str:subreddit>/', views.manual_getstory, name='manual_getstory'),
    path('api/v0/create/', views.create_text_image_js, name='create_text_image_js'),
    
    path('login/', views.user_login, name='login'),
    path('signup/', views.user_signup, name='signup'),
    path('logout/', views.user_logout, name='logout'),
    
    # path('testurl/', views.cleanup, name='cleanup'),
]

urlpatterns += staticfiles_urlpatterns()