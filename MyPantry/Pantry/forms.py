from django import forms
from django.forms import ModelForm
from Pantry.models import Ingredient, Recipe, JournalEntry, Grocery
from django.contrib.auth.models import User
from django.core import validators

class JoinForm(forms.ModelForm):
    password = forms.CharField(widget = forms.PasswordInput(attrs={'autocomplete':'new-password'}))
    email = forms.CharField(widget = forms.TextInput(attrs={'size': '30'}))
    class Meta():
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password')
        help_texts = {
            'username': None
        }

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())

class IngredientForm(ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'size':'80'}))
    quantity = forms.CharField(widget=forms.TextInput(attrs={'size':'80'}))
    unit = forms.CharField(widget=forms.TextInput(attrs={'size':'80'}))
    class Meta():
        model = Ingredient
        fields = ('name', 'quantity', 'unit')

class GroceryForm(ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'size':'80'}))
    quantity = forms.CharField(widget=forms.TextInput(attrs={'size':'80'}))
    unit = forms.CharField(widget=forms.TextInput(attrs={'size':'80'}))
    class Meta():
        model = Grocery
        fields = ('name', 'quantity', 'unit')

class RecipeForm(ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'size':'80'}))
    category = forms.CharField(widget=forms.TextInput(attrs={'size':'80'}))
    directions = forms.CharField(widget=forms.Textarea(attrs={'rows':'8', 'cols':'80'}))
    class Meta():
        model = Recipe
        fields = ('title', 'category', 'directions')

class JournalEntryForm(forms.ModelForm):
    description = forms.CharField(widget=forms.TextInput(attrs={'size': '80'}))
    entry = forms.CharField(widget=forms.Textarea(attrs={'rows': '8', 'cols':'80'}))
    class Meta():
        model = JournalEntry
        fields = ('description', 'entry')