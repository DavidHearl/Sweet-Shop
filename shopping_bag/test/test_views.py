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

    def test_add_to_bag(self):
        """ Test Adding product to shopping bag """
        product = Product.objects.create(
            name='Test Product',
            price='0.99',
            vegetarian=False,
            description='Test Description',
            image="Test image",
            )
        response = self.client.post(f'/shopping_bag/add/{product.id}/', {
            'quantity': 1,
            'redirect_url': f'/products/{product.id}/'})
        self.assertRedirects(response, f'/products/{product.id}/')

    def test_remove_item_from_bag(self):
        """ Test removing products from the shopping bag """
        product = Product.objects.create(
            name='Test Product',
            price='0.99',
            vegetarian=False,
            description='Test Description',
            image="Test image",
            )
        self.client.post(f'/shopping_bag/add/{product.id}/', {
            'quantity': 1,
            'redirect_url': f'/products/{product.id}/'})

        response = self.client.get(f'/shopping_bag/remove/{product.id}/')
        shopping_bag = self.client.session['shopping_bag']

        self.assertEqual(shopping_bag, {})
        self.assertEqual(response.status_code, 200)
