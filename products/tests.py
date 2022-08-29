import os
from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Product, Review

# Create your tests here.


class TestViews(TestCase):
    """

    """
    def setUp(self):
        """ Create test login user and create Profile entry"""
        username = "jojo"
        pswd = "Trials"
        user_model = get_user_model()
        self.user = user_model.objects.create_user(username=username,
                                                   password=pswd,
                                                   is_superuser=True)
        logged_in = self.client.login(username=username, password=pswd)

        self.assertTrue(logged_in)

    def test_products_page(self):
        """ TC1 - Test all products view renders correct page """

        response = self.client.get('/products/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/products.html')

    def test_product_detail_page(self):
        """ TC2 - Test product detail view """
        Product.objects.get_or_create(
            name="Cheescake",
            description="Food to eat",
            price="5.00",
        )
        response = self.client.get('/products/1/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/product_detail.html')

    def test_review_page(self):
        """ TC3 - Test Review Screen Renders Correctly """
        user = self.user
        Product.objects.get_or_create(
            name="Cheesecake",
            description="Food to eat",
            id="1",
            price="5.00",
        )

        product = Product.objects.get(id="1")

        Review.objects.get_or_create(
            user=self.user,
            product=product,
            rate='3'
        )

        review = Review.objects.get(user=user, product=product)

        response = self.client.post('/products/1/rate/')
        self.assertTemplateUsed(response, 'products/product_review.html')
        self.assertTrue(review.product.name == "Cheesecake")

    def test_view_review_page(self):
        """ TC4 - Test Review Detail Screen Renders Correctly """
        user = self.user
        Product.objects.get_or_create(
            name="Cheesecake",
            description="Food to eat",
            id="1",
            price="5.00",
        )

        product = Product.objects.get(id="1")

        Review.objects.get_or_create(
            user=self.user,
            product=product,
            rate='3'
        )

        review = Review.objects.get(user=user, product=product)

        response = self.client.get('/products/1/review/jojo/')
        self.assertTemplateUsed(response, 'products/review_detail.html')
        self.assertTrue(review.product.name == "Cheesecake")
