from django.contrib import admin
from django.urls import path,include    
from app import urls


urlpatterns = [
    path('admin/', admin.site.urls),
    path("",include(urls)),
    path("accounts/",include("django.contrib.auth.urls"))
]
