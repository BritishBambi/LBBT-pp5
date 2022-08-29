import os
from django.test import TestCase

# Create your tests here.


class TestViews(TestCase):
    """
    TC1 - Test Home Page
    TC2 - Test About us Page
    """

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
