from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist

# Importing models
from .models import Inventory, Cart, Order

# Create your views here.

# view to display the login page and authenticate the user based in the
# credentials provided


def login_view(request):
    '''
    All the login related code will be written here
    :param request: the request parameter from the web
    :return: return login.html page if not logged in else return dashboard page
    '''
    # Respond to the POST request for Login
    if request.method == "POST":
        username = request.POST['_username']
        password = request.POST['_password']
        # authenticating the credentials of the user
        user = authenticate(username=username, password=password)
        # IF user exists with the provided credentials then login
        if user:
            login(request, user)
    # If no user logged in show login page
    if not request.user.is_authenticated():
        return render(request, "login.html")
    # Get the required information to display dashboard page
    inventory = Inventory.objects.all()
    return render(request, "dashboard.html", {'inventory': inventory})


# View to handle the logout functionality
@login_required(login_url="")
def logout_view(request):
    '''
    View to logout functionality
    :param request: request from the web
    :return: login web page
    '''
    logout(request)
    return HttpResponseRedirect("/")


# View to Handle the Add to Cart functionality
@login_required(login_url="")
def add_to_cart_view(request, item_id):
    '''
    VIew to add an item to the cart
    :param request: request from web
    :param item_id: item id to add card
    :return:
    '''
    error = None
    info = None
    try:
        item = Inventory.objects.get(id=item_id)
        if item.available_count == 0:
            error = "Not in Stock"
        else:
            item.available_count -= 1
            item.save()
            try:
                cart = Cart.objects.get(
                    item=item, user=request.user, is_active=True)
                cart.quantity += 1
            except ObjectDoesNotExist:
                cart = Cart()
                cart.item = item
                cart.user = request.user
                cart.quantity = 1
            cart.save()
    except ObjectDoesNotExist:
        error = "Item Not Found"
    except Exception as e:
        print(e)
        error = "Something Went Wrong while adding item to Cart"
    if not error:
        info = "Item Added to Cart successfully"
    inventory = Inventory.objects.all()
    return render(
        request, "dashboard.html", {
            'inventory': inventory, 'i': info, 'e': error})


# View to Handle the Add to Cart functionality
@login_required(login_url="")
def delete_from_cart_view(request, item_id):
    '''
    View to Delete item from cart
    :param request: request from web
    :param item_id: id of item to be removed
    :return:  home page
    '''
    error = None
    info = None
    try:
        cart = Cart.objects.get(id=item_id)
        cart.is_active = False
        cart.save()
        item = Inventory.objects.get(id=cart.item.id)
        item.available_count += cart.quantity
        item.save()
    except ObjectDoesNotExist:
        error = "Cart Not Found"
    except Exception as e:
        print(e)
        error = "Something Went Wrong while deleting item from Cart"
    if not error:
        info = "Item deleted from Cart successfully"
    inventory = Inventory.objects.all()
    return render(
        request, "dashboard.html", {
            'inventory': inventory, 'i': info, 'e': error})


# View to Handle the View Cart functionality
@login_required(login_url="")
def show_cart_view(request):
    '''
    View to show the cart
    :param request: request from the web
    :return: my cart web page
    '''
    carts = Cart.objects.filter(user=request.user, is_active=True)
    return render(request, "my_cart.html", {'carts': carts})


# View to Place the Order
@login_required(login_url="")
def place_order_view(request):
    '''
    View to place the order
    :param request: request from the web
    :return: place order and return to dashboard
    '''
    carts = Cart.objects.filter(user=request.user, is_active=True)
    carts_li = ""
    for cart in carts:
        carts_li += str(cart.id)
        carts_li += "-"
        cart.is_active = False
        cart.save()
    order = Order()
    order.user_id = request.user
    order.carts = carts_li
    order.save()
    from django.core.mail import send_mail
    from django.conf import settings
    send_mail('Your Order with ABC',
              'Your Order Places successfully, to view orders go to your orders on website.',
              settings.EMAIL_HOST_USER,
              [request.user.email],
              fail_silently=False)
    return HttpResponseRedirect("/")


# View to Show the Order
@login_required(login_url="")
def show_order_view(request):
    '''
    View to show the orders
    :param request: request from the web
    :return: shows the web page containing all the previous orders
    '''
    orders = Order.objects.filter(user_id=request.user)
    ords = []
    for order in orders:
        carts = order.carts[:-1].split("-")
        for cart in carts:
            temp = {}
            cart_obj = Cart.objects.get(id=int(cart))
            temp["item"] = cart_obj.item.item_name
            temp["quantity"] = cart_obj.quantity
            ords.append(temp)
    return render(request, 'show_orders.html', {"orders": ords})
