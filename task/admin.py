from django.contrib import admin
from .models import Inventory, Cart, Order

# Register your models here.


# Model Admin for Inventory model
@admin.register(Inventory)
class InventoryAdmin(admin.ModelAdmin):
    """
    The body of the class will be blank, we are adding this class to just perform CRUD operations on the model
    from django admin site
    """
    pass


# Model Admin for Cart Model
@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    """
    The body of the class will be blank, we are adding this class to just perform CRUD operations on the model
    from django admin site
    """
    pass


# Model Admin for Order Model
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    """
    The body of the class will be blank, we are adding this class to just perform CRUD operations on the model
    from django admin site
    """
    pass