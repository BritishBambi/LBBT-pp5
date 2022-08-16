from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    """Model to create the product catagory"""
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_freindly_name(self):
        return self.friendly_name


class Product(models.Model):
    """Product model containing all the information needed for product page"""
    category = models.ForeignKey(
        'Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True, default='placeholder.jpg')


RATE_CHOICES = [
    (1, '1 - Terrible'),
    (2, '2 - Not the best'),
    (3, '3 - Alright'),
    (4, '4 - Very good'),
    (5, '5 - Delicious!'),
]


class Review(models.Model):
    """Review model to relate to a product page and display the score"""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    text = models.TextField(max_length=3000, blank=True)
    rate = models.PositiveSmallIntegerField(choices=RATE_CHOICES)


class Recipe(models.Model):
    """Product recipe to be detailed on a product page"""
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    recipe = models.TextField(max_length=3000, blank=True)
