from django.shortcuts import render, redirect, reverse, \
     HttpResponseRedirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Q, Avg
from django.db.models.functions import Lower

from .models import Product, Category, Recipe, Review, Comment
from .forms import RateForm, ProductForm, CommentForm

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
                messages.error(request,
                               "You didn't enter any search criteria!")
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

    product = Product.objects.get(id=product_id)
    recipies = Recipe.objects.filter(product=product)

    reviews = Review.objects.filter(product=product)
    reviews_avg = reviews.aggregate(Avg('rate'))
    reviews_count = reviews.count()

    context = {
        'product': product,
        'recipies': recipies,
        'reviews': reviews,
        'reviews_avg': reviews_avg,
        'reviews_count': reviews_count,
    }

    return render(request, 'products/product_detail.html', context)


@login_required
def review_product(request, product_id):
    """ A View that checks for a valid post method
    to save the review to the product and user """

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


def view_review(request, product_id, username):
    """ A view that finds and renders all existing
    reviews for a product in the template """

    user = get_object_or_404(User, username=username)
    product = Product.objects.get(id=product_id)
    review = Review.objects.get(user=user, product=product)
    comment = Comment.objects.filter(review=review)

    if Comment.objects.filter(review=review, user=user).exists():
        comment_exists = True
    else:
        comment_exists = False

    template = 'products/review_detail.html'

    context = {
        'review': review,
        'comment_exists': comment_exists,
        'product': product,
        'comment': comment,
    }

    return render(request, template, context)


@login_required()
def delete_review(request, username, product_id):
    """
    Checks for a valid POST request from the delete_review page
    to simply delete the exisitng review model. The user will then
    be returned to the product page.
    """
    user = get_object_or_404(User, username=username)
    product = Product.objects.get(id=product_id)
    review = Review.objects.get(user=user, product=product)

    if request.method == 'POST':
        review.delete()
        messages.success(request, 'Review Deleted')
        return HttpResponseRedirect(
            reverse('product_detail', args=[product_id]))

    context = {
        'review': review,
        'product': product,
    }

    return render(request, 'products/delete_review.html', context)


@login_required
def review_comment(request, product_id, username):
    """ A View that checks for a valid post method
    to save the comment to the product and user """

    product = Product.objects.get(id=product_id)
    user = User.objects.get(username=username)
    review = Review.objects.get(user=user, product=product)

    if Comment.objects.filter(review=review, user=user).exists():
        comment_exists = True
    else:
        comment_exists = False

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.review = review
            comment.save()
            messages.success(request, 'Comment saved')

            return HttpResponseRedirect(
                reverse('view_review', args=[product_id, user.username])
                )

    else:
        form = CommentForm()

    template = 'products/reivew_comment.html'

    context = {
        'product': product,
        'form': form,
        'comment_exists': comment_exists,
    }

    return render(request, template, context)


@login_required()
def delete_comment(request, username, product_id):
    """
    Checks for a valid POST request from the delete_review page
    to simply delete the exisitng review model. The user will then
    be returned to the product page.
    """
    user = get_object_or_404(User, username=username)
    product = Product.objects.get(id=product_id)
    review = Review.objects.get(user=user, product=product)
    comment = Comment.objects.filter(review=review)

    if request.method == 'POST':
        comment.delete()
        messages.success(request, 'Comment Deleted')
        return HttpResponseRedirect(
            reverse('view_review', args=[product_id]))

    context = {
        'review': review,
        'product': product,
    }

    return render(request, 'products/delete_review.html', context)


@login_required()
def add_product(request):
    """ Add a product to the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry only store admins can do that')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(
                request, 'Failed to add product.\
                     Please ensure the form is valid.')
    else:
        form = ProductForm()

    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required()
def edit_product(request, product_id):
    """ Edit a product in the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry only store admins can do that')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to update product.\
                 Please ensure the form is valid.')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


@login_required()
def delete_product(request, product_id):
    """ Delete a product from the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry only store admins can do that')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product deleted!')
    return redirect(reverse('products'))
