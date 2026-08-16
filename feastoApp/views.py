from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
import razorpay
from Feasto import settings

from .models import Cart, Customer, Restaurant, Items

# Create your views here.
def login(request):
    # return HttpResponse("Say hello my app is working!")
    return render(request, "index.html")

def open_signup(request):
    return render(request, "signup.html")

def open_signin(request):
    return render(request, "signin.html")

# def signup(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         email = request.POST.get('email')
#         mobile = request.POST.get('mobile')
#         address = request.POST.get('address')
#         try:
#             Customer.objects.get(username = username)
#             return HttpResponse("Duplicate Username!")
#         except:
#             Customer.objects.create(
#                 username = username,
#                 password = password,
#                 email = email,
#                 mobile = mobile,
#                 address = address,
#             )
#     return render(request, "signin.html") 
def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')
        address = request.POST.get('address')

        if Customer.objects.filter(username=username).exists():
            return HttpResponse("Duplicate Username!")

        Customer.objects.create(
            username=username,
            password=password,
            email=email,
            mobile=mobile,
            address=address,
        )

        return render(request, "signin.html")

    return render(request, "signup.html")

def signin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
    try:
        Customer.objects.get(username = username, password = password)
        if username == 'admin':
            return render(request, 'admin_home.html')
        else:
            restaurantList = Restaurant.objects.all()
            return render(request, 'customer_home.html', {"restaurantList":restaurantList, "username":username})
    except Customer.DoesNotExist:
        return render(request, 'fail.html', {"username":username})

def open_add_restaurant(request):
    return render(request, 'open_add_restaurant.html')

def add_restaurant(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        picture = request.POST.get('picture')
        cuisine = request.POST.get('cuisine')
        rating = request.POST.get('rating')

        if Restaurant.objects.filter(name=name).exists():
            return HttpResponse("Duplicate Restaurant!")

        Restaurant.objects.create(
            name=name,
            picture=picture,
            cuisine=cuisine,
            rating=rating,
        )

        return render(request, "admin_home.html")

    return render(request, "admin_home.html")

def open_show_restaurant(request):
    restaurantList = Restaurant.objects.all()
    return render(request, "show_restaurants.html", {"restaurantList": restaurantList})

def open_update_restaurant(request, restaurant_id):
    restaurant = Restaurant.objects.get(id = restaurant_id)
    return render(request, 'update_restaurant.html', {"restaurant":restaurant})

def update_restaurant(request, restaurant_id):
    restaurant = Restaurant.objects.get(id=restaurant_id)
    if request.method == 'POST':
        restaurant.name = request.POST.get('name')
        restaurant.picture = request.POST.get('picture')
        restaurant.cuisine = request.POST.get('cuisine')
        restaurant.rating = request.POST.get('rating')
        restaurant.save()
        restaurantList = Restaurant.objects.all()
        return render(request, "show_restaurants.html", {"restaurantList": restaurantList})

def delete_restaurant(request, restaurant_id):
    restaurant = Restaurant.objects.get(id = restaurant_id)
    restaurant.delete()
    restaurantList = Restaurant.objects.all()
    return render(request, "show_restaurants.html", {"restaurantList": restaurantList})

def open_update_menu(request, restaurant_id):
    restaurant = Restaurant.objects.get(id = restaurant_id)
    itemList = restaurant.items.all()
    return render(request, "update_menu.html", {"itemList":itemList, "restaurant":restaurant})

def update_menu(request, restaurant_id):
    restaurant = Restaurant.objects.get(id = restaurant_id)
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        price = request.POST.get('price')
        vegetarian = request.POST.get('vegetarian') == 'on'        
        picture = request.POST.get('picture')
        restaurant = restaurant
        if Items.objects.filter(name=name).exists():
            return HttpResponse("DUPLICATE FOOD ITEM!")
        Items.objects.create(
            name = name,
            description = description,
            price = price,
            vegetarian = vegetarian,
            picture = picture,
            restaurant = restaurant
        )
    return render(request, "admin_home.html")

def view_menu(request, restaurant_id, username):
    restaurant = Restaurant.objects.get(id=restaurant_id)
    itemList = restaurant.items.all()
    # itemList = Ictems.objects.all()
    return render(request, "customer_menu.html", {"itemList":itemList, "restaurant":restaurant, "username":username})

def add_to_cart(request, item_id, username):
    item = Items.objects.get(id=item_id)
    customer = Customer.objects.get(username = username)
    cart, created = Cart.objects.get_or_create(customer=customer)
    cart.items.add(item)
    return HttpResponse('ADDED TO CART')

def show_cart(request, username):
    customer = Customer.objects.get(username = username)
    cart = Cart.objects.filter(customer = customer).first()
    items = cart.items.all() if cart else []
    total_price = cart.total_price() if cart else 0
    return render(request, "cart.html", {"itemList":items, "total_price":total_price, "username":username})

def checkout(request, username):

    customer = get_object_or_404(Customer, username=username)

    cart = Cart.objects.filter(customer=customer).first()

    cart_items = cart.items.all() if cart else []

    total_price = cart.total_price() if cart else 0

    if total_price == 0:
        return render(request, 'checkout.html', {
            "error": "Your Cart is empty"
        })

    # Initialize Razorpay client
    client = razorpay.Client(
        auth=(
            settings.RAZORPAY_KEY_ID,
            settings.RAZORPAY_KEY_SECRET
        )
    )

    client.session.trust_env = False

    order_data = {
        'amount': int(total_price * 100),
        'currency': 'INR',
    }

    try:
        order = client.order.create(data=order_data)

    except Exception:
        return render(request, 'checkout.html', {
            'username': username,
            'cart_items': cart_items,
            'total_price': total_price,
            'error': 'Payment service is currently unreachable. Please check your internet/proxy settings',
        })

    return render(request, 'checkout.html', {
        'username': username,
        'cart_items': cart_items,
        'total_price': total_price,
        'razorpay_key_id': settings.RAZORPAY_KEY_ID,
        'order_id': order['id'],
        'amount_paise': order_data['amount'],
    })

def orders(request, username):
    customer = get_object_or_404(Customer, username=username)
    cart = Cart.objects.filter(customer=customer).first()

    cart_items = list(cart.items.all()) if cart else []

    print("BEFORE CLEAR:", cart_items)
    print("NUMBER OF ITEMS:", len(cart_items))

    total_price = cart.total_price() if cart else 0

    if cart:
        cart.items.clear()

    print("AFTER CLEAR:", list(cart.items.all()))

    return render(request, 'orders.html', {
        'username': username,
        'customer': customer,
        'cart_items': cart_items,
        'total_price': total_price,
    })
    
     
    
    
        
    
    