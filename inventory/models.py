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