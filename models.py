from django.db import models
from django.urls import reverse


#menu_name Model
class Recipe(models.Model):
    menu_id = models.IntegerField(primary_key=True)
    menu_name = models.CharField(max_length=20, blank=False, null=False)
    menu_category1 = models.CharField(max_length=20, blank=False, null=False)
    menu_category2 = models.CharField(max_length=20, blank=False, null=False)
    ingredient1 = models.CharField(max_length=20, blank=True, null=True)
    ingredient2 = models.CharField(max_length=20, blank=True, null=True)
    ingredient3 = models.CharField(max_length=20, blank=True, null=True)
    ingredient4 = models.CharField(max_length=20, blank=True, null=True)
    ingredient5 = models.CharField(max_length=20, blank=True, null=True)
    ingredient6 = models.CharField(max_length=20, blank=True, null=True)
    ingredient7 = models.CharField(max_length=20, blank=True, null=True)
    ingredient8 = models.CharField(max_length=20, blank=True, null=True)
    ingredient9 = models.CharField(max_length=20, blank=True, null=True)
    ingredient10 = models.CharField(max_length=20, blank=True, null=True)
    ingredient11 = models.CharField(max_length=20, blank=True, null=True)
    ingredient12 = models.CharField(max_length=20, blank=True, null=True)
    ingredient13 = models.CharField(max_length=20, blank=True, null=True)
    ingredient14 = models.CharField(max_length=20, blank=True, null=True)
    ingredient15 = models.CharField(max_length=20, blank=True, null=True)
    ingredient16 = models.CharField(max_length=20, blank=True, null=True)
    ingredient17 = models.CharField(max_length=20, blank=True, null=True)
    ingredient18 = models.CharField(max_length=20, blank=True, null=True)
    ingredient19 = models.CharField(max_length=20, blank=True, null=True)
    ingredient20 = models.CharField(max_length=20, blank=True, null=True)
    recipe = models.CharField(max_length=500, blank=False, null=False)
    source = models.CharField(max_length=20, blank=True, null=True)
    register_date = models.DateField(blank=False, null=False, auto_now_add=True)
    
    class Meta:
        managed = False
        db_table = 'RECIPE'
    
    def __str__(self):
        return 'id:' + str(self.menu_id) + ' "' + self.menu_name + '"'
    
    @staticmethod
    def get_absolute_url(self):
        return reverse('recipe_site:menu')

###############################################################################
class RecipeRecord(models.Model):
    menu_id = models.ForeignKey(Recipe, models.DO_NOTHING, blank=True, null=True)
    record_date = models.DateField(blank=True, null=True)
    rate = models.CharField(max_length=1, blank=True, null=True)
    memo = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'RECIPE_RECORD'

    def __str__(self):
        return self.menu_id + ',' + self.record_date
