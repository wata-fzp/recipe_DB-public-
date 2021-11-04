from django.contrib import admin
from .models import Recipe, RecipeRecord
#from .models import 

admin.site.site_title = 'recipe_site'
admin.site.site_header = 'kaki\'s recipe_site'


# Register your models here.
admin.site.register(Recipe)
admin.site.register(RecipeRecord)
