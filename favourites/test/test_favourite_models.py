""" Favourites test models """
from django.contrib.auth.models import User
from django.test import TestCase
from favourites.models import Favourites
from products.models import Product


class TestFavouriteModels(TestCase):
    """ Test the favourites models """
    def setUp(self):
        """
        Create test users, product and favourite
        """
        test_user = User.objects.create_user(
            username='test_user', password='test_password')

        Product.objects.create(
            name='Test Product Name',
            price='0.99',
            vegetarian=False,
            description='Test Description',
        )

        Favourites.objects.create(
            username=test_user
        )

    def test_favourites_string_method(self):
        """ Test the favourite string method """
        favourite = Favourites.objects.get()
        self.assertEqual((favourite.__str__()), "test_user's Favourites")