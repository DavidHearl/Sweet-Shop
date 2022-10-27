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

    def test_add_product_to_favourites(self):
        """
        Test for adding a product to favourites
        """
        self.client.login(username='test_user', password='test_password')
        product = Product.objects.create(
            name='Test Product Name',
            price='0.99',
            vegetarian=False,
            description='Test Description',
        )
        response = self.client.post(f'/favourites/add_to_favourites/'
                                    f'{product.id}/')
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(
            str(messages[0]), "Added the product to your favourites")

    def test_remove_product_from_favourites(self):
        """
        This test removes a product from the users favourites
        """
        test_user1 = User.objects.create_user(
            username='test_user1', password='test_password')
        self.client.login(username='test_user1', password='test_password')
        test_user1 = User.objects.get(username='test_user1')
        product = Product.objects.create(
            name='Test Product Name 2',
            price='0.99',
            vegetarian=False,
            description='Test Description',
        )
        product = Product.objects.get(name='Test Product Name 2')
        favourites = Favourites.objects.create(username=test_user1)
        favourites.products.add(product)
        redirect_from = 'favourites'
        response = self.client.get(
            f'/favourites/remove_from_favourites/'
            f'{product.id}/{redirect_from}/')
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(
            str(messages[0]), 'Removed the product from your favourites list')
