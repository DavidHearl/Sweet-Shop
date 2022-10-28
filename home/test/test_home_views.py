""" Test home views """
from django.test import TestCase
from django.contrib.messages import get_messages


class TestHomeViews(TestCase):
    """ Test home view """
    def test_page_access(self):
        """ Test the home page """
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
