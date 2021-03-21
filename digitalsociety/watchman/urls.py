"""digitalsociety URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from . import views

urlpatterns = [
    path('', views.registration_page, name='w_registration-page'),
    path('register', views.register, name='register'),
    path('w_login', views.w_login, name='w_login'),
    path('w_login-evalute/', views.w_login_evalute, name='w_login-evalute'),
 path('w_logout/', views.w_logout, name='w_logout'),
 
]
