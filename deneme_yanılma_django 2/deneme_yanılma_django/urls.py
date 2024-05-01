"""
URL configuration for deneme_yanılma_django project.

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
from django.contrib import admin
from django.urls import path, include
from register import views as register_views
from deneme_yanılma_django.views import home
from main import views as main_views

urlpatterns = [
    path('', home),
    path("admin/", admin.site.urls),
    path("register/register", register_views.register, name="register"),
    path('main/', include('main.urls'))
]
