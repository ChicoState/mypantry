from django import forms
from django.contrib.auth.models import User
from .models import UserModel, ingredient, recipe
from django.forms import ModelForm


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username','password']
        
class ingredientForm(ModelForm):
    class Meta:
        model = ingredient
        fields =['name', 'quantity', 'unit']

class recipeForm(ModelForm):
    class Meta:
        model = recipe
        #ingredients was not working with the forms more investigation is needed
        #exclude = ['ingredients']
        model.ingredients = ingredient
        #fields = "__all__"
        fields = ['title','directions','content','category']