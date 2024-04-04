from django.shortcuts import render
from .models import Ingradient, MenuItem, RecipeRequirement, Purchase, PurcahseHistory, Profit

# for calculating unit values
# changing the quantity into mililiter and gram based on their state
def to_gram(state, unit, quantity):
    result = 0
    # if it's state solid change the quantity into gram
    if state == "solid":
        # change into gram based on thier units
        if unit == "teaspoon":
            result = quantity * 5
        elif unit == "tablespoon":
            result = quantity * 15
        elif unit == "pound":
            result = quantity * 433
        elif unit == "kilogram":
            result = quantity * 1000
        elif unit == "ounce":
            result = quantity * 28.3
        else : # if it is not in the above it is a gram unit so we don't have to change any thing
            result = quantity
    # if is's state liquid change the quantity into mililiter
    elif state == "liquid":\
        # change into mililiter based on thier units
        if unit == "teaspoon":
            result = quantity * 5
        elif unit == "tablespoon":
            result = quantity * 15
        elif unit == "gallon":
            result = quantity * 3785.41
        elif unit == "glass":
            result = quantity * 240
        elif unit == "ounce":
            result = quantity * 28.4
        elif unit == "litre":
            result = quantity * 1000
        else : # if it is not in the above it is a mililiter unit so we don't have to change any thing
            result = quantity
    else : # if it is not solid or liquid so it is count we don't have to change any thing
        result = quantity
    result = "%.2f" %result
    return result

# changing the quantity from mililiter and gram into their state
def from_gram(state, unit, quantity):
    result = 0
    # if the state is solid we change it form gram
    if state == "solid":
        if unit == "teaspoon":
            result = quantity / 5
        elif unit == "tablespoon":
            result = quantity / 15
        elif unit == "pound":
            result = quantity / 433
        elif unit == "kilogram":
            result = quantity / 1000
        elif unit == "ounce":
            result = quantity / 28.3
        else :
            result = quantity
    # if the state is liquid we change it from mililiter
    elif state == "liquid":
        if unit == "teaspoon":
            result = quantity / 5
        elif unit == "tablespoon":
            result = quantity / 15
        elif unit == "gallon":
            result = quantity / 3785.41
        elif unit == "glass":
            result = quantity / 240
        elif unit == "ounce":
            result = quantity / 28.4
        elif unit == "litre":
            result = quantity / 1000
        else :
            result = quantity
    # if the state is nither solid nor liquid we don't have to change any thing
    else :
        result = quantity
    # we change the last result into 2nd decimal place in case it has many decimal place
    result = "%.2f" %result
    return result

# Create your views here.
def Index(request):
    return render(request, "inventory/index.html")

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
    menu_items = MenuItem.objects.order_by("-Reating")
    context = {
        "menu_items" : menu_items,
    }
    
    return render(request, "inventory/menus.html", context)

def ShowRecipe(request):
    menu_items = MenuItem.objects.all()
    
    context ={
        "menu_items" : menu_items,
    }
    
    return render(request, "inventory/recipe.html", context)

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
    
    return render(request, "inventory/purchase.html", context)

def Confirm_profit(request, start, end, cost, revenue, profit):
    purchases = Purchase.objects.all()
    
    for item in purchases:
        PurcahseHistory(Menu_name = item.Menu_item.Title, Timestamp = item.Timestamp, Quantity = item.Quantity, Total_price = item.Total_price).save()
        
        item.delete()
        
    Profit(Cost = cost, Revenue = revenue, Profit = profit, Timestamp_start = start, Timestamp_end = end).save()
    
    Profit(request)

def All_Profit(request):
    profites = Profit.objects.order_by("-pk")  
    total_profit = 0
    
    for item in profites:
        total_profit += item.Profit
        
    context = {
        "profites": profites,
        "total_profit": total_profit
    }
    
    return render(request, "inventory/all_profit.html", context)

def All_purchase(request):
    purchases = PurcahseHistory.objects.order_by("Timestamp")
    
    context = {
        "purchases": purchases
    }
    
    return render(request, "inventory/purchase_history.html", context)

def Add_Menus(request):
    ingradients = Ingradient.objects.all()
    context = {
        "ingradients" : ingradients
    }
    
    return render(request, "inventory/Add_menu.html", context)

def SubmitMenu(request):
    context = {}
    if request.method == "POST":
        title = request.POST["title"]
        price = request.POST["price"]
        reating = request.POST["reating"]
        ingradient_list = request.POST.getlist("ingradient_list")
        AddMenus = MenuItem(Title = title, Price = price, Reating = reating, Status = False)
        AddMenus.save()
        FeachMenuItem = MenuItem.objects.get(Title = title, Price = price, Reating = reating)
        for item in ingradient_list:
            FeachIngradient = Ingradient.objects.get(id = item)
            AddRecipeRequirement = RecipeRequirement(Menu_item = FeachMenuItem, Ingradint = FeachIngradient)
            AddRecipeRequirement.save()
        
        feachRecipe = RecipeRequirement.objects.filter(Menu_item = FeachMenuItem)
        units = [
            "teaspoon",
            "tablespoon",
            "pound",
            "gram",
            "kilogram",
            "ounce",
            "mililitre",
            "litre",
            "glass",
            "gallon",
            "count"
        ]
        
        context = {
            "RecipeIngradients": feachRecipe,
            "units": units,
            "title": title,
        }
        
    return render(request, "inventory/update_requirement.html", context)

