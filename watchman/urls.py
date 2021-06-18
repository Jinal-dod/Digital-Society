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
path('',views.w_index, name='w_index'),
path('registration-page', views.registration_page, name='w_registration-page'),
path('register', views.register, name='register'),
path('w_login', views.w_login, name='w_login'),
path('w_login-evalute/', views.w_login_evalute, name='w_login-evalute'),
path('w-forgot-password-page/', views.w_forgot_password_page, name='w-forgot-password-page'),
path('w_send_otp/',views.w_send_otp, name='w-send-otp'),
path('w_reset_password/',views.w_reset_password, name='w-reset-password'),
path('w_logout/', views.w_logout, name='w_logout'),
path('w_view_notice/',views.w_view_notice, name='w_view_notice'),
path('w_view_events/',views.w_view_events, name='w_view_events'),
path('w-view-member/',views.w_view_member, name='w-view-member'),
path('w-view-member-profile<int:pk>/',views.w_view_member_profile, name='w-view-member-profile'),
path('w-view-photos/',views.w_view_photos, name='w-view-photos'),
path('w-view-videos/',views.w_view_videos, name='w-view-videos'),
path('w_profile/',views.w_profile, name='w_profile'),
path('w_profile_update/',views.w_profile_update, name='w_profile_update'),
path('add-visitor-page/',views.add_visitor_page, name='add_visitor_page'),
path('add-visitor/',views.add_visitor, name='add_visitor'),
path('w-view-visitors/',views.w_view_visitors, name='w-view-visitors'),
path('w-add-contect/',views.w_add_contect, name='w-add-contect'),




]
