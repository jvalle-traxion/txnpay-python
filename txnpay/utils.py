import base64
import sys

PY2 = sys.version_info[0] == 2
PY3 = sys.version_info[0] == 3

def generate_token(secret_key=None):
    if secret_key is not None:
        key = secret_key
        token = base64.b64encode(secret_key.encode()).decode('utf-8')
    else:
        raise ValueError("Secret key cannot be None.")
    return token

def is_valid_amount(var):
    return isinstance(var, (float, int))

def is_valid_id(var):
    return isinstance(var, int)

def is_valid_bank_type(bank_type):
    return bank_type == 'checkings' or bank_type == 'savings'

def is_length_acceptable(var, length):
    return len(var) <= length
    
if PY3:
    def is_valid_string(var):
        return isinstance(var, str)

elif PY2:
    def is_valid_string(var):
        return isinstance(var, basestring)

else:
    def is_valid_string(var):
        raise SystemError("unsupported version of python detected (supported versions: 2, 3)")