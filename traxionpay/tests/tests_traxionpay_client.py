import unittest

from traxionpay_client import TraxionPay


class TestTraxionPay(unittest.TestCase):

	def setUp(self):
		# usable keys from documentation
		self.secret_key = "cxl+hwc%97h6+4#lx1au*ut=ml+=!fx85w94iuf*06=rf383xs"
		self.api_key = "7)5dmcfy^dp*9bdrcfcm$k-n=p7b!x(t)_f^i8mxl@v_+rno*x"

		self.merchant_id = 6328
		self.merchant_ref_no = "ABC123DEF456"
		self.amount = 1500.0
		self.description = "My test payment"
		
		self.api = TraxionPay(secret_key=self.secret_key, api_key=self.api_key)

	def test_init(self):
		with self.assertRaises(ValueError):
			api = TraxionPay(secret_key=self.secret_key)

		with self.assertRaises(ValueError):
			api = TraxionPay(api_key=self.api_key)

	def test_cash_in_value_errors(self):

		# Raise value error when merchant_id is missing
		with self.assertRaises(ValueError):
			self.api.cash_in(
							merchant_ref_no=self.merchant_ref_no,
							description=self.description,
							amount=self.amount)

		# Raise value error when merchant_ref_no is missing
		with self.assertRaises(ValueError):
			self.api.cash_in(
							merchant_id=self.merchant_id,
							description=self.description,
							amount=self.amount)

		# Raise value error merchant_ref_no has more than 100 characters
		merchant_ref_no = "s"*105 # 105 characters
		with self.assertRaises(ValueError):
			self.api.cash_in(
							merchant_id=self.merchant_id,
							merchant_ref_no=merchant_ref_no,
							description=self.description,
							amount=self.amount)
		
		# Raise value error when description is missing
		with self.assertRaises(ValueError):
			self.api.cash_in(
							merchant_id=self.merchant_id,
							merchant_ref_no=self.merchant_ref_no,
							amount=self.amount)

		# Raise value error description has more than 500 characters
		description = "str"*200 # 600 characters
		with self.assertRaises(ValueError):
			self.api.cash_in(
							merchant_id=self.merchant_id,
							merchant_ref_no=self.merchant_ref_no,
							description=description,
							amount=self.amount)

		# Raise value error when amount is missing
		with self.assertRaises(ValueError):
			self.api.cash_in(
							merchant_id=self.merchant_id,
							merchant_ref_no=self.merchant_ref_no,
							description=self.description)
	
	def test_cash_in_type_errors(self):

		# Raise type error when merchant_id is not an integer
		merchant_id = "6328"
		with self.assertRaises(TypeError):
			self.api.cash_in(
							merchant_id=merchant_id,
							merchant_ref_no=self.merchant_ref_no,
							description=self.description,
							amount=self.amount)
		
		# Raise type error when merchant_ref_no is not a string
		merchant_ref_no = 1234567
		with self.assertRaises(TypeError):
			self.api.cash_in(
							merchant_id=self.merchant_id,
							merchant_ref_no=merchant_ref_no,
							description=self.description,
							amount=self.amount)
		
		# Raise type error when description is not a string
		description = 1234567
		with self.assertRaises(TypeError):
			self.api.cash_in(
							merchant_id=self.merchant_id,
							merchant_ref_no=self.merchant_ref_no,
							description=description,
							amount=self.amount)

		# Raise type error when amount is not a float
		amount = "1500"
		with self.assertRaises(TypeError):
			self.api.cash_in(
							merchant_id=self.merchant_id,
							merchant_ref_no=self.merchant_ref_no,
							description=description,
							amount=amount)