"""Test Checkout Views"""
from django.test import TestCase
from django.contrib.auth.models import User
from django.contrib.messages import get_messages
from checkout.models import Order


class TestCheckoutViews(TestCase):
    """ Test the checkout views """

    def setUp(self):
        """ Setup Tests """
        testuser = User.objects.create_user(
            username='test_user',
            password='test_password',
            email='test@test.com')
        testuser.save()

        Order.objects.create(
            order_number='987654321',
            full_name='Test User',
            email='test@test.com',
            phone_number='1234567890',
            country='Test Country',
            postcode='Test postcode',
            town_or_city='Test city',
            street_address1='Test address',
            county='Test country',
        )

    def test_empty_bag_error(self):
        """ Test if the shopping bag is empty """
        response = self.client.get('/checkout/')
        self.assertRedirects(response, '/products/')
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(
            str(messages[0]), "There's nothing in your \
                bag at the moment")
