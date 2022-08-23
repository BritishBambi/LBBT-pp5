import os
from django.test import TestCase
from django.contrib.auth import get_user_model


API_KEY = os.environ.get("API_KEY")

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

    def test_home_page(self):
        """ TC1 - Test home view renders correct page """
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/index.html')

    def test_about_us_page(self):
        """ TC2 - Test about us view renders the correct page"""
        response = self.client.get('/about_us/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/about_us.html')
