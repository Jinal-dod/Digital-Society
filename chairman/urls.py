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
 path('', views.loginpage, name='loginpage'),   
 path('index/', views.index, name='index'),  
 path('login/', views.login, name='login'), 
 path('login-evalute/', views.login_evalute, name='login-evalute'),
 path('logout/', views.logout, name='logout'),

 path('forgot-password/', views.forgot_password, name='forgot-password-page'),
 path('send-otp/', views.send_otp, name='send-otp'),
 path('reset-password/', views.reset_password, name='reset-password'),

 path('add-notice/',views.add_notice, name='add-notice'),
 path('view-notice/',views.view_notice, name='view-notice'),
 path('delete-notice<int:pk>/',views.delete_notice, name='delete-notice'),

 path('profile/',views.profile, name='profile'),
 path('profile-update/',views.profile_update, name='profile-update'),

 path('add-events/',views.add_events, name='add-events'),
 path('view-events/',views.view_events, name='view-events'),
 path('delete-event<int:pk>/',views.delete_event, name='delete-event'),

 path('add-member/',views.add_member, name='add-member'),
 path('view-member/',views.view_member, name='view-member'),
 path('view-member-profile<int:pk>/',views.view_member_profile, name='view-member-profile'),
 path('member-profile-update-page<int:pk>/',views.member_profile_update_page, name='member-profile-update-page'),
 path('member-profile-update<int:pk>/',views.member_profile_update, name='member-profile-update'),
 path('delete-member/',views.delete_member, name='delete-member'),
 
 path('watchman_list/',views.watchman_list, name='watchman_list'),
 path('ver_watch/<int:pk>',views.ver_watch, name='ver_watch'),

 path('add-photos/',views.add_photos, name='add-photos'),
 path('view-photos/',views.view_photos, name='view-photos'),
 path('delete-photo<int:pk>/',views.delete_photo, name='delete-photo'),
 path('add-videos/',views.add_videos, name='add-videos'),
 path('view-videos/',views.view_videos, name='view-videos'),
 path('delete-videos<int:pk>/',views.delete_videos, name='delete-videos'),

 path('view-suggestion/',views.view_suggestion, name='view-suggestion'),
 path('view-complain/',views.view_complain, name='view-complain'),
 
 path('view-visitors/',views.view_visitors, name='view-visitors'),
 
path('initiate_payment/<int:pk>', views.initiate_payment, name='initiate_payment'),
path('callback/', views.callback, name='callback'),
path('add-maintenance/', views.add_maintenance, name='add_maintenance'),
path('view-maintenance/', views.view_maintenance, name='view_maintenance'),
path('maintenance-list/', views.maintenance_list, name='maintenance_list'), 

path('add-contect/',views.add_contect, name='add-contect'),

path('check-email/',views.check_email, name='check-email'), 
]
