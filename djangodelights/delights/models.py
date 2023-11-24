from django.db import models
from django.utils import timezone

class Ingredient(models.Model):
    name = models.CharField(max_length=255)
    price_per_unit = models.DecimalField(max_digits=10, decimal_places=2)
    available_quantity = models.PositiveIntegerField()

    def __str__(self):
        return self.name
    
class MenuItem(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    recipe_requirements = models.ManyToManyField('RecipeRequirements', related_name='menu_items')

    def __str__(self):
        return self.name
    
class RecipeRequirements(models.Model):
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.quantity} {self.ingredient.name}"
    
class purchase(models.Model):
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    purchase_time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.menu_item.name} - {self.purchase_time}"