"""MyPantry URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from Pantry import views as pantry_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', pantry_views.home),
    path('login/', pantry_views.user_login),
    path('logout/', pantry_views.user_logout),
    path('join/', pantry_views.join),
    path('pantry/', pantry_views.pantry),
    path('pantry/add/', pantry_views.pantry_add),
    path('pantry/edit/<int:id>/', pantry_views.pantry_edit),
    path('browse/', pantry_views.browse),
    path('recipes/', pantry_views.recipes),
    path('recipes/add/', pantry_views.recipe_add),
    path('recipes/edit/<int:id>/', pantry_views.recipe_edit),
    path('journal/', pantry_views.journal),
    path('journal/add/', pantry_views.journal_add),
    path('journal/edit/<int:id>/', pantry_views.journal_edit),
    path('groceries/', pantry_views.groceries),
    path('groceries/add/', pantry_views.groceries_add),
    path('groceries/edit/<int:id>/', pantry_views.groceries_edit)
]