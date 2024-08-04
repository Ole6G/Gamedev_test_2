"""
URL configuration for Gamedev_test_2 project.

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
from django.urls import path

from game.views import assign_prize,export_player_levels

urlpatterns = [
    path('admin/', admin.site.urls),
    path('export/', export_player_levels, name='export_player_levels'),
    path('assign_prize/<int:player_level_id>/', assign_prize, name='assign_prize'),
]
