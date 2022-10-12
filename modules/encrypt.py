from Crypto.Cipher import AES
import base64
import binascii

class RijndaelEncryptor(object):
    """
    Encrypts text using Rijndael 128 in CBC mode and using PKCS7 padding
    """

    def __init__(self, k=16):
        self.k = k  # sets block size of 16 for padding, NOT FOR CIPHER

    def _pkcs7decode(self, text):
        """
        Remove PKCS7 padding from text
        """
        val = text[-1]
        if val > self.k:
            raise ValueError('Input is not padded or padding is corrupt')
        l = len(text) - val
        return text[:l].decode(encoding="UTF-8")

    def _pkcs7encode(self, text):
        """
        Add PKCS7 padding to text
        """
        l = len(text)
        val = self.k - (l % self.k)
        return text + bytearray([val] * val).decode(encoding="UTF-8")

    def encrypt(self, text, input_key, input_iv):
        """
        Encrypt method
        Both Keys and IVs need to be 16 characters encoded in base64.
        """
        # Create aes object
        # key = base64.b64decode(input_key)
        # iv = base64.b64decode(input_iv)
        # aes = AES.new(key, AES.MODE_CBC, iv)
        aes = AES.new(input_key, AES.MODE_CBC, input_iv)
        # Pad text and encrypt
        pad_text = self._pkcs7encode(text)
        cipher_text = aes.encrypt(pad_text.encode("utf8"))
        # Encode to base64 and return
        return base64.b64encode(cipher_text)

    def decrypt(self, text, input_key, input_iv):
        """
        Decrypt method
        Both Keys and IVs need to be 16 characters encoded in base64.
        """
        # Create aes object
        # key = base64.b64decode(input_key)
        # iv = base64.b64decode(input_iv)
        aes = AES.new(input_key, AES.MODE_CBC, input_iv)
        # aes = AES.new(key, AES.MODE_CBC, iv)
        # Decode from base64 and decrypt
        decode_text = base64.b64decode(text)
        pad_text = aes.decrypt(decode_text)
        # Unpad text and return
        return self._pkcs7decode(pad_text)