from django.shortcuts import render
from .models import Ingradient, MenuItem, RecipeRequirement, Purchase, PurcahseHistory, Profit

# Create your views here.
def ShowIngradients(request):
    Ingradients = Ingradient.objects.all()
    context = {
        "ingradients" : Ingradients
    }
    
    return render(request, "inventory/ingradients.html", context)

def DeleteIngradients(request, id):
    Ingradient.objects.get(id=id).delete()
    return ShowIngradients(request)
    
def ShowMenu(request):
    menu_items = MenuItem.objects.all()
    context = {
        "menu_items" : menu_items
    }
    
    return render(request, "inventory/menus.html", context)

def Purchases(request):
    purchases_item = Purchase.objects.all()
    context = {
        "purchases" : purchases_item
    }
    
    return render(request, "inventory/purchase.html", context)

def Profit_revenue(request):
    # creating a variable for the cost and the revenue
    cost = 0
    revenue = 0
    # selecting all the items in the purchase table
    purchases = Purchase.objects.all()
    
    start = purchases[0].Timestamp
    end = purchases[0].Timestamp
    # loop every single purchase
    for purchase in purchases:
        # creating a variable for a single purchase
        single_cost = 0
        # get the menu item and quantity from the perchase table and assign it to the variable
        item = purchase.Menu_item
        quantity = purchase.Quantity
        # to get the time for the smallest and largest
        if start >= purchase.Timestamp:
            start = purchase.Timestamp
            
        if end < purchase.Timestamp:
            end = purchase.Timestamp

        # select all the Recipe requirment for a single menu item from the RecipeRequirment table using the menu item
        requirements = RecipeRequirement.objects.filter(Menu_item = item)
        # loop through every Recipe requirement and add their cost
        for requirment in requirements:
            # add the cost for every recipe needed for a single menu item
            single_cost += requirment.Ingradint.Unit_price
        # multiply it by the quantity (how many of that item purcased)
        single_cost *= quantity
        # Add the total price and the cost in every loop
        revenue += purchase.Total_price
        cost += single_cost
    profit = revenue - cost
    context = {
        "purchases": purchases,
        "start_time": start,
        "end_time": end,
        "cost": cost,
        "revenue": revenue,
        "profit": profit
    }
    
    return render(request, "inventory/purchase_profit.html", context)

def Confirm_profit(request, start, end, cost, revenue, profit):
    purchases = Purchase.objects.all()
    
    for item in purchases:
        PurcahseHistory(Menu_name = item.Menu_item.Title, Timestamp = item.Timestamp, Quantity = item.Quantity, Total_price = item.Total_price).save()
        
        item.delete()
        
    Profit(Cost = cost, Revenue = revenue, Profit = profit, Timestamp_start = start, Timestamp_end = end).save()
    
    profites = Profit.objects.all()
    
    context = {
        "profites": profites
    }
    
    return render(request, "inventory/all_profit.html", context)

def All_purchase(request):
    purchases = PurcahseHistory.objects.order_by("Timestamp")
    
    context = {
        "purchases": purchases
    }
    
    return render(request, "inventory/purchase_history.html", context)
