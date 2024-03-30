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
    path("Logout/", views.Logout, name="logout"),
]