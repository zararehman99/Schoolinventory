from django.shortcuts import render, redirect
from .models import InventoryItem, Order, OrderItem
from .forms import CartAddItemForm, CheckoutForm

def inventory(request):
    items = InventoryItem.objects.all()
    return render(request, 'inventory.html', {'items': items})

def add_to_cart(request, item_id):
    # Implement logic to add item to cart
    return redirect('cart')

def remove_from_cart(request, item_id):
    # Implement logic to remove item from cart
    return redirect('cart')

def cart(request):
    # Implement logic to display cart items
    return render(request, 'cart.html')

def checkout(request):
    # Implement logic for checkout process
    return render(request, 'checkout.html')


def add_to_cart(request, item_id):
    form = CartAddItemForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        # Handle form submission
        quantity = form.cleaned_data['quantity']
        # Add the item to the cart
    return redirect('cart')
