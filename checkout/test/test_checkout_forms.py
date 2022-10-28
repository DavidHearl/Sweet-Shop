""" Test checkout forms """
from django.test import TestCase
from checkout.forms import OrderForm


class TestOrderForm(TestCase):
    """ Test the validators on the oreder form """

    def test_full_name_required(self):
        """ Test if form submits while missing the full name field """
        form = OrderForm({
            'full_name': '',
            'email': 'test@test.com',
            'phone_number': '0123456789',
            'street_address1': 'Test_Street',
            'town_or_city': 'Test_City',
            'country': 'GBR',
        })
        self.assertFalse(form.is_valid())
        self.assertIn('full_name', form.errors.keys())
        self.assertEqual(
            form.errors['full_name'][0], 'This field is required.')

    def test_email_required(self):
        """ Test if form submits while missing the email field """
        form = OrderForm({
            'full_name': 'Test User',
            'email': '',
            'phone_number': '0123456789',
            'street_address1': 'Test_Street',
            'town_or_city': 'Test_City',
            'country': 'GBR',
        })
        self.assertFalse(form.is_valid())
        self.assertIn('email', form.errors.keys())
        self.assertEqual(
            form.errors['email'][0], 'This field is required.')

    def test_phone_number_required(self):
        """ Test if form submits while missing the phonenumber field """
        form = OrderForm({
            'full_name': 'Test User',
            'email': 'test@test.com',
            'phone_number': '',
            'street_address1': 'Test_Street',
            'town_or_city': 'Test_City',
            'country': 'GBR',
        })
        self.assertFalse(form.is_valid())
        self.assertIn('phone_number', form.errors.keys())
        self.assertEqual(
            form.errors['phone_number'][0], 'This field is required.')

    def test_street_address_required(self):
        """ Test if form submits while missing the street address field """
        form = OrderForm({
            'full_name': 'test',
            'email': 'test@test.com',
            'phone_number': '0123456789',
            'street_address1': '',
            'town_or_city': 'Test_City',
            'country': 'GBR',
        })
        self.assertFalse(form.is_valid())
        self.assertIn('street_address1', form.errors.keys())
        self.assertEqual(
            form.errors['street_address1'][0], 'This field is required.')

    def test_town_or_city_required(self):
        """ Test if form submits while missing the town/city field """
        form = OrderForm({
            'full_name': 'test',
            'email': 'test@test.com',
            'phone_number': '0123456789',
            'country': 'GBR',
            'town_or_city': '',
            'street_address1': 'test',
        })
        self.assertFalse(form.is_valid())
        self.assertIn('town_or_city', form.errors.keys())
        self.assertEqual(
            form.errors['town_or_city'][0], 'This field is required.')

    def test_country_is_required(self):
        """ Test if form submits while missing the country field """
        form = OrderForm({
            'full_name': 'Test User',
            'email': 'test@test.com',
            'phone_number': '0123456789',
            'street_address1': 'Test_Street',
            'town_or_city': 'Test_City',
            'country': '',
        })
        self.assertFalse(form.is_valid())
        self.assertIn('country', form.errors.keys())
        self.assertEqual(
            form.errors['country'][0], 'This field is required.')
