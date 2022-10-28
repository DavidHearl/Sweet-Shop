""" Test Checkout Urls work correctly """
from django.test import TestCase
from django.urls import reverse, resolve
from checkout.views import checkout, \
    checkout_completed_successfully, cache_checkout_data


class TestUrls(TestCase):
    """ Test the response of the checkout app's URLs """

    def test_response_of_checkout_page(self):
        """ Test the response of the checkout URL """
        url = reverse('checkout')
        self.assertEqual(resolve(url).func, checkout)

    def test_response_of_checkout_success_page(self):
        """ Test the response of the checkout success URL """
        url = reverse('checkout_completed_successfully', args=['THD3591GER'])
        self.assertEqual(resolve(url).func, checkout_completed_successfully)

    def test_response_of_cache_checkout_data(self):
        """ Test the response of the cache checkout data URL """
        url = reverse('cache_checkout_data')
        self.assertEqual(resolve(url).func, cache_checkout_data)
