# TraxionPay Python SDK

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)

## Installation
```sh
pip install txnpay
```

## Usage

#### Initialize
After installing, initialize by importing the package and using the public and secret keys.
```python
from txnpay import Traxionpay

traxionpay = TraxionPay(api_key=your_api_key, secret_key=your_secret_key)
```
#### Cash in
```python
# Sample arguments are the bare minimum for cash_in
response = traxionpay.cash_in(merchant_id=6328,
                              merchant_ref_no="ABC123DEF",
                              merchant_additional_data="eyJwYXltZW50X2NvZGUiOiAiQUJDMTIzREVGNDU2IA=",
                              description="My payment",
                              amount=100.0,
                              status_notification_url="https://www.mysite.com/callback",
                              success_page_url="https://www.mysite.com/success",
                              failure_page_url="https://www.mysite.com/failed",
                              cancel_page_url="https://www.mysite.com/cancelled",
                              pending_page_url="https://www.mysite.com/pending")
```
#### Cash out
```python
response = traxionpay.cash_out(otp="AB12DE34", bank_account=413, amount=100.0)
```
