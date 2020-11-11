"""Test module for traxionpay python sdk"""
import unittest
import base64
import json

from txnpay import TraxionPay


class TestTraxionPay(unittest.TestCase):
    """Unit tests for TraxionPay Python SDK"""
    def setUp(self):
        # usable keys from documentation
        self.secret_key = "cxl+hwc%97h6+4#lx1au*ut=ml+=!fx85w94iuf*06=rf383xs"
        self.api_key = "7)5dmcfy^dp*9bdrcfcm$k-n=p7b!x(t)_f^i8mxl@v_+rno*x"

        self.merchant_id = 6328
        self.merchant_ref_no = "ABC123DEF456"
        self.amount = 1500.0
        self.description = "My test payment"
        self.additional_data = base64.b64encode(json.dumps({ "payment_code": self.merchant_ref_no }).encode()).decode('ascii')
        self.site_url = "https://dev.traxionpay.com/"
        self.notif_url = "https://devapi.traxionpay.com/callback"

        self.api = TraxionPay(secret_key=self.secret_key, api_key=self.api_key)


    def test_init(self):
        """Test to see if an error is raised if secret_key is missing"""
        with self.assertRaises(ValueError):
            TraxionPay(api_key=self.api_key)


    def test_cash_in(self):
        """Test to see if some fields are missing in `cash_in` method"""
        # Raise value error when merchant_id is missing
        with self.assertRaises(ValueError):
            self.api.cash_in(merchant_ref_no=self.merchant_ref_no,
                             description=self.description,
                             amount=self.amount)

        # Raise value error when merchant_ref_no is missing
        with self.assertRaises(ValueError):
            self.api.cash_in(merchant_id=self.merchant_id,
                             description=self.description,
                             amount=self.amount)

        # Raise value error merchant_ref_no has more than 100 characters
        merchant_ref_no = "s"*105 # 105 characters
        with self.assertRaises(ValueError):
            self.api.cash_in(merchant_id=self.merchant_id,
                             merchant_ref_no=merchant_ref_no,
                             description=self.description,
                             amount=self.amount)

        # Raise value error when description is missing
        with self.assertRaises(ValueError):
            self.api.cash_in(merchant_id=self.merchant_id,
                             merchant_ref_no=self.merchant_ref_no,
                             amount=self.amount)

        # Raise value error description has more than 500 characters
        description = "str"*200 # 600 characters
        with self.assertRaises(ValueError):
            self.api.cash_in(merchant_id=self.merchant_id,
                             merchant_ref_no=self.merchant_ref_no,
                             description=description,
                             amount=self.amount)

        # Raise value error when amount is missing
        with self.assertRaises(ValueError):
            self.api.cash_in(merchant_id=self.merchant_id,
                             merchant_ref_no=self.merchant_ref_no,
                             description=self.description)

        # Raise type error when merchant_id is not an integer
        merchant_id = "6328"
        with self.assertRaises(TypeError):
            self.api.cash_in(merchant_id=merchant_id,
                             merchant_ref_no=self.merchant_ref_no,
                             description=self.description,
                             amount=self.amount)

        # Raise type error when merchant_ref_no is not a string
        merchant_ref_no = 1234567
        with self.assertRaises(TypeError):
            self.api.cash_in(merchant_id=self.merchant_id,
                             merchant_ref_no=merchant_ref_no,
                             description=self.description,
                             amount=self.amount)

        # Raise type error when description is not a string
        description = 1234567
        with self.assertRaises(TypeError):
            self.api.cash_in(merchant_id=self.merchant_id,
                             merchant_ref_no=self.merchant_ref_no,
                             description=description,
                             amount=self.amount)

        # Raise type error when amount is not a float
        amount = "1500"
        with self.assertRaises(TypeError):
            self.api.cash_in(merchant_id=self.merchant_id,
                             merchant_ref_no=self.merchant_ref_no,
                             description=description,
                             amount=amount)

        # cash in successful
        cash_in_response = self.api.cash_in(merchant_id=self.merchant_id,
                                            merchant_ref_no=self.merchant_ref_no,
                                            merchant_additional_data=self.additional_data,
                                            description=self.description,
                                            amount=self.amount,
                                            status_notification_url=self.notif_url,
                                            success_page_url=self.site_url,
                                            failure_page_url=self.site_url,
                                            cancel_page_url=self.site_url,
                                            pending_page_url=self.site_url)

        self.assertIsNotNone(cash_in_response)


    def test_fetch_banks_length(self):
        """Test to see if `fetch_banks` returns bank"""
        banks = self.api.fetch_banks()
        bank = banks[0]

        self.assertGreater(len(banks), 0)
        self.assertIn('id', bank)
        self.assertIn('code', bank)
        self.assertIn('name', bank)


    def test_fetch_bank_accounts(self):
        """Test to see if `fetch_bank_accounts returns bank accounts"""
        bank_accounts = self.api.fetch_bank_accounts()
        self.assertGreater(len(bank_accounts), 0)

    
    def test_fetch_otp(self):
        """Test to see if `fetch_otp` returns an otp"""
        otp = self.api.fetch_otp()
        self.assertIn('code', otp)


    def test_cash_out(self):
        """Test to see if some fields are missing in `cash_out` method"""
        otp = self.api.fetch_otp()
        code = otp['code']
        bank_accounts = self.api.fetch_bank_accounts()
        bank_account = bank_accounts[0]['id']

        # amount is missing
        with self.assertRaises(ValueError):
            self.api.cash_out(otp=code, bank_account=bank_account)

        # bank_account is missing
        with self.assertRaises(ValueError):
            self.api.cash_out(otp=code, amount=self.amount)

        # otp is missing
        with self.assertRaises(ValueError):
            self.api.cash_out(bank_account=bank_account, amount=self.amount)

        # otp is not type string
        with self.assertRaises(TypeError):
            self.api.cash_out(otp=otp, bank_account=bank_account, amount=self.amount)

        # otp is not type float
        amount = "100"
        with self.assertRaises(TypeError):
            self.api.cash_out(otp=otp, bank_account=bank_account, amount=amount)

        # bank_account is not type int
        bank_account_id = "364"
        with self.assertRaises(TypeError):
            self.api.cash_out(otp=otp, bank_account=bank_account_id, amount=amount)

        cash_out_response = self.api.cash_out(otp=code,
                                              bank_account=bank_account,
                                              amount=self.amount)

        # cash_out successful
        self.assertIn('ref_no', cash_out_response)
        self.assertIn('transaction_id', cash_out_response)
        self.assertIn('remittance_id', cash_out_response)
