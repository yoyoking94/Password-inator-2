from Backend import savePassword

def close(root, entryPassword,  saveEntry):
    print()
    savePassword.savePassword(entryPassword, saveEntry)
    root.destroy()
    """ find a way to close only the entry name window """