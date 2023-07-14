# Django JazzCash Checkout
Setting up JazzCash Checkout with Python Django.
This repository contains a Django application that demonstrates the integration of the JazzCash payment gateway.

## Prerequisites

Before running the application, make sure you have the following:

- Python installed
- Django framework installed
- JazzCash merchant credentials (Merchant ID, Password, Integrity salt)

## Configuration
Open the views.py file in the jazzcash folder and update the following configuration variables:

```python
JAZZCASH_MERCHANT_ID = "<JAZZCASH_MERCHANT_ID>"
JAZZCASH_PASSWORD = "<JAZZCASH_PASSWORD>"
JAZZCASH_RETURN_URL = "<JAZZCASH_RETURN_URL>"
JAZZCASH_INTEGRITY_SALT = "<JAZZCASH_INTEGRITY_SALT>"
```
Replace <JAZZCASH_MERCHANT_ID>, <JAZZCASH_PASSWORD>, <JAZZCASH_RETURN_URL>, and <JAZZCASH_INTEGRITY_SALT> with your actual JazzCash merchant credentials and desired return URL.

## Usage
Run the Django application:
```shell
python manage.py runserver
```
