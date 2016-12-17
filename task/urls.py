"""beautycode URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
"""

from django.conf.urls import url
from task import views

urlpatterns = [
    # URL related to Login
    url(r'^$', views.login_view, name='login'),
    # URL related to Logout
    url(r'^logout/$', views.logout_view, name='logout'),
    # URL to add item to cart
    url(r'^add/(?P<item_id>\d+)/$', views.add_to_cart_view, name='add_to_cart'),
    # URL to delete item from cart
    url(r'^delete/(?P<item_id>\d+)/$', views.delete_from_cart_view, name='delete_from_cart'),
    # URL to view cart items
    url(r'^view/$', views.show_cart_view, name='view_cart'),
    # URL to Place the order
    url(r'^order/$', views.place_order_view, name='place_order'),
    # URL to Place the order
    url(r'^show_orders/$', views.show_order_view, name='show_orders'),
]
