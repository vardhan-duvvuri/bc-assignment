from django.db import models
from django.contrib.auth.models import User
import  json

# Create your models here.


# Models related to Task app


class Inventory(models.Model):
    """
    Model related to store the inventory information
    Fields :
        item_name : CharField - To store the name of the item
        available_count : IntegerField - To store the quantity available in the inventory
    """
    item_name = models.CharField(max_length=126, null=False, blank=False)
    available_count = models.IntegerField(null=False, blank=False)

    def __str__(self):
        return "{0} - ({1})".format(self.item_name, self.available_count)

    class Meta:
        # Sort the records based on fields while querying in the ORM
        ordering = ["-available_count"]


class Cart(models.Model):
    """
    Model related to store the user cart information
    Fields :
        user : Foreign Key (User Model)- Foreign Key to the model django.contrib.auth.models.User
        item : Foreign Key (Inventory Model) - Foreign Key to the model task.models.Inventory
        quantity : Integer Field - To store the no of items user want to add in the cart
        is_active : Boolean Field - If user deletes the item from the cart then this will be False, else it will be true
    """
    user = models.ForeignKey(User)
    item = models.ForeignKey(Inventory)
    quantity = models.IntegerField(null=False, blank=False, default=1)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return "For User {0} the Item {1} Quantity ({2})".format(self.user, self.item, self.quantity)


class Order(models.Model):
    """
    Model related to store the Orders
    Fields :
        carts : Char Field- Foreign Key to the model task.models.Cart
    """
    carts = models.CharField(max_length=200)
    user_id = models.ForeignKey(User)


    def __str__(self):
        return "Order ({1})".format(self.carts)