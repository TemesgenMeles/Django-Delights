from django.db import models
units = [
    ("tsp", "teaspoon"),
    ("tbsp", "tablespoon"),
    ("lbs", "pound"),
    ("gr", "gram"),
    ("kg", "kilogram"),
    ("oz", "ounce"),
    ("ml", "mililitre"),
    ("li", "litre"),
    ("glass", "glass"),
    ("gal", "gallon"),
    ("count", "count")
]
# Create your models here.
class Ingradient(models.Model):
    states = [
        ("li", "liquid"),
        ("so", "solid"),
        ("co", "count")
    ]
    
    Name = models.CharField(max_length=50)
    State = models.CharField(max_length=2, choices=states)
    Quantity = models.FloatField(default=0)
    Unit = models.CharField(max_length=6, choices=units)
    Unit_price = models.FloatField(default=0)

class MenuItem(models.Model):
    Title = models.CharField(max_length=30)
    Price = models.FloatField()
    Reating = models.IntegerField(default=3)
    Status = models.BooleanField(default=True)
    
class RecipeRequirement(models.Model):
    Menu_item = models.ForeignKey("MenuItem", verbose_name=("Menu Item"), on_delete=models.CASCADE)
    Ingradint = models.ForeignKey("Ingradient", verbose_name=("Recipe"), on_delete=models.PROTECT)
    Quantity = models.FloatField(default=0, blank=False, null=False)
    Unit = models.CharField(default="gram", max_length=6, choices=units)
    
class Purchase(models.Model):
    Menu_item = models.ForeignKey("MenuItem", verbose_name=("Menu Item"), on_delete=models.PROTECT)
    Timestamp = models.DateTimeField(auto_now=True)
    Quantity = models.IntegerField(default=1)
    Total_price = models.FloatField()
    
class PurcahseHistory(models.Model):
    Menu_name = models.CharField(max_length=50)
    Timestamp = models.DateTimeField()
    Quantity = models.IntegerField(default=1)
    Total_price = models.FloatField()
    
class Profit(models.Model):
    Cost = models.FloatField(default = 0)
    Revenue = models.FloatField(default = 0)
    Profit = models.FloatField(default = 0)
    Timestamp_start = models.CharField(max_length=255)
    Timestamp_end = models.CharField(max_length=255)
    