import os
# import required module
from cryptography.fernet import Fernet

def key():
    """ with open(r'S:\Project\Python\Password-inator\Mark II\Assets\filekey.key', 'rb') as filekey:
        key = filekey.read()
        return key """
    
    if os.path.exists(r'S:\Project\Python\Password-inator\Mark II\Assets\filekey.key'):
        with open(r'S:\Project\Python\Password-inator\Mark II\Assets\filekey.key', "rb") as filekey:
            key = filekey.read()
            return key
    else:
        with open(r'S:\Project\Python\Password-inator\Mark II\Assets\filekey.key', "wb") as filekey:
            encryptionKey = Fernet.generate_key()
            key = filekey.write(encryptionKey)
            return key