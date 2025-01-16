from django.contrib import admin
from .models import FoodCategories, FoodRecipe, Comment

admin.site.register(FoodCategories)
admin.site.register(FoodRecipe)
admin.site.register(Comment)
