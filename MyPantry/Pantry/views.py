from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.urls import reverse
from Pantry.forms import JoinForm, LoginForm, IngredientForm, RecipeForm, JournalEntryForm, GroceryForm
from Pantry.models import Recipe, Ingredient, JournalEntry, Grocery
import csv

def home(request):
    return render(request, 'home.html')

def user_logout(request):
    logout(request)
    return redirect("/login/")

def user_login(request):
    if(request.method == 'POST'):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data["username"]
            password = login_form.cleaned_data["password"]
            user = authenticate(username=username, password=password)
            if user:
                if user.is_active:
                    login(request, user)
                    return redirect("/")
                else:
                    return HttpResponse("Your account is not active.")
            else:
                print("Someone tried to login and failed.")
                print("They used username: {} and password: {}".format(username, password))
    return render(request, 'login.html', {"login_form":LoginForm})

def join(request):
    if(request.method == "POST"):
        join_form = JoinForm(request.POST)
        if(join_form.is_valid()):
            user = join_form.save()
            user.set_password(user.password)
            user.save()
            return redirect("/login/")
        else:
            page_data = {"join_form": join_form}
            return render(request, 'join.html', page_data)
    else:
        join_form = JoinForm()
        page_data = {"join_form":join_form}
    return render(request, 'join.html', page_data)

@login_required(login_url='/login/')
def pantry(request):
    if (request.method == "GET" and "delete" in request.GET):
        id = request.GET["delete"]
        Ingredient.objects.filter(id=id).delete()
        return redirect("/pantry/")
    else:
        table_data = Ingredient.objects.filter(user=request.user)
        context = {
            "table_data": table_data
        }
        return render(request, 'pantry.html', context)

@login_required(login_url='/login/')
def pantry_add(request):
    if (request.method == "POST"):
        if ("add" in request.POST):
            add_form = IngredientForm(request.POST)
            if (add_form.is_valid()):
                name = add_form.cleaned_data["name"]
                quantity = add_form.cleaned_data["quantity"]
                unit = add_form.cleaned_data["unit"]
                user = User.objects.get(id=request.user.id)
                Ingredient(user=user, name=name, quantity=quantity, unit=unit).save()
                return redirect("/pantry/")
            else:
                context = {
                    "form_data": add_form
                }
                return render(request, 'pantry_add.html', context)
        else:
            return redirect("/pantry/")
    else:
        context = {
            "form_data": IngredientForm()
        }
        return render(request, 'pantry_add.html', context)

@login_required(login_url='/login/')
def pantry_edit(request, id):
    if (request.method == "GET"):
        ingredient = Ingredient.objects.get(id=id)
        form = IngredientForm(instance=ingredient)
        context = {"form_data": form}
        return render(request, 'pantry_edit.html', context)
    elif (request.method == "POST"):
        if ("edit" in request.POST):
            form = IngredientForm(request.POST)
            if (form.is_valid()):
                ingredient = form.save(commit=False)
                ingredient.user = request.user
                ingredient.id = id
                ingredient.save()
                return redirect("/pantry/")
            else:
                context = {
                    "form_data": form
                }
                return render(request, 'pantry_add.html', context)
        else:
            return redirect("/pantry/")

@login_required(login_url='/login/')
def browse(request):
    if(Recipe.objects.count()==0):
        #Input stuff into model
        with open('../../recipes.csv', newline='') as f:
            #file stuff
            reader = csv.reader(f)
            for item in reader:
                #get recipe info
                title = item[0]
                directions  = item[1]
                category=  item[(19*3)+1] # this should be the last row
                recipe = Recipe(title=title, directions=directions, category=category)
                recipe.save()
                # get ingredients list
                for x in range(2,59, 3):
                    if item[x] :
                        name = item[x+2]
                        quantity = item[x]
                        unit = item[x+1]
                        Ingredient(name=name, quantity=quantity, unit=unit, recipe=recipe).save()
    
    table_data = Recipe.objects.all()
    context = {
        "table_data": table_data
    }
    
    return render(request, 'browse.html', context)

@login_required(login_url='/login/')
def recipes(request):
    if (request.method == "GET" and "delete" in request.GET):
        id = request.GET["delete"]
        Recipe.objects.filter(id=id).delete()
        return redirect("/recipes/")
    else:
        table_data = Recipe.objects.filter(user=request.user)
        context = {
            "table_data": table_data
        }
        return render(request, 'recipes.html', context)

