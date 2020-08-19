import hashlib

def encrypt_text(text):
    encryptor = hashlib.sha512()
    encryptor.update(bytearray(text.encode()))
    hexdigest = encryptor.hexdigest()

    return hexdigest