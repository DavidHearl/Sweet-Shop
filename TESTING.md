# Testing

## Table of Contents

[HTML Validation](#html-validation)

[CSS Validation](#css-validation)

[JS Validation](#javascript-validation)

[PEP8 Validation](#pep-8-validation)

[Google's Lighthouse Performance](#lighthouse-testing)

[User Story Testing](#user-story-testing)

[Automated Testing](#automated-testing)

[Responsive Testing](#responsive-testing)

[Credentials](#credentials)

## HTML Validation

[Back To Top](#table-of-contents)

https://validator.w3.org/

Home

![Home HTML Validation](./testing_images/html_validation/html_home.png "HTML Home Validation")

All Products

![All Products HTML Validation](./testing_images/html_validation/html_all_products.png "HTML All Products Validation")

Product Detail

![Product Detail HTML Validation](./testing_images/html_validation/html_product_detail.png "HTML Product Detail Validation")

Add Products

![Add Products HTML Validation](./testing_images/html_validation/html_add_product.png "HTML Add Product Validation")

Manage Inventory

![Manage Inventory HTML Validation](./testing_images/html_validation/html_manage_inventory.png "HTML Manage Inventory Validation")

My Profile

![Profile HTML Validation](./testing_images/html_validation/html_profile_validation.png "HTML Profile Validation")

My Favourites

![Favourite HTML Validation](./testing_images/html_validation/html_favourites.png "HTML Favourite Validation")

Shopping Bag (Empty)

![Shopping Bag Empty HTML Validation](./testing_images/html_validation/html_shopping_bag_empty.png "HTML Shopping Bag Empty Validation")

Shopping Bag (Items)

![Shopping Bag Items HTML Validation](./testing_images/html_validation/html_shopping_bag_items.png "HTML Shopping Bag Items Validation")

Checkout

![Checkout HTML Validation](./testing_images/html_validation/html_checkout.png "HTML Checkout Validation")

## CSS Validation 

[Back To Top](#table-of-contents)

https://jigsaw.w3.org/css-validator/validator.html.en

![CSS Validation](./testing_images/CSS%20Validator.png "CSS Validation")

CSS Passes all validation. However, sometimes parse erros can be returned by the validator. If you follow the URL which the error is associated with you can see that it is an issue associated with bootstrap so can be disregarded.

## Javascript Validation

[Back To Top](#table-of-contents)

https://jshint.com

## PEP 8 Validation

[Back To Top](#table-of-contents)

http://pep8online.com/

Upon time of writing the pep 8 website is currently down. This means it is impossible to get screenshots of python files passing validation. As a work around I have installed pycodestyle as a linter. This shows up any issues in the development environment.

The Screen shots below were taken before the website went down.

Checkout / Admin.py

![Checkout Admin](./testing_images/pep8_validation/checkout-admin.png "Checkout Admin")

Checkout / Forms.py

![Checkout Forms](./testing_images/pep8_validation/checkout-forms.png "Checkout Forms")

Checkout / Models.py

![Checkout Models](./testing_images/pep8_validation/checkout-models.png "Checkout Models")

Checkout / Urls.py

![Checkout Urls](./testing_images/pep8_validation/checkout-urls.png "Checkout Urls")

Checkout / Views.py

![Checkout Views](./testing_images/pep8_validation/checkout-views.png "Checkout Views")

#### Favourites
- Models.py

![Favourties Models](./testing_images/pep8_validation/favourites-models.png "Favourties Models")

- Urls.py

![Favourites Urls](./testing_images/pep8_validation/favourites-urls.png "Favourites Urls")

- Views.py

![Favourites Views](./testing_images/pep8_validation/favourites-views.png "Favourites Views")

#### Home

- Urls.py

![Home Urls](./testing_images/pep8_validation/home-urls.png "")

- Views.py

![Home Views](./testing_images/pep8_validation/home-views.png "")

#### Products

- admin.py

![Product Admin](./testing_images/pep8_validation/products-admin.png "")

- forms.py

![Product Forms](./testing_images/pep8_validation/products-forms.png "")

- models.py

![Product Models](./testing_images/pep8_validation/products-models.png "")

- urls.py

![Product Urls](./testing_images/pep8_validation/checkout-urls.png "")

- views.py

![Product Views](./testing_images/pep8_validation/products-views.png "")

- widgets.py

![Product Widgets](./testing_images/pep8_validation/products-widgets.png "")

#### Profiles

- forms.py

![Profile Forms](./testing_images/pep8_validation/profiles-forms.png "")

- models.py

![Profile Models](./testing_images/pep8_validation/profiles-models.png "")

- urls.py

![Profile Urls](./testing_images/pep8_validation/products-urls.png "")

- views.py

![Profile Views](./testing_images/pep8_validation/profiles-views.png "")

#### Shopping Bag

- contexts.py

![Shopping Bag Contexts](./testing_images/pep8_validation/shoppingbag-contexts.png "")

- urls.py

![Shopping Bag Urls](./testing_images/pep8_validation/shoppingbag-urls.png "")

- views.py

![Shopping Bag Views](./testing_images/pep8_validation/shoppingbag-views.png "")

## Lighthouse Testing

[Back To Top](#table-of-contents)

Home

## User Story Testing

[Back To Top](#table-of-contents)

1. As a site user I want to be able to easily register for an account so that I can have a personal account and be able to view my profile
2. As a site user I want to be able to easily login and logout of an account so I can access my personal account information
3. As a site user I want to be able to recover my password so that I can still login even if I have forgotten my details
4. As a site user I want to recive an email confirmation after I have registered for an account so that I can verify my account was created successfully
5. As a site user I want to have a personalised profile so that I can view my previous orders and order confirmations
6. As a site user I want to be able to save my payment information so that I can checkout quicker next time I visit the site
7. As a shopper I want to view a list of products so that I can choose items to purchase
8. As a shopper I want to view individual product details so that I can see the product description, price, and rating
9. As a shopper I want to identify deals easily so that I can take advantage of savings on products that I would like to purchase
10. As a shopper I want to see my purchase total at all times so I can keep track of how much I am going to spend
11. As a shopper I want to be able to sort the list of available products so that I can easily find the products with the best rating and best price
12. As a shopper I want to be able to sort for a specific category of product so that I can look for products with the best price and best rating in that category
13. As a shopper I want to be able to sort by price or rating within a specific category so that I can find products easily
14. As a shopper I want to search for a product by name or description so I can find a specific product I would like to purchase
15. As a shopper I want to see what I have searched for and how many result have been returned so I can quickly see if the product I want to purchase is available
16. As a shopper I want to be able to select the quantity when purchasing an item so that I can order more then 1 item
17. As a shopper I want to view the items currently in my bad to summarise my purchases and the cost
18. As a shopper I want to adjust the quantity of items in my shopping bag so I can easily make changes to my purchases before checkout
19. As a shopper I want to be able to easily enter in my payment information so I can have a hassel free experience
20. As a shopper I want to feel that my personal information is safe so that I can confiently provide the information required to make a purchase
21. As a shopper I want to view and order confirmation after checkout to verify that I haven't made any mistakes
22. As a shopper I want to recieve and email confirmation after checkout so I can keep the confirmation of the purchase for my records
23. As a store owner I want to be able to add new items to my store so that I can add newly released products to the store
24. As a store owner I want to be able to edit/update products in my store so that I can adjust price, descriptions, images and other criteria
25. As a store owner I want to be able to delete a product so that I can remove items that are no longer in stock or are not for sale

## Automated Testing

[Back To Top](#table-of-contents)

Automated Unit Testing werer carried out using Django's inbuilt testing tools. Tools were written to cover a large variety of the site. Below Are instructions on how to run the tests, with an overview of the __29__ tests.

Before testing can begin the database needs to be disabled. To do this we need to go into the env.py file and comment out the "DATABASE_URL" value which should be mapped to our postgres database. Once this is done, you can run the tests with the following command.

Terminal Command : python3 manage.py test

It is important to note the file structure required for the tests. Within each application there needs to be a folder called "test", as an example the checkout folder stucture is as follows : sweet_shop/checkout/test/*test_xxx_xxx.py*. Within the test file there also needs to be a blank dunder init file.

### Checkout Appication (11)
    - Forms (6)
        - test_full_name_required                       [Passed]
        - test_email_required                           [Passed]
        - test_phone_number_required                    [Passed]
        - test_street_address_required                  [Passed]
        - test_town_or_city_required                    [Passed]
        - test_country_is_required                      [Passed]
    - Models (1)
        - test_order_string                             [Passed]
    - Urls (3)
        - test_response_of_checkout_page                [Passed]
        - test_response_of_checkout_success_page        [Passed]
        - test_response_of_cache_checkout_data          [Passed]
    - Views (1)
        - test_empty_bag_error                          [Passed]

### Favourite Appication (4)
    - Models (1)
        - test_favourites_string_method                 [Passed]
    - Views (3)
        - test_get_product_favourites_page              [Passed]
        - test_add_product_to_favourites                [Passed]
        - test_remove_product_from_favourites           [Passed]

### Home Appication (1)
    - Views (1)
        - test_page_access                              [Passed]

### Products Appication (7)
    - Models (2)
        - test_category_returns_name                    [Passed]
        - test_product_returns_name                     [Passed]
    - Views (5)
        - test_user_count                               [Passed]
        - test_url_response                             [Passed]
        - test_get_all_products                         [Passed]
        - test_superuser_can_add_product                [Passed]
        - test_non_superuser_can_not_add_product        [Passed]

### Profiles Appication (3)
    - Models (1)
        - test_profile_string_method                    [Passed]
    - Views (2)
        - test_url_response                             [Passed]
        - test_profile_view_template                    [Passed]

### Shopping Bag Appication (2)
    - Views (2)
        - test_add_to_bag                               [Passed]
        - test_remove_item_from_bag                     [Passed]


![Business Model](./testing_images/automated_testing.PNG "Title")

## Responsive Testing

[Back To Top](#table-of-contents)

| Page | Desktop | Tablet | Mobile |
|:-:|:-:|:-|:-:|
|Home||||
|All Products||||
|Product Detail||||
|Add Products||||
|Manage Inventory||||
|My Profile||||
|My Favourites||||
|Shopping Bag (Empty)||||
|Shopping Bag (Items)||||
|Checkout||||

## Credentials

[Back To Top](#table-of-contents)

To test higher functionality of the site, the admin credentials found below can be used

__Username : admin__

__Password : admin-password__

To test lower functionality the user can register for an account on the site.