def SubmitRecipes(request, rrid):
    if request.method == "POST":
        #rrid = request.POST['id']
        quantity = request.POST['quantity']
        unit = request.POST['unit']

        feachRR = RecipeRequirement.objects.get(id = rrid)
        feachRR.Quantity = quantity
        feachRR.Unit = unit
        feachRR.save()
        
        FeachMenuItem = feachRR.Menu_item
        
        feachRecipe = RecipeRequirement.objects.filter(Menu_item = FeachMenuItem)
        units = [
            "teaspoon",
            "tablespoon",
            "pound",
            "gram",
            "kilogram",
            "ounce",
            "mililitre",
            "litre",
            "glass",
            "gallon",
            "count"
        ]
        
        context = {
            "RecipeIngradients": feachRecipe,
            "units": units,
            "title": FeachMenuItem.Title 
        }
    
    return render(request, "inventory/update_requirement.html", context)

def Buy(request, itemID):
    
    Menu_item_id = itemID
    
    purchase_item = MenuItem.objects.get(id = Menu_item_id)
    
    context = {
        "purchase_item" : purchase_item,
    }
    
    return render(request, "inventory/purchase_conformation.html", context)
    
def buy_function(request, itemID):
    if request.method == "POST":
        Mid = itemID
        quant = float(request.POST.get('quantity'))
        menuItem = MenuItem.objects.get(id=Mid)
        pri = menuItem.Price * quant
        
        Purchase(Menu_item = menuItem, Quantity = quant, Total_price = pri).save()
        
        Recipe_requirements = RecipeRequirement.objects.filter(Menu_item = menuItem)
        
        for recipe_requirement in Recipe_requirements:
            whole_ingradient = recipe_requirement.Ingradint
            
            ingradient_state = whole_ingradient.State
            ingradient_unit = whole_ingradient.Unit
            ingradient_quantity = whole_ingradient.Quantity
            
            required_unit = recipe_requirement.Unit
            required_quantity = recipe_requirement.Quantity
            
            big = to_gram(ingradient_state, ingradient_unit, ingradient_quantity)
            
            small = to_gram(ingradient_state, required_unit, required_quantity)
            small = float(small) * float(quant)
            
            left_Ingradient = float(big) - float(small)
            
            finall_quantity = from_gram(ingradient_state, ingradient_unit, left_Ingradient)
            
            whole_ingradient.Quantity = finall_quantity
            whole_ingradient.save()
        
    return ShowMenu(request)
        
def Edit_Menu_Page(request, itemID):
    menu_item = MenuItem.objects.get(id = itemID)

    context = {
        "menu_item" : menu_item,
    }
    
    return render(request, "inventory/edit_menu.html", context)

def Edit_Menu(request, itemID):
    if request.method == "POST":
        MIID = itemID
        title = request.POST['menu_name']
        price = request.POST['price']
        reating = request.POST['reating']

        menu_item = MenuItem.objects.get(id=MIID)
        menu_item.Title = title
        menu_item.Price = price
        menu_item.Reating = reating
        
        menu_item.save()
        
        return ShowMenu(request)

def Recipe_Edit_Page(request, itemID):
    recipe_item = RecipeRequirement.objects.filter(Menu_item = itemID)
    menu_item = MenuItem.objects.get(id = itemID)
    title = menu_item.Title
    menuID = menu_item.id
    
    left_ingradient = []
    ingradients = Ingradient.objects.all()
    for ingradient in ingradients:
        count = 0
        for recipe in recipe_item:
            if ingradient == recipe.Ingradint:
                count = count + 1
            else:
                continue
        if count == 0:
            left_ingradient.append(ingradient)

    units = [
            "teaspoon",
            "tablespoon",
            "pound",
            "gram",
            "kilogram",
            "ounce",
            "mililitre",
            "litre",
            "glass",
            "gallon",
            "count"
        ]
    
    context = {
        "recipe_item" : recipe_item,
        "title" : title,
        "menuID" : menuID,
        "units" : units,
        "ingradients": left_ingradient,
    }
    
    return render(request, "inventory/recipe_edit.html", context)

def Recipe_Edit(request, itemID):
    if request.method == "POST":
        recipe_requirement = RecipeRequirement.objects.get(id = itemID)
        
        quan = request.POST['recipe_quantity']
        unit = request.POST['recipe_unit']
        
        recipe_requirement.Quantity = quan
        recipe_requirement.Unit = unit
        
        recipe_requirement.save()
        
        return ShowRecipe(request)

def Recipe_Delete(request, itemID, menuID):
    recipe_requirement = RecipeRequirement.objects.get(id = itemID)
    recipe_requirement.delete()
    
    return Recipe_Edit_Page(request, menuID)

def Add_Recipe_from_Edit(request, menuID):
    if request.method == "POST":
        menuID = menuID
        ingradientID = request.POST['name']
        menu_item = MenuItem.objects.get(id = menuID)
        ingradient = Ingradient.objects.get(id = ingradientID)
        quantity = request.POST['quantity']
        unit = request.POST['unit']

        RecipeRequirement(Menu_item = menu_item, Ingradint = ingradient, Quantity = quantity, Unit = unit).save()
        
        return ShowRecipe(request)
    
def Logout(request):
    pass