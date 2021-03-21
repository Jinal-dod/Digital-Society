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
 path('', views.index, name='index'),  
 path('login/', views.login, name='login'), 
 path('login-evalute/', views.login_evalute, name='login-evalute'),
 path('logout/', views.logout, name='logout'),
 path('forgot-password/', views.forgot_password, name='forgot-password-page'),
 path('send-otp/', views.send_otp, name='send-otp'),
 path('reset-password/', views.reset_password, name='reset-password'),
 path('add-notice-page/', views.add_notice_page, name='add-notice-page'),
 path('add-notice/',views.add_notice, name='add-notice'),
 path('view-notice/',views.view_notice, name='view-notice'),
 path('profile/',views.profile, name='profile'),
 path('profile-update/',views.profile_update, name='profile-update'),
 path('add-events-page/', views.add_events_page, name='add-events-page'),
 path('add-events/',views.add_events, name='add-events'),
 path('view-events/',views.view_events, name='view-events'),
 path('add-member-page/', views.add_member_page, name='add-member-page'),
 path('add-member/',views.add_member, name='add-member'),
 path('view-member/',views.view_member, name='view-member'),
 path('view-member-profile<int:pk>/',views.view_member_profile, name='view-member-profile'),
 path('member-profile-update/',views.member_profile_update, name='member-profile-update'),
 path('watchman_list/',views.watchman_list, name='watchman_list'),
 path('ver_watch/<int:pk>',views.ver_watch, name='ver_watch'),

 
]
