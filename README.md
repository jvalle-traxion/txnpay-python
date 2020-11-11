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
#### Link a bank account
```python
traxionpay.link_bank_account(bank_code="161311",
                             bank_type="savings",
                             account_number="9012345678",
                             account_name="John Doe")
```
#### Fetch Cash Out OTP
```python
otp = traxionpay.fetch_otp()
```
#### Fetch bank accounts
```python
bank_accounts = traxionpay.fetch_bank_accounts()
```
#### Fetch banks
```python
banks = traxionpay.fetch_banks()
```
