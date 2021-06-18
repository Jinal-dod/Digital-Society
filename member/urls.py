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
path('', views.m_index, name='m_index'),  
path('login/', views.m_login, name='login'), 
path('login-evalute/', views.m_login_evalute, name='m-login-evalute'),
path('logout/', views.m_logout, name='m_logout'),
path('forgot-password/', views.m_forgot_password, name='m-forgot-password-page'),
path('send-otp/', views.m_send_otp, name='m-send-otp'),
path('reset-password/', views.m_reset_password, name='m-reset-password'),
path('mprofile/',views.m_profile, name='m_profile'),
path('mmember-profile-update/',views.m_profile_update, name='m-member-profile-update'),
path('m-view-member/',views.m_view_member, name='m-view-member'),
path('m-view-member-profile<int:pk>/',views.m_view_member_profile, name='m-view-member-profile'),
path('m-view-events/',views.m_view_events, name='m-view-events'),
path('m-view-notice/',views.m_view_notice, name='m-view-notice'),
path('m-add-complain-page/',views.m_add_complain_page, name='m-add-complain-page'),
path('m-add-complain/',views.m_add_complain, name='m-add-complain'),
path('m-view-complain/',views.m_view_complain, name='m-view-complain'),
path('delete-complain<int:pk>/',views.delete_complain, name='delete-complain'),
path('m-add-suggestion-page/',views.m_add_suggestion_page, name='m-add-suggestion-page'),
path('m-add-suggestion/',views.m_add_suggestion, name='m-add-suggestion'),
path('m-view-suggestion/',views.m_view_suggestion, name='m-view-suggestion'),
path('delete-suggestion<int:pk>/',views.delete_suggestion, name='delete-suggestion'),
path('m-view-photos/',views.m_view_photos, name='m-view-photos'),
path('m-view-videos/',views.m_view_videos, name='m-view-videos'),
path('m-view-visitor/',views.m_view_visitors, name='m-view-visitor'),
path('m-add-contect/',views.m_add_contect, name='m-add-contect'),
path('s-view-maintenance/', views.s_view_maintenance, name='s_view_maintenance'),
path('s-maintenance-list/', views.s_maintenance_list, name='s_maintenance_list'),
]