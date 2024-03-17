from django.urls import path
from . import views

urlpatterns = [
    path("", views.Index, name="index"),
    path("Menu/", views.ShowMenu, name="menu_item"),
    path("Recipes/", views.ShowRecipe, name="recipes"),
    path("Stocks/", views.ShowIngradients, name="stocks"),
    path("Shop/", views.Purchases, name="purchase"),
    path("Profit/", views.Profit_revenue, name="profit"),
    path("Logout/", views.Logout, name="logout"),
]