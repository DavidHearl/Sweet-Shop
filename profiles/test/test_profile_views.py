""" Profiles Test Views """
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.messages import get_messages
from checkout.models import Order
from profiles.models import UserProfile


class TestProfilesViews(TestCase):
    """ Test Profile Views """

    def setUp(self):
        """ Setup test """
        testuser = User.objects.create_user(
            username='test_user',
            password='test_password',
            email='test@test.com')
        testuser.save()

        Order.objects.create(
            order_number='987654321',
            user_profile=UserProfile.objects.get(user=testuser),
            full_name='Test User',
            email='test@test.com',
            phone_number='1234567890',
            country='Test Country',
            postcode='Test postcode',
            town_or_city='Test city',
            street_address1='Test address',
            county='Test country',
        )

    def test_url_response(self):
        """ Test users can see their profile """
        login = self.client.login(username='test_user',
                                  password='test_password')
        response = self.client.get('/profiles/')
        self.assertTrue(login)
        self.assertEqual(response.status_code, 200)

    def test_profile_view_template(self):
        """ User profile uses correct template """
        login = self.client.login(username='test_user',
                                  password='test_password')
        response = self.client.get(reverse('user_profile'))
        self.assertTrue(login)
        self.assertTemplateUsed(response, 'profiles/user_profiles.html')
