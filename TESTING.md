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

### HTML Validation - https://validator.w3.org/


### PEP 8 Validation - http://pep8online.com/

Readability would be drastically reduced if the line length was decreased. As Django allows an increase to 99 characters in certain circumstances it is more user friendly if this is left as is

#### Checkout
- PASS : admin.py, apps.py, forms.py, models.py, urls.py, views.py
- FAIL : webhook_handler.py > line 71, 72 > line too long 80 > 79
- FAIL : checkout > webhook_handler.py > line 132 > line too long 81 > 79

#### Favourites
- PASS : admin.py, apps.py, forms.py, models.py, tests.py, urls.py, views.py

#### Home
- PASS : admin.py, apps.py, forms.py, models.py, tests.py, urls.py, views.py

#### Products
- PASS : admin.py, apps.py, forms.py, models.py, tests.py, urls.py, views.py, widgets.py

#### Profiles
- PASS : admin.py, apps.py, forms.py, models.py, tests.py, urls.py, views.py

#### Shopping Bag
- PASS : admin.py, apps.py, contexts.py, models.py, tests.py, urls.py, views.py

### CSS Validation - https://jigsaw.w3.org/css-validator/validator.html.en
PASS - static/css/base.css


## Manual Testing


## Automated Testing

![Business Model](./media/test_urls.png "Title")

## Responsive Testing