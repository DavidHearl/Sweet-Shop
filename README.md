# The Sweet Shop - [Live Website](https://the-sweet-shop.herokuapp.com)

The live website can be viewed using the link : https://the-sweet-shop-davidhearl.herokuapp.com

## Table of Contents
---
1. [User Stories](#UserStories)
2. [Features](#Features)
3. [Databases](#Databases)
4. [Technologies Used](#TechnologiesUsed)
5. [Testing](#Testing)
6. [Validator Testing](#ValidatorTesting)
7. [Bugs Found](#BugsFound)
8. [Deployment](#Deployment)
9. [Acknowledgement](#Acknowledgement)

## Aim

The Sweet Shop is an ecommerce website that allows users to purchase a selection of confectionary items.
The sweetshop was developed for my 5th portfolio project as part of my Diploma in software development.

## About
---
The Sweet Shop website provides the user the ability to purchase a wide variety of sweets.
Upon landing on the site you are greeted with three main options which indicate the purpose of the site.

As a non logged in user you can browse all the products and add them to your bag ready for checkout.
You can then checkout by entering your details along with a valid card. Once your order is comple you will see a confirmation page and a confirmation email will be sent.
As a logged in user you will be able to checkout faster as you can save your information to your profile. You will also be able to view your order history and leave reviews on your favourite products.
A logged in user will also be able to add there favourite sweets to their own page for quick and easy access for repeat purchases.

## User registration

An important aspect of the site was to give the user an option to purchase items from the site without having to sign up.
Some users can find it frustrating being forced to sign up to a site before a purchase so I felt it was important to avoid this to limit any negative feedback on the site.

## Project Installation Requirements
---
- pip3 install Django==3.2
- pip3 install django-allauth
- pip3 install Pillow
- pip3 install django-crispy-forms
- pip3 install stripe
- pip3 install django-countries
- pip3 install dj_database_url
- pip3 install psycopg2-binary
- pip3 install gunicorn
- pip3 install boto3
- pip3 install django-storages

## Scope
---
- A simple intuitive UX experience;
- An easy navigation for the user;
- A site that is visually appealing and responsive across multiple devices

## Structure
- A straghtforward and clear layout is present to ensure users can navigate inutitvely and have a pleasant experience
- The navbar is fixed to the top of the page to ensure that the user can navigate the depths of the site with a couple of clicks at all time
- Footer is fixed on the bottom of all pages.

## Wireframes
---
Wireframes created with Balsamiq. The project was developed from initial wireframes.

![Desktop Home Page](./media/Desktop%20Home%20Page.png "Title")
![Desktop Products Page](./media/Desktop%20Products%20Page.png "Title")

![iPad Home Page](./media/iPad%20Home%20Page.png "Title")
![iPad Products Page](./media/iPad%20Products%20Page.png "Title")

![iPhone Home Page](./media/iPhone%20Home%20Page.png "Title")
![iPhone Products Page](./media/iPhone%20Products%20Page.png "Title")

## User Stories

| User Stories | Met |
|:----------|:---:|
|As a site user I want to be able to easily register for an account so that I can have a personal account and be able to view my profile|[x]|
|As a site user I want to be able to easily login and logout of an account so I can access my personal account information|[x]|
|As a site user I want to be able to recover my password so that I can still login even if I have forgotten my details|[x]|
|As a site user I want to recive an email confirmation after I have registered for an account so that I can verify my account was created successfully|[x]|
|As a site user I want to have a personalised profile so that I can view my previous orders and order confirmations|[x]|
|As a site user I want to be able to save my payment information so that I can checkout quicker next time I visit the site|[x]|
|||
|As a shopper I want to view a list of products so that I can choose items to purchase|[x]|
|As a shopper I want to view individual product details so that I can see the product description, price, and rating|[x]|
|As a shopper I want to identify deals easily so that I can take advantage of savings on products that I would like to purchase|[x]|
|As a shopper I want to see my purchase total at all times so I can keep track of how much I am going to spend|[x]|
|As a shopper I want to be able to sort the list of available products so that I can easily find the products with the best rating and best price|[x]|
|As a shopper I want to be able to sort for a specific category of product so that I can look for products with the best price and best rating in that category|[x]|
|As a shopper I want to be able to sort by price or rating within a specific category so that I can find products easily|[x]|
|As a shopper I want to search for a product by name or description so I can find a specific product I would like to purchase|[x]|
|As a shopper I want to see what I have searched for and how many result have been returned so I can quickly see if the product I want to purchase is available|[x]|
|As a shopper I want to be able to select the quantity when purchasing an item so that I can order more then 1 item|[x]|
|As a shopper I want to view the items currently in my bad to summarise my purchases and the cost|[x]|
|As a shopper I want to adjust the quantity of items in my shopping bag so I can easily make changes to my purchases before checkout|[x]|
|As a shopper I want to be able to easily enter in my payment information so I can have a hassel free experience|[x]|
|As a shopper I want to feel that my personal information is safe so that I can confiently provide the information required to make a purchase|[x]|
|As a shopper I want to view and order confirmation after checkout to verify that I haven't made any mistakes|[x]|
|As a shopper I want to recieve and email confirmation after checkout so I can keep the confirmation of the purchase for my records|[x]|
|||
|As a store owner I want to be able to add new items to my store so that I can add newly released products to the store|[x]|
|As a store owner I want to be able to edit/update products in my store so that I can adjust price, descriptions, images and other criteria|[x]|
|As a store owner I want to be able to delete a product so that I can remove items that are no longer in stock or are not for sale|[x]|

## Agile Development Tool
For the agile methodology I used the GitHub canban board, it was here where I created the user stories, first as a draft then progressed the items to issues in the to do column. You can see a snap shot below.

![In progress canban](./media/Canban%20Inprogress.png "Canban")

When I wanted to start working on a feature, I moved the issue from the 'todo' list to the 'in progress' list. Once the task was completed it was moved in to the completed list.

![Completed Canban](./media/Canban%20Board.png "Canban")

The user stories detailed above are aligned with the project goals. Which was to produce a simple, interactive online store where users could find all types of confectionary items. They would have the abilty to select a seemingly infinite combination of sweets and chocolate.

## Models
---

### Order Line Item
| Key | Name | Type |
|:-:|:----------:|:-:|
|FK|Order|CharField|
|FK|Product Name|CharField|
||Quantity|Integer Field|
||Line Item Total|Decimal Field|

### Category
| Key | Name | Type |
|:-:|:----------:|:-:|
||Name|CharField|
||Friendly Name|CharField|

### Products
| Key | Name | Type |
|:-:|:----------:|:-:|
|FK|Category|CharField|
||Name|CharField|
||Description|TextField|
||Price|DecimalField|
||Color|CharField|
||Flavour|CharField|
||Brand|CharField|
||Vegiterian|BooleanField|
||Rating|DecimalField|
||Image|ImageField|

### Review
| Key | Name | Type |
|:-:|:----------:|:-:|
|FK|Product||
|FK|Username||
||name|CharField|
||rating|DecimalField|
||content|TextField|
||created|DateTimeField|
||updated|DateTimeField|
||active|BooleanField|

### Order
| Key | Name | Type |
|:-:|:----------:|:-:|
||Order Number|CharField|
|FK|User Profile||
||Full Name|CharField|
||Email|EmailField|
||Phone Number|CharField|
||Country|CountryField|
||Postcode|CharField|
||Town or City|CharField|
||Street Address 1|CharField|
||Street Address 2|CharField|
||County|CharField|
||Date|DateTimeField|
||Delivery Cost|DecimalField|
||Order Total|DecimalField|
||Grand Total|DecimalField|
||Original Shopping Bag|Text Field|
||Stripe ID|CharField|

### Order Line Item
| Key | Name | Type |
|:-:|:----------:|:-:|
|FK|Order||
|FK|Product||
||Quantity|IntgerField|
||Line Item Total|DecimalField|

### User Profile
| Key | Name | Type |
|:-:|:----------:|:-:|
||user|OneToOneField|
||default_phone_number|CharField|
||default_country|CountryField|
||default_postcode|CharField|
||default_town_or_city|CharField|
||default_street_address1|CharField|
||default_street_address2|CharField|
||default_county|CharField|

### Favourites
| Key | Name | Type |
|:-:|:----------:|:-:|
||products|ManyToMany|
||username|OneToOneField|


## Technologies Used
---

### Languages
---

| Key | Name |
|:-:|:----------:|
|HTML|https://en.wikipedia.org/wiki/HTML5|
|CSS|https://en.wikipedia.org/wiki/CSS|
|Python|https://en.wikipedia.org/wiki/JavaScript|
|JavaScript|https://jquery.com/|
|JQuery|https://en.wikipedia.org/wiki/Python_(programming_language)|
|Markdown|https://en.wikipedia.org/wiki/Markdown|

### Tools, Libaries and Frameworks
---

| Libraries / Frameworks / Tools | Description | Link |
|:-:|:----------:|:-:|
|Django|Database Driven Framework||
|gunicorn|HTTP Interface Server||
|psycopg2|Database adaptor||
|cloudinary|Image management||
|django allauth|User authentication||
|django crispy forms|Styling forms||
|HTML Validation|Validating HTML|w3.org|
|CSS Validation|Validating CSS|w3.org|
|JS Validation|Validating JS & jQuery|jshint|
|PEP8|Validating python|PEP8|
|Site mockup|Mockup of site on different screen sizes|https://techsini.com/multi-mockup/index.php|
|Balsamic|Wireframes|Balsamic|
|Visual Studio Code|IDE||
|Bootstrap|Responsive design||
|Font Awesome|Icons||
|Pillow|Image processing tool||
|generateprivacypolicy.com|Privacy Policy Generator||
|Stripe|online payments||

## Testing
---

Testing is required on all features. All clickable links must be redirected to the correct pages. 
All forms linked to the database must be tested to ensure they post all the correct data.

Full Testing details can be found here [Testing](./TESTING.md)

## Pass Criteria - Checklist
---
| Number | Marking Criteria | Met |
|:-:|:----------|:---:|
|1.1|Implement at least one Django app containing some e-commerce functionality using an online payment processing system (e.g. Stripe). This may be a shopping cart checkout, subscription-based payments or single payments, donations, etc. |[x]|
|1.2|Implement a feedback system that reports successful and unsuccessful purchases to the user, with a helpful message |[x]|
|1.3|Develop and implement a Full-Stack web application built using the Django framework, to incorporate a relational database, an interactive Front-End and multiple apps (an app for each potentially reusable component) |[x]|
|1.4|Implement at least one form, with validation, that allows users to create and edit models in the backend |[x]|
|1.5|Build a Django file structure that is consistent and logical, following the Django conventions. |[x]|
|1.6|Write code that demonstrates characteristics of ‘clean code.’ ||
|1.7|Define application URLs in a consistent manner |[x]|
|1.8|Incorporate a main navigation menu and structured layout ||
|1.9|Demonstrate proficiency in the Python language by including sufficient custom logic in your project ||
|1.10|Write Python code that includes functions with compound statements such as if conditions and loops |[x]|
|1.11|Design a relational database schema with clear relationships between entities |[x]|
|1.12|Create at least THREE original custom Django models. |[x]|
|1.13|All CRUD (create, select/read, update, delete) functionality is implemented. ||
|1.14|Deploy the final version of your code to a hosting platform and test that it matches the development version. |[x]|
|1.15|Ensure that all final deployed code is free of commented out code and has no broken internal links ||
|1.16|Ensure the security of the deployed version, making sure to not include any passwords in the git repository, that all secret keys are hidden in environment variables or in files that are in .gitignore, and that DEBUG mode is turned off |[x]|
|1.17|Use a git-based version control system for the entire application, generating documentation through regular commits and in the project README. |[x]|
|1.18|Create a project README that is well-structured and written using a consistent markdown format |[x]|
|1.19|Document the complete deployment procedure, including the database, and the testing procedure, in a README file that also explains the application’s purpose and the value that it provides to its users |[x]|
|2.1|Design a Front-End for a full stack web application that meets accessibility guidelines, follows the principles of UX design, meets its given purpose and provide a set of user interactions ||
|2.2|Document and implement all User Stories within an Agile tool and map them to the project goals |[x]|
|2.3|Design and implement manual or automated test procedures to assess functionality, usability, responsiveness and data management within the entire web application ||
|2.4|Present a clear rationale for the development of the project in the README, demonstrating that it has a clear, well-defined purpose addressing the needs of and user stories for a particular target audience (or multiple related audiences). |[x]|
|2.5|Document the UX design work undertaken for this project, including any wireframes, mockups, diagrams, etc., created as part of the design process and its reasoning. Include diagrams created as part of the design process and demonstrate that these have been followed through to implementation |[x]|
|2.6|Use an Agile tool to manage the planning and implementation of all primary functionality |[x]|
|2.7|Document and implement all User Stories and map them to the project within an Agile tool |[x]|
|3.1|Ensure that all pages on the site can be reached by a link from another findable page. |[x]|
|3.2|Include Meta Description tags in the application HTML |[x]|
|3.3|Include a site title on the parent template |[x]|
|3.4|When defining the relationship between the current document and a linked document, ensure the following: Use “nofollow” for any paid links and distrusted content. Use “sponsored” for any sponsored or compensated links. |[x]|
|3.5|Include a sitemap on your application to allow search engine bot crawling |[x]|
|3.6|Include a robots.txt file to control search engine bot crawling |[x]|
|3.7|Include a 404 response page with an appropriate redirect for attempted access to non-existent content |[x]|
|3.8|Ensure all text content supports the purpose of the application - no Lorem Ipsum text to be used. |[x]|
|4.1|Implement an authentication mechanism, allowing a user to register and log in, addressing a clear reason as to why the users would need to do so. ||
|4.2|Implement login and registration pages that are only available to anonymous users. |[x]|
|4.3|Implement functionality that prevents non-admin users from accessing the data store directly without going through the code |[x]|
|4.4|Apply role-based login and registration functionality ||
|4.5|Ensure the current login state is reflected to the user |[x]|
|4.6|Users should not be permitted to access restricted content or functionality before role-based login |[x]|
|5.1|Create a Facebook Business Page dedicated to your product |[x]|
|5.2|Add a newsletter signup form to your application. |[x]|
|6.1|Document the e-commerce business model underlying your application |[x]|

## E-Commerce Business Model & Business Page

Facebook : Business Page (https://m.facebook.com/The-Sweet-Shop-111602038303857)

The Sweet Shop Business Model

Our ecommerce business model follows a business-to-business-to-consumer model. 
Everyone loves a sweet treat, and our business aims to provide just that. The Sweet Shop makes satisfying people’s cravings easier than ever. Our business sells wholesale sweets online at an affordable price. We offer a wide range of sweets from old favourites to new flavours. Our website is accessible, easily navigated and provides a quick and simple payment method. 
We aim to be accessible to the mass market and will sell our product via our website with various advertising opportunities including our Facebook page and PPC advertising. 
Below I have included our business model canvas for The Sweet Shop. 

![Business Model](./media/Business_Model.png "Title")

## Newsletter

The newsletter was created using mailchimp

Once the user signs up, for the news letter they show up in the dashboard as can be seen in the example below.

![Newsletter](./media/Mailchimp.png "Newsletter screenshot")

Disclaimer : The address has been blanked out on the image above

## Bugs found

## Deployment to Heroku
---

This project was deployed with Heroku using the following method:

### Requirements and Procfile

Heroku needs to know which technologies are being used and any requirements the project may have. 
The best way to do this is to create a requirements.txt file.

- In the terminal type: 'pip3 freeze --local > requirements.txt' to create your requirements file.
- Create your Procfile and copy the following code: 'web: gunicorn sweet_shop.wsgi:application' Make sure that there is no blank lines at the end of the file
- Add, Commit then Push these files to your repository

### Creating the Heroku Application

- Login to heroku
- Select 'Create New App' from within your dashboard
- Choose a name for your application. Note: This name must be unique
- Select the region best suited to you
- Click 'Create App'

### Connecting to github

- From the dashboard, click the 'Deploy' tab
- Scroll down till you find 'Deployment Method' and choose 'GitHub'
- From the search bar, locate your repository
- When you have found your repository, click 'Connect'

### Environment Variables

- Click the 'Settings' tab at the top of the page
- Locate 'Config Vars' and click 'Reveal Config Vars' (This is essentially your env.py file)
- Enter all variables required
    - SECRET_KEY
    - DATABASE_URL
    - USE_AWS
    - AWS_ACCESS_KEY_ID
    - AWS_SECRET_ACCESS_KEY
    - STRIPE_PUBLIC_KEY
    - STRIPE_SECRET_KEY
    - STRIPE_WEBHOOK_KEY
    - EMAIL_ADDRESS
    - EMAIL_PASSWORD

### Postgres Database

- AWS S3 Buckets
- Past Variable into Heroku Config vars

## Acknowledgements

- Code Institute for the default template
- Code Institute's Boutique Ado project for Stripe payments and guidance
- https://mycolor.space to generate gradient background-image
- Code Institute Tutors, General Steer in the right direction when bugs were found
- Focus Group for testing and feedback
