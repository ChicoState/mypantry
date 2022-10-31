from lib2to3.pgen2.tokenize import untokenize
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from .forms import UserForm, recipeForm, ingredientForm
from .models import ingredient, recipe
from django import forms
from django.contrib.auth.models import User

IMAGE_FILE_TYPES = ['jpg','png']

def home(request):
    return render(request, 'Pantry/dashboard.html')

def userlogin(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return render(request, 'Pantry/dashboard.html')
        else:
            return render(request, 'Pantry/login.html', {'error_message':'Login credentials are wrong'})
    return render(request, 'Pantry/login.html')

def userlogout(request):
    logout(request)
    form = UserForm(request.POST or None)
    context = {
        "form": form,
    }
    return render(request, 'Pantry/login.html', context)

def register(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user.set_password(password)
        user.save()
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return render(request, 'Pantry/login.html')
    context = {
        "form": form,
    }
    return render(request, 'Pantry/register.html')

def pantry(request):
    form = ingredientForm(request.POST or None)
    if form.is_valid():
        name = form.cleaned_data["name"]
        quantity = form.cleaned_data["quantity"]
        unit = form.cleaned_data["unit"]
        user = User.objects.get(id=request.user.id)
        ingredient(user=user, name=name, quantity=quantity, unit=unit).save()
    context = {
        "form": form,
    }
    return render(request, 'Pantry/pantry.html', context)


def browse(request):
    return render(request, 'Pantry/browse.html')

def viewRecipe(request):
    if not request.user.is_authenticated:
        return render(request,'Pantry/login.html')
    else:
        all_recipes = recipe.objects.all()
        return render(request, 'Pantry/view_recipe.html', {'all_recipes':all_recipes})

def details(request, recipe_id):
    recipes = get_object_or_404(recipe, pk=recipe_id)
    return render(request, 'Pantry/detail.html',{'recipes':recipes})


def myRecipes(request):
    return render(request, 'Pantry/saved_recipes.html')


#@login_Reqired
def createRecipe(request):
    #TODO: add the ingredients to the form (see forms.py)
    if not request.user.is_authenticated:
        return render(request,'Pantry/login.html')
    else:
        context={}
        form = recipeForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            myRec = form.save(commit=False)
            myRec.user = request.user
            myRec.save()
            form.save()
            return render(request, 'Pantry/view_recipe.html',{'myRec':myRec})
        context['form']= form
        return render(request, 'Pantry/create_recipe.html', context)

def updateRecipe(request):
    return render(request, 'Pantry/update_recipe.html')

def deleteRecipe(request):
    return render(request, 'Pantry/delete_recipe.html')
