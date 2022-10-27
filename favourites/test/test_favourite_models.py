""" Favourites test models """
from django.contrib.auth.models import User
from django.test import TestCase
from favourites.models import Favourites
from products.models import Product


class TestFavouriteModels(TestCase):
    """
    Testing for favourites models
    """
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

    def test_favourites_str_method(self):
        """
        This test tests the favourites str method
        """
        favourite = Favourites.objects.get()
        self.assertEqual((favourite.__str__()), "test_user's Favourites")