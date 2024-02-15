import os
import getpass

def savePassword(entryPassword, saveEntry):
    
    username = getpass.getuser()
    path = r'C:\Users\{}\Desktop\password.txt'.format(username)

    entryValue = saveEntry.get()
    entryPassword = entryPassword.get()    
    
    if os.path.exists(path):
        with open(path, "a+") as file:
            file.write("{} = {}\n".format(entryValue, entryPassword))
    else:
        with open(path, "w+") as file:
            file.write("{} = {}\n".format(entryValue, entryPassword))