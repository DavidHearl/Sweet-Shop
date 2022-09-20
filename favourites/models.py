from django.db import models
from django.contrib.auth.models import User
from products.models import Product

class Favourites(models.Model):
    """ Model to select favourites """

    products = models.ManyToManyField(Product, blank=True)
    username = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        """ Return object string """

        return f"{self.username}'s Favourites"
