"""Products Tests Views"""
from django.test import TestCase
from django.contrib.messages import get_messages
from django.contrib.auth.models import User
from products.models import Category, Product


class TestProductModels(TestCase):
    """ Test category and product views """
    def setUp(self):
        """ Create test user, category and product"""
        User.objects.create_user(
            username='test_user', password='test_password')

        User.objects.create_superuser(
            username='test_super_user', password='test_password')

        Category.objects.create(
            name='test-category', friendly_name='test category')

        Product.objects.create(
            name='Test Product Name',
            price='0.99',
            vegetarian=False,
            description='Test Description',
        )

    def test_user_count(self):
        """ Test users """
        user_count = User.objects.all().count()
        self.assertEqual(user_count, 2)

    def test_url_response(self):
        """ test url """
        response = self.client.get('/products/')
        self.assertEqual(response.status_code, 200)

    def test_get_all_products(self):
        """ Test all products """
        response = self.client.get('/products/', {
            'search_term': 'test', 'current_categories': 'test'})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/products.html')

    def test_get_product_detail(self):
        """ Test product detail view """
        product = Product.objects.get()
        response = self.client.get(f'/products/{product.id}/', {'product': product, 'product_in_favourites': 'true'})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/product_detail.html')
