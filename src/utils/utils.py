# utils.py

import hashlib
import hmac
import time
import json

def generate_secret_key(size=16):
    """Generate a secret key of a specified size."""
    return hashlib.sha256(os.urandom(size)).hexdigest()

def generate_timestamp():
    """Generate a Unix timestamp."""
    return int(time.time())

def generate_nonce():
    """Generate a random nonce."""
    return str(os.urandom(16)).encode('hex')

def verify_signature(secret_key, signature, timestamp, nonce):
    """Verify a signature using HMAC."""
    expected_signature = hmac.new(secret_key.encode(), f"{timestamp}{nonce}".encode(), hashlib.sha256).hexdigest()
    return hmac.compare_digest(expected_signature, signature)

def parse_json_payload(payload):
    """Parse a JSON payload."""
    try:
        return json.loads(payload)
    except json.JSONDecodeError:
        return {}