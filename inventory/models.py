from django.db import models
units = {
    "tbsp": "big table spune",
    "lbs": "table spune",
    "gr": "gram",
    "kg": "kilogram",
    "ounce": "ounce",
    "ml": "mililitre",
    "li": "litre"
}
# Create your models here.
class Ingradient(models.Model):
    states = {
        "li": "liquid",
        "so": "solid"
    }
    Name = models.CharField(max_length=50)
    State = models.CharField(max_length=2, choice=states)
    Quantity = models.FloatField(default=0)
    Unit = models.CharField(max_length=6, choice=units)
    Unit_price = models.FloatField(default=0)

class MenuItem(models.Model):
    Title = models.CharField(max_length=30)
    Price = models.FloatField()
    Status = models.BooleanField(default=True)
    
class RecipeRequirement(models.Model):
    Menu_item = models.ForeignKey("MenuItem", verbose_name=("Menu Item"), on_delete=models.CASCADE)
    Ingradint = models.ForeignKey("Ingradient", verbose_name=("Recipe"), on_delete=models.CASCADE)
    Quantity = models.FloatField(default=0, balnk=False, Null=False)
    Unit = models.CharField(max_length=6, choice=units)
    
class Purchase(models.Model):
    Menu_item = models.ForeignKey("MenuItem", verbose_name=("Menu Item"))
    Timestamp = models.DateTimeField(auto_now=True, auto_now_add=True)
    Quantity = models.IntegerField(default=1)
    Total_price = models.FloatField()