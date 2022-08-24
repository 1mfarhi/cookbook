from django.db import models
from django.db.models import Model


# Create your models here.
class Recipe(models.Model)
    recipe_name = models.CharField(max_length=255)
    recipe_ingredients = models.ManyToManyFields(ingredients)
    recipe_instructions = TextField()