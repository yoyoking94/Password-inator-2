from cryptography.fernet import Fernet
import getpass
## ==== Import backend ==== ##
from Backend import key

def decrypt():
    encryptionKey = key.key()
    
    fernet = Fernet(encryptionKey)

    username = getpass.getuser()
    path = r'C:\Users\{}\Desktop\password.txt'.format(username)
    
    with open(path, 'rb') as enc_file:
        encrypted = enc_file.read()

    decrypted = fernet.decrypt(encrypted)

    with open(path, 'wb') as dec_file:
        dec_file.write(decrypted)
    