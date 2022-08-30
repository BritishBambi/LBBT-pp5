# Testing and Verifying 

## Test Case 01 - Validate Python Code online using PEP8 Checker

![Screenshot of Python Test Spreadsheet](assets/screenshots/testing/python-validator.PNG "Python Validation")

The Python code was checked using the pep8 validator available at pep8online.com. The code from each file was copied in its entirity and checked for errors. All the files returned no serious issues and the error codes that were given related to line length which could not be altered.

* Screenshots of the validator reports are here:
    * LBBT Folder
        * [asgi.py file](/assets/screenshots/testing/lbbt-asgi.PNG) 
        * [settings.py file](/assets/screenshots/testing/lbbt-settings.PNG) 
        * [urls.py file](/assets/screenshots/testing/lbbt-urls.PNG) 
        * [wsgi.py file](/assets/screenshots/testing/lbbt-wsgi.PNG)
    * Home Folder
        * [urls.py file](/assets/screenshots/testing/home-urls.PNG)
        * [vies.py file](/assets/screenshots/testing/home-views.PNG)
    * Profiles Folder 
        * [admin.py file](/assets/screenshots/testing/profiles-admin.PNG)
        * [forms.py file](/assets/screenshots/testing/profiles-forms.PNG) 
        * [models.py file](/assets/screenshots/testing/profiles-models.PNG) 
        * [urls.py file](/assets/screenshots/testing/profiles-urls.PNG) 
        * [views.py file](/assets/screenshots/testing/profiles-views.PNG)
    * Products Folder 
        * [admin.py file](/assets/screenshots/testing/products-admin.PNG) 
        * [forms.py file](/assets/screenshots/testing/products-forms.PNG)
        * [models.py file](/assets/screenshots/testing/products-models.PNG)
        * [urls.py file](/assets/screenshots/testing/products-urls.PNG))
        * [views.py file](/assets/screenshots/testing/products-views.PNG)
        * [widgets.py file](/assets/screenshots/testing/products-widgets.PNG)
    * Bag Folder
        * [contexts.py file](/assets/screenshots/testing/bag-contexts.PNG)
        * [urls.py file](/assets/screenshots/testing/bag-urls.PNG)
        * [views.py file](/assets/screenshots/testing/bag-views.PNG)
    * Checkout Folder
        * [admin.py file](/assets/screenshots/testing/checkout-admin.PNG)
        * [apps.py](/assets/screenshots/testing/checkout-apps.PNG)
        * [forms.py file](/assets/screenshots/testing/checkout-forms.PNG) 
        * [models.py file](/assets/screenshots/testing/checkout-models.PNG)
        * [signals.py fle](/assets/screenshots/testing/checkout-signals.PNG)
        * [urls.py file](assets/screenshots/testing/checkout-urls.PNG) 
        * [views.py file](/assets/screenshots/testing/checkout-views.PNG)
        * [webhook_handler file](/assets/screenshots/testing/checkout-webhook_handler.PNG)
        * [webhooks file](/assets/screenshots/testing/checkout-webhooks.PNG)


## Test Case 02 - Validate Javascript Online using JSHint

The JavaScript code was checked using the jshint.com validator available at jshint.com. No errors were detected within the files I created.

* Screenshots of the validator reports are here:
    * Javascript
        * [Bag](/assets/screenshots/testing/js-bag.PNG) 
        * [Countryfield](/assets/screenshots/testing/js-countryfield.PNG) 
        * [Products](/assets/screenshots/testing/js-products.PNG) 
        * [Quantity Script](/assets/screenshots/testing/js-quantity-input.PNG)
        * [script.js](/assets/screenshots/testing/js-script.PNG)
        * [Stripe](/assets/screenshots/testing/js-stripe.PNG)

## Test Case 03 - Validate CSS online using W3C CSS Validation

TWhen validating by url it discovers a total of 711 warnings relating to the Mailchimp newsletter imported css and the bootstrap code. When validating by direct input the validator also reports a warning about the imported style sheet - or the google font import, the warning only states that it does not check the imported style sheet in direct input mode and can be ignored.

![Base CSS](/assets/screenshots/testing/css-base.PNG)

![Checkout CSS](/assets/screenshots/testing/css-checkout.PNG)

## Test Case 04 - HTML Testing

