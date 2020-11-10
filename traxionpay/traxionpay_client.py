import base64
import json
import hmac
import hashlib
import requests

from .utils import (generate_token, is_valid_amount, is_valid_string,
                    is_valid_id, is_length_acceptable)


class TraxionPay():
    """Core object for using TraxionPay's `cash_in` and `cash_out` functionalities.

    :param api_key: A key that can be retrieved from developer's page.

    :param secret_key: A key that is used for generating tokens.
    The key can be retrieved from developer's page.

    """

    def __init__(self, secret_key=None, api_key=None):
        try:
            self.token = generate_token(secret_key=secret_key)
            self.secret_key = secret_key
            self.api_key = api_key
        except:
            raise ValueError('Secret key and API key cannot be null')

    def cash_in(self, merchant_id=None, merchant_ref_no=None, description=None,
                amount=None, merchant_additional_data=None, currency=None,
                billing_email=None, billing_first_name=None, billing_last_name=None,
                billing_middle_name=None, billing_phone=None, billing_mobile=None,
                billing_address=None, billing_address2=None, billing_city=None,
                billing_state=None, billing_zip=None, billing_country=None,
                billing_remark=None, payment_method=None, status_notification_url=None,
                success_page_url=None, failure_page_url=None, cancel_page_url=None,
                pending_page_url=None):
        """Cash In enables merchants to receive money through the application.
            Through this feature, merchants receive payments and store it in their in-app wallet.

            POST `https://devapi.traxionpay.com/payform-link`

            :param merchant_id: [`int`] ID of the merchant that would accept the amount to cash in.

            :param merchant_ref_no: [`str,100`] A unique transaction code that identifies the transaction.

            :param description: [`str,500`] A description that describes the transaction.

            :param amount: [`float|int`] The amount to be cashed-in to an account.

            :param billing_email: [`str|None,200`] Email address of the billing detail.

            :returns URL of PayForm:

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
        if billing_email is not None:
            if is_valid_string(billing_email):
                payform_data['billing_email'] = billing_email
            else:
                raise TypeError('billing_email should be of type str')
        else:
            payform_data['billing_email'] = ''

        # billing first name
        if billing_first_name is not None:
            if is_valid_string(billing_first_name):
                payform_data['billing_first_name'] = billing_first_name
            else:
                raise TypeError('billing_first_name should be of type str')
        else:
            payform_data['billing_first_name'] = ''

        # billing last name
        if billing_last_name is not None:
            if is_valid_string(billing_last_name):
                payform_data['billing_last_name'] = billing_last_name
            else:
                raise TypeError('billing_last_name should be of type str')
        else:
            payform_data['billing_last_name'] = ''

        # billing middle name
        if billing_middle_name is not None:
            if is_valid_string(billing_middle_name):
                payform_data['billing_middle_name'] = billing_middle_name
            else:
                raise TypeError('billing_middle_name should be of type str')
        else:
            payform_data['billing_middle_name'] = ''

        # billing phone
        if billing_phone is not None:
            if is_valid_string(billing_phone):
                payform_data['billing_phone'] = billing_phone
            else:
                raise TypeError('billing_phone should be of type str')
        else:
            payform_data['billing_phone'] = ''

        # billing mobile
        if billing_mobile is not None:
            if is_valid_string(billing_mobile):
                payform_data['billing_mobile'] = billing_mobile
            else:
                raise TypeError('billing_mobile should be of type str')
        else:
            payform_data['billing_mobile'] = ''

        # billing phone
        if billing_address is not None:
            if is_valid_string(billing_address):
                payform_data['billing_address'] = billing_address
            else:
                raise TypeError('billing_address should be of type str')
        else:
            payform_data['billing_address'] = ''

        # billing mobile
        if billing_address2 is not None:
            if is_valid_string(billing_address2):
                payform_data['billing_address2'] = billing_address2
            else:
                raise TypeError('billing_address2 should be of type str')
        else:
            payform_data['billing_address2'] = ''

        # billing phone
        if billing_city is not None:
            if is_valid_string(billing_city):
                payform_data['billing_city'] = billing_city
            else:
                raise TypeError('billing_city should be of type str')
        else:
            payform_data['billing_city'] = ''

        # billing mobile
        if billing_state is not None:
            if is_valid_string(billing_state):
                payform_data['billing_state'] = billing_state
            else:
                raise TypeError('billing_state should be of type str')
        else:
            payform_data['billing_state'] = ''

        # billing zip
        if billing_zip is not None:
            if is_valid_string(billing_zip):
                payform_data['billing_zip'] = billing_zip
            else:
                raise TypeError('billing_zip should be of type str')
        else:
            payform_data['billing_zip'] = ''

        # billing phone
        if billing_country is not None:
            if is_valid_string(billing_country):
                payform_data['billing_country'] = billing_country
            else:
                raise TypeError('billing_country should be of type str')
        else:
            payform_data['billing_country'] = ''

        # billing mobile
        if billing_remark is not None:
            if is_valid_string(billing_remark):
                payform_data['billing_remark'] = billing_mobile
            else:
                raise TypeError('billing_remark should be of type str')
        else:
            payform_data['billing_remark'] = ''

        # billing phone
        if payment_method is not None:
            if is_valid_string(payment_method):
                payform_data['payment_method'] = payment_method
            else:
                raise TypeError('payment_method should be of type str')
        else:
            payform_data['payment_method'] = ''

        # billing mobile
        if status_notification_url is not None:
            if is_valid_string(status_notification_url):
                payform_data['status_notification_url'] = status_notification_url
            else:
                raise TypeError('status_notification_url should be of type str')
        else:
            payform_data['status_notification_url'] = ''

        # billing phone
        if success_page_url is not None:
            if is_valid_string(success_page_url):
                payform_data['success_page_url'] = success_page_url
            else:
                raise TypeError('success_page_url should be of type str')
        else:
            payform_data['success_page_url'] = ''

        # billing mobile
        if failure_page_url is not None:
            if is_valid_string(failure_page_url):
                payform_data['failure_page_url'] = failure_page_url
            else:
                raise TypeError('failure_page_url should be of type str')
        else:
            payform_data['failure_page_url'] = ''

        # billing phone
        if cancel_page_url is not None:
            if is_valid_string(cancel_page_url):
                payform_data['cancel_page_url'] = cancel_page_url
            else:
                raise TypeError('cancel_page_url should be of type str')
        else:
            payform_data['cancel_page_url'] = ''

        # billing mobile
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

        response = requests.post(url='https://devapi.traxionpay.com/payform-link', data=payload)
        return response.url
