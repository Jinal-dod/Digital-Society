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
 path('', views.m_index, name='index'),  
 path('login/', views.m_login, name='login'), 
 path('login-evalute/', views.m_login_evalute, name='m-login-evalute'),
 path('logout/', views.m_logout, name='m_logout'),
 path('forgot-password/', views.m_forgot_password, name='forgot-password-page'),
 path('send-otp/', views.m_send_otp, name='send-otp'),
 path('reset-password/', views.m_reset_password, name='reset-password'),
 path('mprofile/',views.m_profile, name='m_profile'),
 path('mmember-profile-update/',views.m_profile_update, name='m-member-profile-update'),

]
