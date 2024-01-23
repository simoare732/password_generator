from cryptography.fernet import Fernet

@staticmethod
def genKey():
    """
    A method which generate a key 
    """
    byts = Fernet.generate_key()
    strg = byts.decode("utf-8")
    return strg

@staticmethod
def encryptText(text, key):
    """
    A method which encrypt a text passed as parameter with a key

    Parameters:
    -----------
    text : str
        The text to encrypt
    key : str
        The key with which encrypt the text
    """
    cipher_suite = Fernet(key)
    cipher_text_bytes = cipher_suite.encrypt(text.encode())
    cipher_text = cipher_text_bytes.decode("utf-8")
    return cipher_text

@staticmethod
def decryptText(cipher_text, key):
    """
    A method which decrypt a text passed as parameter with a key

    Parameters:
    -----------
    cypher_text : str
        The text to decrypt
    key : str
        The key with which decrypt the text
    """
    cipher_suite = Fernet(key)
    plain_text = cipher_suite.decrypt(cipher_text).decode()
    return plain_text