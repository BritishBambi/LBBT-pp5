from django.shortcuts import render, redirect, reverse, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower

from .models import Product, Category, Recipe, Review
from .forms import RateForm

# Create your views here.


def all_products(request):
    """ A Simple view to render all the products """

    products = Product.objects.all()
    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) | Q(
                description__icontains=query)
            products = products.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ A view to render an individual product detail page"""

    # product = get_object_or_404(Product, pk=product_id)
    product = Product.objects.get(id=product_id)
    recipies = Recipe.objects.get(product=product)

    context = {
        'product': product,
        'recipies': recipies,
    }

    return render(request, 'products/product_detail.html', context)


@login_required
def reviewProduct(request, product_id):

    product = Product.objects.get(id=product_id)
    user = request.user

    if Review.objects.filter(product=product, user=user).exists():
        review_exists = True
    else:
        review_exists = False

    if request.method == 'POST':
        form = RateForm(request.POST)
        if form.is_valid():
            rate = form.save(commit=False)
            rate.user = user
            rate.product = product
            rate.save()
            messages.success(request, 'Review saved')

            return HttpResponseRedirect(
                reverse('product_detail', args=[product_id])
                )

    else:
        form = RateForm()

    template = 'products/product_review.html'

    context = {
        'product': product,
        'form': form,
        'review_exists': review_exists,
    }

    return render(request, template, context)
