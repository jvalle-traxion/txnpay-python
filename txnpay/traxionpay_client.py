"""
traxionpay module containing cash in and cash out functions
"""
import base64
import json
import hmac
import hashlib
import requests

from .constants import BASE_URL
from .exceptions import MissingAuthenticationError, APIResponseError
from .utils import (generate_token,
                    is_valid_amount,
                    is_valid_string,
                    is_valid_id,
                    is_valid_bank_type,
                    is_length_acceptable)


class TraxionPay():
    """Core object for using TraxionPay's `cash_in` and `cash_out` functionalities.

        :param api_key:

        :param secret_key:

        See full documentation at <https://dev.traxionpay.com/developers-guide>.
    """

    def __init__(self, secret_key=None, api_key=None):
        try:
            self.secret_key = secret_key
            self.api_key = api_key
            self.token = generate_token(secret_key=secret_key)
            self.auth_headers = {
                'Authorization': 'Basic {}'.format(self.token),
                'Content-Type': 'application/json'
            }
        except:
            raise ValueError('Secret key and API key cannot be null')

    def cash_in(self,
                merchant_id=None,
                merchant_ref_no=None,
                description=None,
                amount=None,
                currency=None,
                merchant_additional_data=None,
                payment_method=None,
                status_notification_url=None,
                success_page_url=None,
                failure_page_url=None,
                cancel_page_url=None,
                pending_page_url=None,
                **billing_details):
        """Cash In enables merchants to receive money through the application.
            Through this feature, merchants receive payments and store it in their in-app wallet.

            POST `https://devapi.traxionpay.com/payform-link`

            :param merchant_id:

            :param merchant_ref_no:

            :param description:

            :param amount:

            :param currency: (optional, defaults to PHP if None)

            :param merchant_additional_data:

            :param payment_method: (optional)

            :param status_notification_url:

            :param success_page_url:
            
            :param failure_page_url:

            :param cancel_page_url:
            
            :param pending_page_url:

            :billing_details: (optional)
        """
        payform_data = {}

        # merchant ID
        if merchant_id is not None:
            if is_valid_id(merchant_id):
                payform_data['merchant_id'] = merchant_id
            else:
                raise TypeError('merchant_id should be of type int')
        else:
            raise ValueError('merchant_id cannot be None')

        # merchant reference number
        if merchant_ref_no is not None:
            if is_valid_string(merchant_ref_no):
                length = 100
                if is_length_acceptable(merchant_ref_no, length):
                    payform_data['merchant_ref_no'] = merchant_ref_no
                else:
                    raise ValueError(
                        'merchant_ref_no must be less than or equal to {}'.format(length))
            else:
                raise TypeError('merchant_ref_no should be of type str')
        else:
            raise ValueError('merchant_ref_no cannot be None')

        # payment description
        if description is not None:
            if is_valid_string(description):
                length = 500
                if is_length_acceptable(description, length):
                    payform_data['description'] = description
                else:
                    raise ValueError('description must be less than or equal to {}'.format(length))
            else:
                raise TypeError('description should be of type str')
        else:
            raise ValueError('description cannot be None')

        # total amount
        if amount is not None:
            if is_valid_amount(amount):
                payform_data['amount'] = amount
            else:
                raise TypeError('amount should be of type float')
        else:
            raise ValueError('amount cannot be None')

        # additional merchant data
        if merchant_additional_data is not None:
            if is_valid_string(merchant_additional_data):
                payform_data['merchant_additional_data'] = merchant_additional_data
            else:
                raise TypeError('merchant_additional_data should be of type str')
        else:
            payform_data['merchant_additional_data'] = ''

        # currency
        if currency is not None:
            if is_valid_string(currency):
                payform_data['currency'] = currency
            else:
                raise TypeError('currency should be of type str')
        else:
            payform_data['currency'] = 'PHP'

        # billing email
        billing_email = billing_details.get('billing_email')
        if billing_email is not None:
            if is_valid_string(billing_email):
                payform_data['billing_email'] = billing_email
            else:
                raise TypeError('billing_email should be of type str')
        else:
            payform_data['billing_email'] = ''

        # billing first name
        billing_first_name = billing_details.get('billing_first_name')
        if billing_first_name is not None:
            if is_valid_string(billing_first_name):
                payform_data['billing_first_name'] = billing_first_name
            else:
                raise TypeError('billing_first_name should be of type str')
        else:
            payform_data['billing_first_name'] = ''

        # billing last name
        billing_last_name = billing_details.get('billing_last_name')
        if billing_last_name is not None:
            if is_valid_string(billing_last_name):
                payform_data['billing_last_name'] = billing_last_name
            else:
                raise TypeError('billing_last_name should be of type str')
        else:
            payform_data['billing_last_name'] = ''

        # billing middle name
        billing_middle_name = billing_details.get('billing_middle_name')
        if billing_middle_name is not None:
            if is_valid_string(billing_middle_name):
                payform_data['billing_middle_name'] = billing_middle_name
            else:
                raise TypeError('billing_middle_name should be of type str')
        else:
            payform_data['billing_middle_name'] = ''

        # billing phone
        billing_phone = billing_details.get('billing_phone')
        if billing_phone is not None:
            if is_valid_string(billing_phone):
                payform_data['billing_phone'] = billing_phone
            else:
                raise TypeError('billing_phone should be of type str')
        else:
            payform_data['billing_phone'] = ''

        # billing mobile
        billing_mobile = billing_details.get('billing_mobile')
        if billing_mobile is not None:
            if is_valid_string(billing_mobile):
                payform_data['billing_mobile'] = billing_mobile
            else:
                raise TypeError('billing_mobile should be of type str')
        else:
            payform_data['billing_mobile'] = ''

        # billing address
        billing_address = billing_details.get('billing_address')
        if billing_address is not None:
            if is_valid_string(billing_address):
                payform_data['billing_address'] = billing_address
            else:
                raise TypeError('billing_address should be of type str')
        else:
            payform_data['billing_address'] = ''

        # billing address2
        billing_address2 = billing_details.get('billing_address2')
        if billing_address2 is not None:
            if is_valid_string(billing_address2):
                payform_data['billing_address2'] = billing_address2
            else:
                raise TypeError('billing_address2 should be of type str')
        else:
            payform_data['billing_address2'] = ''

        # billing city
        billing_city = billing_details.get('billing_city')
        if billing_city is not None:
            if is_valid_string(billing_city):
                payform_data['billing_city'] = billing_city
            else:
                raise TypeError('billing_city should be of type str')
        else:
            payform_data['billing_city'] = ''

        # billing state
        billing_state = billing_details.get('billing_state')
        if billing_state is not None:
            if is_valid_string(billing_state):
                payform_data['billing_state'] = billing_state
            else:
                raise TypeError('billing_state should be of type str')
        else:
            payform_data['billing_state'] = ''

        # billing zip
        billing_zip = billing_details.get('billing_zip')
        if billing_zip is not None:
            if is_valid_string(billing_zip):
                payform_data['billing_zip'] = billing_zip
            else:
                raise TypeError('billing_zip should be of type str')
        else:
            payform_data['billing_zip'] = ''

        # billing country
        billing_country = billing_details.get('billing_country')
        if billing_country is not None:
            if is_valid_string(billing_country):
                payform_data['billing_country'] = billing_country
            else:
                raise TypeError('billing_country should be of type str')
        else:
            payform_data['billing_country'] = 'PH'

        # billing remark
        billing_remark = billing_details.get('billing_remark')
        if billing_remark is not None:
            if is_valid_string(billing_remark):
                payform_data['billing_remark'] = billing_mobile
            else:
                raise TypeError('billing_remark should be of type str')
        else:
            payform_data['billing_remark'] = ''

        # payment method
        if payment_method is not None:
            if is_valid_string(payment_method):
                payform_data['payment_method'] = payment_method
            else:
                raise TypeError('payment_method should be of type str')
        else:
            payform_data['payment_method'] = ''

        # status notification url
        if status_notification_url is not None:
            if is_valid_string(status_notification_url):
                payform_data['status_notification_url'] = status_notification_url
            else:
                raise TypeError('status_notification_url should be of type str')
        else:
            payform_data['status_notification_url'] = ''

        # url when successful
        if success_page_url is not None:
            if is_valid_string(success_page_url):
                payform_data['success_page_url'] = success_page_url
            else:
                raise TypeError('success_page_url should be of type str')
        else:
            payform_data['success_page_url'] = ''

        # url when failed
        if failure_page_url is not None:
            if is_valid_string(failure_page_url):
                payform_data['failure_page_url'] = failure_page_url
            else:
                raise TypeError('failure_page_url should be of type str')
        else:
            payform_data['failure_page_url'] = ''

        # url when cancelled
        if cancel_page_url is not None:
            if is_valid_string(cancel_page_url):
                payform_data['cancel_page_url'] = cancel_page_url
            else:
                raise TypeError('cancel_page_url should be of type str')
        else:
            payform_data['cancel_page_url'] = ''

        # url when pending
        if pending_page_url is not None:
            if is_valid_string(pending_page_url):
                payform_data['pending_page_url'] = pending_page_url
            else:
                raise TypeError('pending_page_url should be of type str')
        else:
            payform_data['pending_page_url'] = ''

        data_to_hash = '{}{}{}{}'.format(merchant_ref_no, amount, 'PHP', description)

        secure_hash = hmac.new(self.secret_key.encode(),
                               data_to_hash.encode(),
                               hashlib.sha256).hexdigest()

        auth_hash = hmac.new(self.secret_key.encode(),
                             self.api_key.encode(),
                             hashlib.sha256).hexdigest()
        alg = "HS256"

        payform_data['secure_hash'] = secure_hash
        payform_data['auth_hash'] = auth_hash
        payform_data['alg'] = alg

        # send cash_in request
        encoded_payform_data = base64.b64encode(json.dumps(payform_data).encode()).decode('utf-8')
        payload = {'form_data': encoded_payform_data}

        response = requests.post(url='{}/payform-link'.format(BASE_URL), data=payload)

        if not response.ok:
            raise APIResponseError(response.text)
        return response.url


    def fetch_banks(self):
        """Retrieves list of banks.

        GET `https://devapi.traxionpay.com/banks/`
        """
        response = requests.get(url='{}/banks/'.format(BASE_URL))

        if not response.ok:
            raise APIResponseError(response.text)
        return response.json()


    def fetch_bank_accounts(self):
        """Retrieves list of usable bank accounts.

        GET `https://devapi.traxionpay.com/payout/bank-account/`
        """
        try:
            response = requests.get(url='{}/payout/bank-account/'.format(BASE_URL),
                                    headers=self.auth_headers)
        except AttributeError:
            raise MissingAuthenticationError()

        if not response.ok:
            raise APIResponseError(response.text)
        return response.json()


    def link_bank_account(self, bank_code=None, bank_type=None,
                          account_number=None, account_name=None):
        """Links or creates a new bank account.

        POST `https://devapi.traxionpay.com/payout/bank-account/`

        :param bank_code:

        :param bank_type:

        :param account_number:

        :param account_name:
        """

        payload = {}

        # otp
        if bank_code is not None:
            if is_valid_string(bank_code):
                payload['bank'] = bank_code
            else:
                raise TypeError('bank_code must be of type str')
        else:
            raise ValueError('bank_code cannot be None')

        # bank type
        if bank_type is not None:
            if is_valid_string(bank_type):
                if is_valid_bank_type(bank_type):
                    payload['bank_type'] = bank_type
                else:
                    raise ValueError('bank_type must either be "checkings" or "savings"')
            else:
                raise TypeError('bank_type must be of type str')
        else:
            raise ValueError('bank_type cannot be None')

        # account number
        if account_number is not None:
            if is_valid_string(account_number):
                payload['account_number'] = account_number
            else:
                raise TypeError('account_number must be of type str')
        else:
            raise ValueError('account_number cannot be None')

        # account name
        if account_name is not None:
            if is_valid_string(account_name):
                length = 50
                if is_length_acceptable(account_name, length):
                    payload['account_name'] = account_name
                else:
                    raise ValueError('account_name must be less than or equal to {}'.format(length))
            else:
                raise TypeError('account_name must be of type str')
        else:
            raise ValueError('account_name cannot be None')

        try:
            response = requests.post(url='{}/payout/bank-account/'.format(BASE_URL),
                                     headers=self.auth_headers,
                                     json=payload)
        except AttributeError:
            raise MissingAuthenticationError()

        if not response.ok:
            raise APIResponseError(response.text)
        return response.json()


    def fetch_otp(self):
        """Retrieves otp for `cash_out` method.

        POST `https://devapi.traxionpay.com/bank-payout/get-otp/`
        """
        try:
            response = requests.post(url='{}/payout/bank-payout/get-otp/'.format(BASE_URL),
                                     headers=self.auth_headers)
        except AttributeError:
            raise MissingAuthenticationError()

        if not response.ok:
            raise APIResponseError(response.text)
        return response.json()


    def cash_out(self, otp=None, amount=None, bank_account=None):
        """The Cash Out feature allows merchants to physically
        retrieve the money stored in the in-app wallet.

        To Cash Out, the merchant links a bank accout,
        provides an OTP, and requests a payout to the bank.

        POST `https://devapi.traxionpay.com/payout/bank-payout/`

        :param otp:

        :param amount:

        :param bank_account:
        """
        payload = {}

        # otp
        if otp is not None:
            if is_valid_string(otp):
                payload['OTP'] = otp
            else:
                raise TypeError('otp must be of type str')
        else:
            raise ValueError('otp cannot be None')

        # amount
        if amount is not None:
            if is_valid_amount(amount):
                payload['amount'] = amount
            else:
                raise TypeError('amount must be of type float')
        else:
            raise ValueError('amount cannot be None')

        # bank account number
        if bank_account is not None:
            if is_valid_id(bank_account):
                payload['bank_account'] = bank_account
            else:
                raise TypeError('bank_account must be of type str')
        else:
            raise ValueError('bank_account cannot be None')

        try:
            response = requests.post(url='{}/payout/bank-payout/'.format(BASE_URL),
                                     headers=self.auth_headers,
                                     json=payload)
        except AttributeError:
            raise MissingAuthenticationError()

        if not response.ok:
            raise APIResponseError(response.text)
        return response.json()
