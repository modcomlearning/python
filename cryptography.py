# import cryptography
from cryptography.fernet import Fernet

# this function will write key into a file 
# this is for storage since we do not want to keep generating key everytime.
def write_key():
    """
    Generates a key and save it into a file
    """
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

# run below code once then compile
# check on your project folder if a key.key file has been created with a key inside.compile
#write_key()


# this function is for loading the key from the file generated
def load_key():
    """
    Loads the key from the current directory named `key.key`
    """
    return open("key.key", "rb").read()

# so we load the key.
key = load_key()    

# prepare a message to encrypt
message = "some secret message".encode()
# initialize the Fernet class
f = Fernet(key)
# encrypt the message using f above
encrypted = f.encrypt(message)
print(encrypted)


# decrypt the message using the f defined earlier
decrypted_encrypted = f.decrypt(encrypted)
print(decrypted_encrypted)

# You have to use the same key for encrypting and decrypting




