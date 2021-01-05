"""Utils for traxionpay client"""

import json
import base64
import sys

PY2 = sys.version_info[0] == 2
PY3 = sys.version_info[0] == 3

def generate_token(secret_key=None):
    """Generates token based on secret_key"""
    if secret_key is not None:
        token = base64.b64encode(secret_key.encode()).decode('utf-8')
    else:
        raise ValueError("Secret key cannot be None.")
    return token

def encode_additional_data(additional_data):
    """Encodes additional_data object"""
    if isinstance(additional_data, dict):
        return base64.b64encode(json.dumps(additional_data).encode()).decode('utf-8')
    raise ValueError("additional_data must be of type dict")

def is_valid_amount(var):
    """Checks if amount is float or integer"""
    return isinstance(var, (float, int))

def is_valid_id(var):
    """Checks if id is integer"""
    return isinstance(var, int)

def is_valid_bank_type(bank_type):
    """Checks if bank_type is 'savings' or 'checkings'"""
    return bank_type in ('savings', 'checkings')

def is_length_acceptable(var, length):
    """Checks if input length is valid"""
    return len(var) <= length

def is_additional_data_valid(encoded_additional_data):
    """Checks if additional_data is encoded in base64"""
    try:
        decoded = base64.decode(encoded_additional_data)
        encoded = base64.b64encode(decoded).decode('utf-8')
        return encoded == encode_additional_data
    except Exception:
        return False

if PY3:
    def is_valid_string(var):
        """Checks if string is valid"""
        return isinstance(var, str)

elif PY2:
    def is_valid_string(var):
        return isinstance(var, basestring)

else:
    def is_valid_string(var):
        raise SystemError("unsupported version of python detected (supported versions: 2, 3)")
