"""
URL configuration for EventStrike project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.tournament_list, name='tournament_list'),
    path('register_team/<int:tournament_id>/', views.register_team, name='register_team'),
    path('tournament_detail/<int:tournament_id>/', views.tournament_detail, name='tournament_detail'),
    path('add_match_result/<int:match_id>/', views.add_match_result, name='add_match_result'),
    path('dashboard/', views.dashboard, name='dashboard'),
]
