# Dales Window Washing Website

## Overview

### What is the website for?

- Offer service and communication for a window washing service

### What does it do?

- Allow users to log in to pay account balance, seek help, review company and leave comments

### How does it work?

-  The site is styled with Bootstrap and uses Django to authenticate users, register new users, upload comments to a database for displaying on site

## Features

### Existing Features
- Allow users to log in and save basic information
- Allow users to leave comments on the website for others to see
- Email company with any queries
- Display's company logo and information
- Time indicator on all screens
- stripe billing from logged in account

### Features left to implement

## Tech Used

### Some the tech used includes:

- [Bootstrap](http://getbootstrap.com/)
    - We use **Bootstrap** to give our project a simple, responsive layout
- [Django]
    - We use Django to organize our project and build the account, comments and paypal apps separately.
    - Django framework supplies the database where all customer comments and information is stored
- [Discus]
    - We use discus and TinyMCE for the commenting text areas to offer greater choice of style to customers
- [Paypal]
    - We use Paypal to allow users to pay their bill online in a one off payment
- [Python]
    - We use python to code the backend of the application

## Contributing

### Getting the code up and running
1. Firstly you will need to clone this repository by running the ```git clone <https://github.com/dawatson8001/DalesWindowWashers>``` command
2. Then you will need to install all the dependencies from the requirements files
3. The code comes with sqlite3, if you want to review the database data directly you will need to download and install DB browser for SQLite
4. Setup yourself through the admin APIView so your have an admin user for the site
5. Run the site


