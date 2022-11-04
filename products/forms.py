from django import forms
from .widgets import CustomClearableFileInput
from .models import Product, Category, Review


class ModifyProductsForm(forms.ModelForm):
    """ Form to add a product to the database """
    class Meta:
        model = Product
        fields = '__all__'

    image = forms.ImageField(
        label='Image', required=True, widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields['category'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black'


class ManageInventoryForm(forms.ModelForm):
    """ Form to modify the pricing of products """
    class Meta:
        model = Product
        fields = ('price',)


class ReviewForm(forms.ModelForm):
    """ Form to add a review about the product """
    class Meta:
        model = Review
        fields = ('name', 'content')
