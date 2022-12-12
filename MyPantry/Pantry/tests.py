# from django.test import TestCase
#from django import urls
# test refrence used: https://djangostars.com/blog/django-pytest-testing/ 

'''
    run in the following dir:
        mypantry-project/MyPantry/Pantry
'''


from django.urls import reverse
import pytest
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User

# a login for testing
@pytest.fixture
def login_form():
	return {'first_name':'Billy', 'last_name':'Billy', 'username':'Chef_Billy', 'email':'Billy@billysblog.com', 'password':'love2cook'}

@pytest.fixture
def pantry_form():
    return{'name':'soup', 'quantity':'1', 'unit':'can'}

@pytest.fixture
def recipe_form():
    return{'title':'test', 'category':'test', 'directions':'test'}

#parametrize the pages for testing if pages render (when not logged in)
@pytest.mark.parametrize('params_no_login',[
        ('home'),
        ('join'),
        ('login'),
])

# Create your tests here.

#test pages to see if they render (pre-login)
def test_pages(client, params_no_login):
        page_url = reverse(params_no_login)
        response = client.get(page_url)
        assert response.status_code == 200        


#tests a user joining 
@pytest.mark.django_db
def test_user_join(client, login_form):
    user_model = get_user_model()
    assert user_model.objects.count() == 0
    join_url = reverse('join')
    response = client.post(join_url, login_form)
    assert user_model.objects.count() == 1
    assert response.status_code == 302
    #check logout
    logout_url = reverse('logout')
    response2 = client.get(logout_url)
    assert response2.status_code == 302
    #we should be able to logout if we are logged in


#using user join we now attempt to login
@pytest.mark.django_db
def test_user_login(client, login_form):
    #join
    join_url  = reverse('join')
    join_response = client.post(join_url, login_form)
    assert join_response.status_code == 302
    #login
    login_url = reverse('login')
    login_response = client.post(login_url, login_form)
    assert login_response.status_code == 302

#after login tests
@pytest.mark.django_db
@pytest.mark.parametrize('params_after_login',[
      ('pantry'),
      ('browse'),
      ('journal'),
      ('recipies'),
      ('groceries'),
])

def test_pages_after_login(client, login_form,params_after_login):
    #join
    join_url  = reverse('join')
    join_response = client.post(join_url, login_form)
    assert join_response.status_code == 302
    #login
    login_url = reverse('login')
    login_response = client.post(login_url, login_form)
    assert login_response.status_code == 302

    #test pages to see if they render (after login)
    page_url = reverse(params_after_login)
    response = client.get(page_url)
    assert response.status_code == 200  


#test adding to the pantry
@pytest.mark.django_db
def test_add_pantry(client, login_form, pantry_form):
    #join
    join_url  = reverse('join')
    join_response = client.post(join_url, login_form)
    assert join_response.status_code == 302
    #login
    login_url = reverse('login')
    login_response = client.post(login_url, login_form)
    assert login_response.status_code == 302
    #add item to pantry
    pantry_add_url = reverse('pantry_add')
    pan_add_response = client.post(pantry_add_url, pantry_form)
    assert pan_add_response.status_code == 302
    

#test adding the grocery
@pytest.mark.django_db
def test_add_grocery(client, login_form, pantry_form):
    #join
    join_url  = reverse('join')
    join_response = client.post(join_url, login_form)
    assert join_response.status_code == 302
    #login
    login_url = reverse('login')
    login_response = client.post(login_url, login_form)
    assert login_response.status_code == 302
    #add item to pantry
    pantry_add_url = reverse('grocery_add')
    pan_add_response = client.post(pantry_add_url, pantry_form)
    assert pan_add_response.status_code == 302

    #test adding to the journal

# test adding to the recipe page
@pytest.mark.django_db
def test_add_recipe(client, login_form, recipe_form):
    #join
    join_url  = reverse('join')
    join_response = client.post(join_url, login_form)
    assert join_response.status_code == 302
    #login
    login_url = reverse('login')
    login_response = client.post(login_url, login_form)
    assert login_response.status_code == 302
    #add item to pantry
    pantry_add_url = reverse('recipe_add')
    pan_add_response = client.post(pantry_add_url, recipe_form)
    assert pan_add_response.status_code == 302