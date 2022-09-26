# Testing

## Table of Contents

- Google's Lighthouse Performance
- Accessability Validation
- HTML Validation
- CSS Validation
- JS Validation
- PEP8 Validation
- Manual Testing
- Automated Testing
- Responsive Testing

## HTML Validation - https://validator.w3.org/
---

### Home
- Home Page
- Sign Up Page
- Sign In Page
- Logout Page

### Products
- Products Page
- Product Details
- Update Product

### Favourites
- Favourites Page

### Shopping Bag 
- Shopping bag Page

### Checkout
- Checkout Summary Page
- Checkout Page
- Checkout Success Page=

## CSS Validation - https://jigsaw.w3.org/css-validator/validator.html.en
---

![CSS Validation](./testing_images/CSS%20Validator.png "CSS Validation")

## PEP 8 Validation - http://pep8online.com/
---

#### Checkout
- Admin.py

![Checkout Admin](./testing_images/checkout-admin.png "Checkout Admin")

- Forms.py

![Checkout Forms](./testing_images/checkout-forms.png "Checkout Forms")

- Models.py

![Checkout Models](./testing_images/checkout-models.png "Checkout Models")

- Urls.py

![Checkout Urls](./testing_images/checkout-urls.png "Checkout Urls")

- Views.py

![Checkout Views](./testing_images/checkout-views.png "Checkout Views")

- Webhook handler.py
- There seems to be an issue with the webhook handler where it is causing errors on the tab indentation. I have reformatted the document as indent with tabs instead of spaces. Since the warnings do not effect the site at all I have elected to ignore the issue .

![Checkout Webhook Handler](./testing_images/checkout-webhookhandler.png "Webhook Handler")

- Webhook.py
- In the webhook.py file an error is causes due to line length. The readability would be greatly reduced if I was to ammend this issue and Django allows an extension to 99 characters in certain circumstances. Therefore it is best to overlook this issue

![Checkout Webhook](./testing_images/checkout-webhook.png "Checkout Webhook")

#### Favourites
- Models.py

![Favourties Models](./testing_images/favourites-models.png "Favourties Models")

- Urls.py

![Favourites Urls](./testing_images/favourites-urls.png "Favourites Urls")

- Views.py

![](./testing_images/favourites-views.png "")

#### Home

- Urls.py

![](./testing_images/home-urls.png"")

- Views.py

![](./testing_images/home-views.png"")

#### Products

- admin.py

![](./testing_images/products-admin.png "")

- forms.py

![](./testing_images/products-forms.png "")

- models.py

![](./testing_images/products-models.png "")

- urls.py

![](./testing_images/checkout-urls.png "")

- views.py

![](./testing_images/products-views.png "")

- widgets.py

![](./testing_images/products-widgets.png "")

#### Profiles

- forms.py

![](./testing_images/profiles-forms.png "")

- models.py

![](./testing_images/profiles-models.png "")

- urls.py

![](./testing_images/products-urls.png "")

- views.py

![](./testing_images/profiles-views.png "")


#### Shopping Bag

- contexts.py

![](./testing_images/shoppingbag-contexts.png "")

- urls.py

![](./testing_images/shoppingbag-urls.png "")

- views.py

![](./testing_images/shoppingbag-views.png "")

## Manual Testing


## Automated Testing

![Business Model](./media/test_urls.png "Title")

## Responsive Testing