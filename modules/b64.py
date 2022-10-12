import base64
import ast

def decode(b64_str):
    byte_str = base64.b64decode(b64_str)
    dict_str = byte_str.decode("UTF-8")
    dict_str = dict_str.replace(":null", ":None")
    return ast.literal_eval(dict_str)

def encode(plain_text):
    message_bytes = plain_text.encode('ascii')
    base64_bytes = base64.b64encode(message_bytes)
    base64_message = base64_bytes.decode('ascii')
    return base64_message