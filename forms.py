from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.forms import forms, CharField, IntegerField
from .models import Recipe


class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password'].widget.attrs['class'] = 'form-control'

class RecipeRegisterForm(forms.Form):
    menu_id = IntegerField(initial=' ', label='ID', required=True)
    menu_name = CharField(initial='', label='MENU TITLE', max_length=20, required=True)
    menu_category1 = CharField(initial='', label='CATEGORY', max_length=20, required=True)
    menu_category2 = CharField(initial='', label='SUB CATEGORY', max_length=20, required=True)
    ingredient1 = CharField(initial='', label='INGREDIENT', max_length=20, required=True)
    ingredient2 = CharField(initial='', label='INGREDIENT', max_length=20, required=True)
    ingredient3 = CharField(initial='', label='INGREDIENT', max_length=20, required=True)
    ingredient4 = CharField(initial='', label='INGREDIENT', max_length=20, required=True)
    ingredient5 = CharField(initial='', label='INGREDIENT', max_length=20, required=True)
    ingredient6 = CharField(initial='', label='INGREDIENT', max_length=20, required=True)
    ingredient7 = CharField(initial='', label='INGREDIENT', max_length=20, required=True)
    ingredient8 = CharField(initial='', label='INGREDIENT', max_length=20, required=True)
    ingredient9 = CharField(initial='', label='INGREDIENT', max_length=20, required=True)
    ingredient10 = CharField(initial='', label='INGREDIENT', max_length=20, required=True)
    ingredient11 = CharField(initial='', label='INGREDIENT', max_length=20, required=True)
    ingredient12 = CharField(initial='', label='INGREDIENT', max_length=20, required=True)
    ingredient13 = CharField(initial='', label='INGREDIENT', max_length=20, required=True)
    ingredient14 = CharField(initial='', label='INGREDIENT', max_length=20, required=True)
    ingredient15 = CharField(initial='', label='INGREDIENT', max_length=20, required=True)
    ingredient16 = CharField(initial='', label='INGREDIENT', max_length=20, required=True)
    ingredient17 = CharField(initial='', label='INGREDIENT', max_length=20, required=True)
    ingredient18 = CharField(initial='', label='INGREDIENT', max_length=20, required=True)
    ingredient19 = CharField(initial='', label='INGREDIENT', max_length=20, required=True)
    ingredient20 = CharField(initial='', label='INGREDIENT', max_length=20, required=True)
    recipe = CharField(initial='', label='RECIPE', max_length=500, required=True)
    source = CharField(initial='', label='SOURCE', max_length=20, required=True)
                
    def save(self):
        data = self.cleaned_data
        register = Recipe(menu_id=data['menu_id'], menu_name=data['menu_name'],
                          menu_category1=data['menu_category1'], menu_category2=data['menu_category2'],
                          ingredient1=data['ingredient1'], ingredient2=data['ingredient2'],
                          ingredient3=data['ingredient3'], ingredient4=data['ingredient4'],
                          ingredient5=data['ingredient5'], ingredient6=data['ingredient6'],
                          ingredient7=data['ingredient7'], ingredient8=data['ingredient8'],
                          ingredient9=data['ingredient9'], ingredient10=data['ingredient10'],
                          ingredient11=data['ingredient11'], ingredient12=data['ingredient12'],
                          ingredient13=data['ingredient13'], ingredient14=data['ingredient14'],
                          ingredient15=data['ingredient15'], ingredient16=data['ingredient16'],
                          ingredient17=data['ingredient17'], ingredient18=data['ingredient18'],
                          ingredient19=data['ingredient19'], ingredient20=data['ingredient20'],
                          recipe=data['recipe'], source=data['source']
                          )
        register.save()
        
#########################################################################################################
class SearchForm(forms.Form):
    menu_id = IntegerField(initial=' ', label='ID', required=False)
    menu_name = CharField(initial='', label='MENU TITLE', max_length=20, required=False)
    menu_category1 = CharField(initial='', label='CATEGORY', max_length=20, required=False)
    menu_category2 = CharField(initial='', label='SUB CATEGORY', max_length=20, required=False)
    ingredient1 = CharField(initial='', label='INGREDIENT', max_length=20, required=False)
    ingredient2 = CharField(initial='', label='INGREDIENT', max_length=20, required=False)
    ingredient3 = CharField(initial='', label='INGREDIENT', max_length=20, required=False)
    ingredient4 = CharField(initial='', label='INGREDIENT', max_length=20, required=False)
    ingredient5 = CharField(initial='', label='INGREDIENT', max_length=20, required=False)
    ingredient6 = CharField(initial='', label='INGREDIENT', max_length=20, required=False)
    ingredient7 = CharField(initial='', label='INGREDIENT', max_length=20, required=False)
    ingredient8 = CharField(initial='', label='INGREDIENT', max_length=20, required=False)
    ingredient9 = CharField(initial='', label='INGREDIENT', max_length=20, required=False)
    ingredient10 = CharField(initial='', label='INGREDIENT', max_length=20, required=False)
    ingredient11 = CharField(initial='', label='INGREDIENT', max_length=20, required=False)
    ingredient12 = CharField(initial='', label='INGREDIENT', max_length=20, required=False)
    ingredient13 = CharField(initial='', label='INGREDIENT', max_length=20, required=False)
    ingredient14 = CharField(initial='', label='INGREDIENT', max_length=20, required=False)
    ingredient15 = CharField(initial='', label='INGREDIENT', max_length=20, required=False)
    ingredient16 = CharField(initial='', label='INGREDIENT', max_length=20, required=False)
    ingredient17 = CharField(initial='', label='INGREDIENT', max_length=20, required=False)
    ingredient18 = CharField(initial='', label='INGREDIENT', max_length=20, required=False)
    ingredient19 = CharField(initial='', label='INGREDIENT', max_length=20, required=False)
    ingredient20 = CharField(initial='', label='INGREDIENT', max_length=20, required=False)
    source = CharField(initial='', label='SOURCE', max_length=20, required=False)
    
    
    
    
    