from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from datetime import datetime, timedelta
import hashlib
import hmac

# Configuration
JAZZCASH_MERCHANT_ID = "<JAZZCASH_MERCHANT_ID>"
JAZZCASH_PASSWORD = "<JAZZCASH_PASSWORD>"
JAZZCASH_RETURN_URL = "<JAZZCASH_RETURN_URL>"
JAZZCASH_INTEGRITY_SALT = "<JAZZCASH_INTEGRITY_SALT>"

def checkout(request):
    #product_id = request.GET.get('product_id')

    product_name = "Product Name"
    product_price = 100

    pp_Amount = int(product_price)

    # Get the current date and time
    current_datetime = datetime.now()
    pp_TxnDateTime = current_datetime.strftime('%Y%m%d%H%M%S')

    # Create expiry date and time by adding one hour to the current date and time
    expiry_datetime = current_datetime + timedelta(hours=1)
    pp_TxnExpiryDateTime = expiry_datetime.strftime('%Y%m%d%H%M%S')

    pp_TxnRefNo = 'T' + pp_TxnDateTime

    post_data = {
        "pp_Version": "1.0",
        "pp_TxnType": "",
        "pp_Language": "EN",
        "pp_MerchantID": JAZZCASH_MERCHANT_ID,
        "pp_SubMerchantID": "",
        "pp_Password": JAZZCASH_PASSWORD,
        "pp_BankID": "TBANK",
        "pp_ProductID": "RETL",
        "pp_TxnRefNo": pp_TxnRefNo,
        "pp_Amount": pp_Amount,
        "pp_TxnCurrency": "PKR",
        "pp_TxnDateTime": pp_TxnDateTime,
        "pp_BillReference": "billRef",
        "pp_Description": "Description of transaction",
        "pp_TxnExpiryDateTime": pp_TxnExpiryDateTime,
        "pp_ReturnURL": JAZZCASH_RETURN_URL,
        "pp_SecureHash": "",
        "ppmpf_1": "1",
        "ppmpf_2": "2",
        "ppmpf_3": "3",
        "ppmpf_4": "4",
        "ppmpf_5": "5"
    }

    sorted_string = '&'.join(f"{key}={value}" for key, value in sorted(post_data.items()) if value != "")
    pp_SecureHash = hmac.new(
        JAZZCASH_INTEGRITY_SALT.encode(),
        sorted_string.encode(),
        hashlib.sha256
    ).hexdigest()
    post_data['pp_SecureHash'] = pp_SecureHash

    return render(request, 'index.html', {'product_name': product_name, 'product_price': product_price, 'post_data': post_data})

@csrf_exempt
def success(request):
    return render(request, 'success.html')
