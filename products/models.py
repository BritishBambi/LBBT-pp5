from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

DEFAULT_IMAGE = ('https://res.cloudinary.com/jojocloudci/\
    image/upload/v1656561920/ez8n8onczraub6ag83ua.jpg')


class Category(models.Model):
    """Model to create the product catagory"""

    class Meta:
        """ Returns category plural name and friendly name """
        verbose_name_plural = 'Catagories'
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_freindly_name(self):
        """Retruns the category by its friendly name """
        return self.friendly_name


class Product(models.Model):
    """Product model containing all the information needed for product page"""
    category = models.ForeignKey(
        'Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(max_digits=6, decimal_places=2,
                                 null=True, blank=True)
    image = CloudinaryField('image', default=DEFAULT_IMAGE)

    def __str__(self):
        return self.name


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

    def __str__(self):
        return self.product.name


class Recipe(models.Model):
    """Product recipe to be detailed on a product page"""
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    recipe_title = models.CharField(max_length=100, blank=True)
    recipe = models.TextField(max_length=6000, blank=True)

    def __str__(self):
        return self.product.name


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    review = models.ForeignKey(Review, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    text = models.TextField(max_length=3000, blank=True, null=True)

    def __str__(self):
        return self.user.username
