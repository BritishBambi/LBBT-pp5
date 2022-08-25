from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag',{})
    if not bag:
        messages.error(request, "There's nothing currently in your bag")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51LaTeTKqUpIuVKpWHTwUCm7ZIvtiGeKYIwu5EVGiZZ8x7a6qFBtmOtJRjCMJu15p497jZIHxaUhNCemQFKQQFI1X006t405W7I',
        'client_test_secret': 'test_secret'
    }

    return render(request, template, context)
