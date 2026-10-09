from django.contrib import admin
from django.urls import path
from .views import inicio, profile, config
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("",inicio,name="url_inicio"),
    path("profile",profile ,name="url_profile"),
    path("config",config,name="url_config"),
    path("logout/",auth_views.LogoutView.as_view(),name="url_logout")

]
