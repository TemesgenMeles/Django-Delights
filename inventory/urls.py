from django.urls import path
from . import views

urlpatterns = [
    path("", views.Index, name="index"),
    path("Menu/", views.ShowMenu, name="menu_item"),
    path("Recipes/", views.ShowRecipe, name="recipes"),
    path("Stocks/", views.ShowIngradients, name="stocks"),
    path("Shop/", views.Profit_revenue, name="purchase"),
    path("Shop/All", views.All_purchase, name="purchaseHistory"),
    path("Profit/", views.All_Profit, name="profit"),
    path("Add_Menus/", views.Add_Menus, name="Add_menu"),
    path("Add_Menus/Submit", views.SubmitMenu, name="Submit_Add_menus"),
    path("Add_Menus/Submit/RR/<rrid>", views.SubmitRecipes,name="Submit_RR"),
    path("Menu/Purchase/<itemID>", views.Buy, name="buy_conformation"),
    path("Menu/buy/<itemID>", views.buy_function, name="buy"),
    path("Menu/Edit/<itemID>", views.Edit_Menu_Page, name="edit_menu_page"),
    path("Menu/Edit/Submit/<itemID>", views.Edit_Menu, name="edit_menu"),
    path("Recipes/Edit/<itemID>", views.Recipe_Edit_Page, name="recipe_edit_page"),
    path("Recipes/Edit/Submit/<itemID>", views.Recipe_Edit, name="recipe_edit"),
    path("Recipes/Edit/Delete/<itemID>/<menuID>", views.Recipe_Delete, name="recipe_delete"),
    path("Recipes/Edit/Add/<menuID>", views.Add_Recipe_from_Edit, name="add_recipe_from_Edit"),
    path("Stocks/Add_Ingradient", views.Add_Ingradient_Page, name="add_ingradient_page"),
    path("Stocks/Add_Ingradient/Submit", views.Add_Ingradient, name="add_ingradient"),
    path("Logout/", views.Logout, name="logout"),
]