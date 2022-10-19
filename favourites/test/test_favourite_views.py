""" Favourites test views """
from django.contrib.auth.models import User
from django.contrib.messages import get_messages
from django.test import TestCase
from favourites.models import Favourites
from products.models import Product


class TestFavouritesViews(TestCase):
    """ Favourite views testing """
    def setUp(self):
        """ Create test user """
        test_user = User.objects.create_user(
            username='test_user', password='test_password')

        Favourites.objects.create(
            username=test_user
        )

    def test_get_product_favourites_page(self):
        """ User can view thier favourites page """
        self.client.login(username='test_user', password='test_password')
        response = self.client.get('/favourites/')
        self.assertTemplateUsed(response, 'favourites/favourites.html')
        self.assertEqual(response.status_code, 200)

