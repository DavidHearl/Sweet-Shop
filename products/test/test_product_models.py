""" Products Tests Models """
from django.test import TestCase
from django.contrib.auth.models import User
from products.models import Category, Product

class TestProductModels(TestCase):
    """ Testing Category, Product and ReviewRating models """
    def setUp(self):
        """ Setup tests. Create product, category and user """
        test_user = User.objects.create_user(
            username='test_user', password='test_password')

        Category.objects.create(
            name='test-category', friendly_name='test category')

        product = Product.objects.create(
            name='Test Product Name',
            price='0.99',
            vegetarian=False,
            description='Test Description',
        )

    def test_category_returns_name(self):
        """ Test category to see if it returns its friendly name """
        category = Category.objects.get(name='test-category')
        self.assertEqual((category.__str__()), category.name)
        self.assertEqual(category.get_friendly_name(), category.friendly_name)

    def test_product_returns_name(self):
        """  Test Product to see if it returns name as a string """
        product = Product.objects.get(name='Test Product Name')
        self.assertEqual((product.__str__()), product.name)