@login_required(login_url='/login/')
def recipe_add(request):
    if (request.method == "POST"):
        if ("add" in request.POST):
            add_form = RecipeForm(request.POST)
            if (add_form.is_valid()):
                title = add_form.cleaned_data["title"]
                category = add_form.cleaned_data["category"]
                directions = add_form.cleaned_data["directions"]
                user = User.objects.get(id=request.user.id)
                Recipe(user=user, title=title, directions=directions, category=category).save()
                return redirect("/recipes/")
            else:
                context = {
                    "form_data": add_form
                }
                return render(request, 'recipe_add.html', context)
        else:
            return redirect("/recipes/")
    
    else:
        context = {
            "form_data": RecipeForm()
        }
        return render(request, 'recipe_add.html', context)

@login_required(login_url='/login/')
def recipe_edit(request, id):
    if (request.method == "GET"):
        recipe = Recipe.objects.get(id=id)
        form = RecipeForm(instance=recipe)
        context = {"form_data": form}
        return render(request, 'recipe_edit.html', context)
    elif (request.method == "POST"):
        if ("edit" in request.POST):
            form = RecipeForm(request.POST)
            if (form.is_valid()):
                recipe = form.save(commit=False)
                recipe.user = request.user
                recipe.id = id
                recipe.save()
                return redirect("/recipes/")
            else:
                context = {
                    "form_data": form
                }
                return render(request, 'recipe_add.html', context)
        else:
            return redirect("/recipes/")

@login_required(login_url='/login/')
def journal(request):
    if (request.method == "GET" and "delete" in request.GET):
        id = request.GET["delete"]
        JournalEntry.objects.filter(id=id).delete()
        return redirect("/journal/")
    else:
        table_data = JournalEntry.objects.filter(user=request.user)
        context = {
            "table_data": table_data
        }
        return render(request, 'journal.html', context)

@login_required(login_url='/login/')
def journal_add(request):
    if (request.method == "POST"):
        if ("add" in request.POST):
            add_form = JournalEntryForm(request.POST)
            if (add_form.is_valid()):
                description = add_form.cleaned_data["description"]
                entry = add_form.cleaned_data["entry"]
                user = User.objects.get(id=request.user.id)
                JournalEntry(user=user, description=description, entry=entry).save()
                return redirect("/journal/")
            else:
                context = {
                    "form_data": add_form
                }
                return render(request, 'journal_add.html', context)
        else:
            return redirect("/journal/")
    else:
        context = {
            "form_data": JournalEntryForm()
        }
        return render(request, 'journal_add.html', context)

@login_required(login_url='/login/')
def journal_edit(request, id):
    if (request.method == "GET"):
        journalEntry = JournalEntry.objects.get(id=id)
        form = JournalEntryForm(instance=journalEntry)
        context = {"form_data": form}
        return render(request, 'journal_edit.html', context)
    elif (request.method == "POST"):
        if ("edit" in request.POST):
            form = JournalEntryForm(request.POST)
            if (form.is_valid()):
                journalEntry = form.save(commit=False)
                journalEntry.user = request.user
                journalEntry.id = id
                journalEntry.save()
                return redirect("/journal/")
            else:
                context = {
                    "form_data": form
                }
                return render(request, 'journal_add.html', context)
        else:
            return redirect("/journal/")

@login_required(login_url='/login/')
def groceries(request):
    if (request.method == "GET" and "delete" in request.GET):
        id = request.GET["delete"]
        Grocery.objects.filter(id=id).delete()
        return redirect("/groceries/")
    else:
        table_data = Grocery.objects.filter(user=request.user)
        context = {
            "table_data": table_data
        }
        return render(request, 'groceries.html', context)

@login_required(login_url='/login/')
def groceries_add(request):
    if (request.method == "POST"):
        if ("add" in request.POST):
            add_form = GroceryForm(request.POST)
            if (add_form.is_valid()):
                name = add_form.cleaned_data["name"]
                quantity = add_form.cleaned_data["quantity"]
                unit = add_form.cleaned_data["unit"]
                user = User.objects.get(id=request.user.id)
                Grocery(user=user, name=name, quantity=quantity, unit=unit).save()
                return redirect("/groceries/")
            else:
                context = {
                    "form_data": add_form
                }
                return render(request, 'groceries_add.html', context)
        else:
            return redirect("/groceries/")
    else:
        context = {
            "form_data": GroceryForm()
        }
        return render(request, 'groceries_add.html', context)

@login_required(login_url='/login/')
def groceries_edit(request, id):
    if (request.method == "GET"):
        grocery = Grocery.objects.get(id=id)
        form = GroceryForm(instance=ingredient)
        context = {"form_data": form}
        return render(request, 'groceries_edit.html', context)
    elif (request.method == "POST"):
        if ("edit" in request.POST):
            form = GroceryForm(request.POST)
            if (form.is_valid()):
                grocery = form.save(commit=False)
                grocery.user = request.user
                grocery.id = id
                grocery.save()
                return redirect("/groceries/")
            else:
                context = {
                    "form_data": form
                }
                return render(request, 'groceries_add.html', context)
        else:
            return redirect("/groceries/")