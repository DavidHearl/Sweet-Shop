"""Shopping Bag Tests"""
from django.test import TestCase
from products.models import Product


class TestViews(TestCase):
    """ Test views in the shopping bag """
    def test_view_bag(self):
        """ Test user can access the shopping bag """
        response = self.client.get('/shopping_bag/')
        self.assertTemplateUsed(response, 'shopping_bag/shopping_bag.html')
        self.assertEqual(response.status_code, 200)
