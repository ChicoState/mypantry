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

#the name fields were added for test.py these are needed for testing to work
urlpatterns = [
    path('admin/', admin.site.urls, name="admin"),
    path('', pantry_views.home, name="home"),
    path('login/', pantry_views.user_login, name="login"),
    path('logout/', pantry_views.user_logout , name="logout"),
    path('join/', pantry_views.join, name="join"),
    path('pantry/', pantry_views.pantry, name="pantry"),
    path('pantry/add/', pantry_views.pantry_add,  name="pantry_add"), 
    path('pantry/edit/<int:id>/', pantry_views.pantry_edit, name="pantry_edit"),  #test needed
    path('browse/', pantry_views.browse, name="browse"),
    path('recipes/', pantry_views.recipes,  name="recipies"),
    path('recipes/add/', pantry_views.recipe_add,  name="recipe_add"), #test needed
    path('recipes/edit/<int:id>/', pantry_views.recipe_edit),
    path('journal/', pantry_views.journal, name="journal"),  #test needed
    path('journal/add/', pantry_views.journal_add), #test needed
    path('journal/edit/<int:id>/', pantry_views.journal_edit),
    path('groceries/', pantry_views.groceries, name="groceries"),
    path('groceries/add/', pantry_views.groceries_add, name="grocery_add"),
    path('groceries/edit/<int:id>/', pantry_views.groceries_edit)
]