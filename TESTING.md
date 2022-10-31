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

![HTML Validation](./testing_images/html-validation.png "HTML Validation")

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

![Favourites Views](./testing_images/favourites-views.png "Favourites Views")

#### Home

- Urls.py

![](./testing_images/home-urls.png "")

- Views.py

![](./testing_images/home-views.png "")

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

Automated Unit Testing werer carried out using Django's inbuilt testing tools. Tools were written to cover a large variety of the site. Below Are instructions on how to run the tests, with an overview of the 29 tests.

Before testing can begin the database needs to be disabled. To do this we need to go into the env.py file and comment out the "DATABASE_URL" value which should be mapped to our postgres database. Once this is done, you can run the tests with the following command.

Terminal Command : python3 manage.py test

It is important to note the file structure required for the tests. Within each application there needs to be a folder called "test", as an example the checkout folder stucture is as follows : sweet_shop/checkout/test/*test_xxx_xxx.py*. Within the test file there also needs to be a blank dunder init file.

### Checkout Appication
    - Forms
        - test_full_name_required                       [Passed]
        - test_email_required                           [Passed]
        - test_phone_number_required                    [Passed]
        - test_street_address_required                  [Passed]
        - test_town_or_city_required                    [Passed]
        - test_country_is_required                      [Passed]
    - Models
        - test_order_string
    - Urls
        - test_response_of_checkout_page                [Passed]
        - test_response_of_checkout_success_page        [Passed]
        - test_response_of_cache_checkout_data          [Passed]
    - Views
        - test_empty_bag_error

### Favourite Appication
    - Models
        - test_favourites_string_method
    - Views
        - test_get_product_favourites_page
        - test_add_product_to_favourites
        - test_remove_product_from_favourites

### Home Appication
### Products Appication
### Profiles Appication
### Shopping Bag Appication




![Business Model](./testing_images/automated_testing.PNG "Title")

## Responsive Testing