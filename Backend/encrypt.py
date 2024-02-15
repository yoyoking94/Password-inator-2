import getpass
from cryptography.fernet import Fernet
## ==== Import backend ==== ##
from Backend import key

def encrypt():
    encryptionKey = key.key()
    
    fernet = Fernet(encryptionKey)
    
    username = getpass.getuser()
    path = r'C:\Users\{}\Desktop\password.txt'.format(username)
    
    with open(path, 'rb') as file:
        original = file.read()

    encrypted = fernet.encrypt(original)
    
    with open(path, 'wb') as encrypted_file:
        encrypted_file.write(encrypted)