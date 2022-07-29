# The Sweet Shop - [Live Website](https://the-sweet-shop.herokuapp.com)

https://github.com/DavidHearl/sweet-shop

Multi Device Layout will go here
https://techsini.com/multi-mockup/index.php

## About
---
The Sweet Shop, is your one stop shop to find any popular sweets often found in pick and mixes.
Order anything between 0.1 and 3.0 Kg

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

## Wireframes
---
Wireframes created with Balsamiq. The project was developed from initial wireframes.

Click the links below to see the wireframes for each page.

[Home Page]()

[Products Page]()

[Shopping Bag]()

[Checkout]()

## Models
---

### Order Line Item
| Key | Name | Type |
|:-:|:----------:|:-:|
|FK|Order|CharField|
|FK|Product Name|CharField|
||Quantity|Integer Field|
||Line Item Total|Decimal Field|

## Technologies Used
---

### Languages
---
- HTML
- CSS
- Python
- JavaScript
- JQuery
- Markdown

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

## Pass Criteria
---
| Number | Marking Criteria | Met |
|:-:|:----------|:---:|
| | Section 1  |
|1.1|Implement at least one Django app containing some e-commerce functionality using an online payment processing system (e.g. Stripe). This may be a shopping cart checkout, subscription-based payments or single payments, donations, etc. |[x]|
|1.2|Implement a feedback system that reports successful and unsuccessful purchases to the user, with a helpful message |[x]|
|1.3|Develop and implement a Full-Stack web application built using the Django framework, to incorporate a relational database, an interactive Front-End and multiple apps (an app for each potentially reusable component) |[x]|
|1.4|Implement at least one form, with validation, that allows users to create and edit models in the backend |[x]|
|1.5|Build a Django file structure that is consistent and logical, following the Django conventions. |[x]|
|1.6|Write code that demonstrates characteristics of ‘clean code.’ |[x]|
|1.7|Define application URLs in a consistent manner |[x]|
|1.8|Incorporate a main navigation menu and structured layout |[x]|
|1.9|Demonstrate proficiency in the Python language by including sufficient custom logic in your project |[x]|
|1.10|Write Python code that includes functions with compound statements such as if conditions and loops |[x]|
|1.11|Design a relational database schema with clear relationships between entities |[x]|
|1.12|Create at least THREE original custom Django models. ||
|1.13|All CRUD (create, select/read, update, delete) functionality is implemented. |[x]|
|1.14|Deploy the final version of your code to a hosting platform and test that it matches the development version. ||
|1.15|Ensure that all final deployed code is free of commented out code and has no broken internal links ||
|1.16|Ensure the security of the deployed version, making sure to not include any passwords in the git repository, that all secret keys are hidden in environment variables or in files that are in .gitignore, and that DEBUG mode is turned off ||
|1.17|Use a git-based version control system for the entire application, generating documentation through regular commits and in the project README. |[x]|
|1.18|Create a project README that is well-structured and written using a consistent markdown format |[x]|
|1.19|Document the complete deployment procedure, including the database, and the testing procedure, in a README file that also explains the application’s purpose and the value that it provides to its users |[x]|
| | Section 2  |
|2.1|Design a Front-End for a full stack web application that meets accessibility guidelines, follows the principles of UX design, meets its given purpose and provide a set of user interactions |[x]|
|2.2|Document and implement all User Stories within an Agile tool and map them to the project goals ||
|2.3|Design and implement manual or automated test procedures to assess functionality, usability, responsiveness and data management within the entire web application ||
|2.4|Present a clear rationale for the development of the project in the README, demonstrating that it has a clear, well-defined purpose addressing the needs of and user stories for a particular target audience (or multiple related audiences). ||
|2.5|Document the UX design work undertaken for this project, including any wireframes, mockups, diagrams, etc., created as part of the design process and its reasoning. Include diagrams created as part of the design process and demonstrate that these have been followed through to implementation ||
|2.6|Use an Agile tool to manage the planning and implementation of all primary functionality ||
|2.7|Document and implement all User Stories and map them to the project within an Agile tool ||
| | Section 3  |
|3.1|Ensure that all pages on the site can be reached by a link from another findable page. |[x]|
|3.2|Include Meta Description tags in the application HTML ||
|3.3|Include a site title on the parent template ||
|3.4|When defining the relationship between the current document and a linked document, ensure the following: Use “nofollow” for any paid links and distrusted content. Use “sponsored” for any sponsored or compensated links. ||
|3.5|Include a sitemap on your application to allow search engine bot crawling ||
|3.6|Include a robots.txt file to control search engine bot crawling ||
|3.7|Include a 404 response page with an appropriate redirect for attempted access to non-existent content ||
|3.8|Ensure all text content supports the purpose of the application - no Lorem Ipsum text to be used. |[x]|
| | Section 4  |
|4.1|Implement an authentication mechanism, allowing a user to register and log in, addressing a clear reason as to why the users would need to do so. ||
|4.2|Implement login and registration pages that are only available to anonymous users. ||
|4.3|Implement functionality that prevents non-admin users from accessing the data store directly without going through the code ||
|4.4|Apply role-based login and registration functionality ||
|4.5|Ensure the current login state is reflected to the user ||
|4.6|Users should not be permitted to access restricted content or functionality before role-based login ||
| | Section 5  |
|5.1|Create a Facebook Business Page dedicated to your product ||
|5.2|Add a newsletter signup form to your application. ||
| | Section 6  |
|6.1|Document the e-commerce business model underlying your application ||

## Manual Testing

## Automated Testing

## Responsive Testing

## E-Commerce Business Model & Business Page

## Bugs found

## Deployment

## Acknowledgements

- Code Institute for the default template
- Code Institute's Boutique Ado project for Stripe payments and guidance
- Code Institute Tutors, General Steer in the right direction when bugs were found
- Focus Group for testing and feedback
