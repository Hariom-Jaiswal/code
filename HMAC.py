import hmac
import hashlib

key = b"secretkey"
message = input("Enter message: ").encode()

hmac_value = hmac.new(key, message, hashlib.sha256).hexdigest()

print("HMAC:", hmac_value)