Due to the way Django templates include Django template code in them, and extend other templates, it is not possible to copy the code for each page out of the source html files. Therefore, in order to validate the code correctly, I navigated to the site and accessed the rendered html code through the developer tools of the browser I used during development, Opera GX. I then pasted the code into the HTML validator site. Across all the pages I tested I some consistent warnings and errors that were created by the inputed elements such as bootstrap, stripe and mailchimp. So I was unable to modify these, however during this testing process I was able to identify some issues in my html that I was able to correct. There was also the aria-label that was inserted as part of the ImageField  form in the edit products fields. All the warnings/messages shown in the screenshots now are caused by external methods and not code that is part of my base HTML/templates. This was an important process to iron out all of these hidden issues.

* Screenshots of the validator reports are here:
    * HTML
        * [About us](/assets/screenshots/testing/html-aboutus.PNG) 
        * [Bag](/assets/screenshots/testing/html-bag.PNG)
        * [Bag - With Items](/assets/screenshots/testing/html-bag-items.PNG) 
        * [Checkout](/assets/screenshots/testing/html-checkout.PNG) 
        * [Checkout Success](/assets/screenshots/testing/html-checkout-success.PNG)
        * [Home](/assets/screenshots/testing/html-home.PNG)
        * [Products](/assets/screenshots/testing/html-products.PNG)
        * [Products - Add](/assets/screenshots/testing/html-products-add.PNG)
        * [Products - Edit](/assets/screenshots/testing/html-products-edit.PNG)
        * [Products - Details](/assets/screenshots/testing/html-products-details.PNG)
        * [Products - Review](/assets/screenshots/testing/html-products-review.PNG)
        * [Products - Review - Details](/assets/screenshots/testing/html-products-review-details.PNG)
        * [Products - Review - Comment](/assets/screenshots/testing/html-products-review-comment.PNG)
        * [Profile](/assets/screenshots/testing/html-profile.PNG)

### Test Case 04a - Manual Testing - Site Navigation

For the manual testing I first began with the ggeneral site navigation. This includes starting from the home screen and being able to access a number of different areas of the site. As there is only one minor difference between the Unregistered and registered navigation most of the testing has been done Unregistered and I have highlighted the particular differnece. However for the rest of the manual HTML testing, testing both of these cases is necessary due to the amount of differences.

![Site Navigation](/assets/screenshots/testing/04a-navigation.PNG)

### Test Case 04b - Manual Testing - Unregistered Products

For the products page a lot of the interactions are accesible to both registered and unregistered users. However a review may only be posted by a registered user and so an unregistered user will be prompted to sign in if they try to select this option. Otherwise a user can view recipies, add to bag and view the same things as everyone else.

![Unregistered Products](/assets/screenshots/testing/04b-unregisterd-products.PNG)

### Test Case 04c - Manual Testing - Unregistered Orders

As will be highlighted with the Registered test case the key difference when placing an order as an unregistered user is that the payment details and the order will not be saved to a user profile. A checkout success page will still be presented to the user although to find this again the user will have to access the email that was sent to the address they provided on payment.

![Unregistered Orders](/assets/screenshots/testing/04c-unregistered-orders.PNG)

![Unregistered Orders Email](/assets/screenshots/order-email2.PNG)

### Test Case 05a -Manual Testing - Registered Products

The main difference between registered users as highlighted previously comes in the ability to leave a product review and that process has been documented. This prevents more users abusing the system by at least getting them to make an account first where their review and user history can be tracked and moderated if bad activity has been spotted.

![Registered Products](/assets/screenshots/testing/05a-registered-products.PNG)

### Test Case 05b - Manual Testing - Registered Orders

Again the purchase process remains standard across the site for registered and unregistered users however this brings the main benefit of having your details saved. When the user has their information saved either from the checkout for a future order or from the profile page, this will be represented when they go to the checkout. This helps a user to keep all their orders saved in one place and have the details pre entered to save time placing an order.

![Registered Orders](/assets/screenshots/testing/05b-registered-order.PNG)

![Registered Order Email](/assets/screenshots/order-email.PNG)

### Test Case 05c - Manual Testing - Registered profile

While the profile page does not contain that many elements and features it uses allauth templates to render some important account settings and also displays the order details form and the order history if any has been found matching the user profile.

![Registered profile](/assets/screenshots/testing/05c-registered-profile.PNG)

### Test Case 06 - Manual Testing - MailChimp 

It is important to test that when a user email has been entered into the newsletter form that it has properly been added to the mailchimp list. 

![Newsletter Screenshot](/assets/screenshots/marketing-screenshot.PNG)

![MailChimp Screenshot](/assets/screenshots/newsletter-confirmation.PNG)





