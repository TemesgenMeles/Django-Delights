from django.template import Library;
from ..models import RecipeRequirement
register = Library()

@register.filter(name='range') 
def filter_range(start, end):  
    return range(start, end)

@register.filter(name="GetRecipe")
def GetRecipe(ids):
    recipes = RecipeRequirement.objects.filter(Menu_item = ids)
    
    context ={
        "recipes" : recipes
    }
    
    return recipes

@register.filter(name="length")
def length(i):
    return len(i)

@register.filter(name="multi")
def multi(num1, num2):
    return "%.2f" %(num1 * num2)

@register.filter(name="short")
def short(num):
    return "%.2f" %num

