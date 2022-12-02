from django.contrib import admin
from django.urls import path
from . import views


urlpatterns=[


path('', views.index, name='meetups'),
path('register/', views.register, name='register'),
path('error/', views.reg_error, name='reg_error'),
path('login/', views.loginPage, name='login'),
path('profile/<str:pk>/', views.profile, name='profile'),
path('update_success/', views.update_success, name='update_success'),
path('meetups/success', views.confirm_registration, name='confirm-registration'),
path('meetups/about', views.meetup_about, name='meetup-about'),
path('meetups/services', views.meetup_services, name='meetup-services'),
path('meetups/team', views.meetup_team, name='meetup-team'),
path('meetups/contact', views.meetup_contact, name='meetup-contact',),

path('meetups/<slug:meetup_slug>', views.meetup_details, name='meetup_details'),
path('logout/', views.logoutUser, name='logout'),


]
