# The Jon
from cryptography.fernet import Fernet
import base64, hashlib, os

def decrypt(filename, key):
    try:
        f = Fernet(key)
        with open(filename, "rb") as file:
            # read the encrypted data
            encrypted_data = file.read()
        # decrypt data
        decrypted_data = f.decrypt(encrypted_data)
        with open(filename, "wb") as file:
            file.write(decrypted_data)
            print("its done!")
    except:
        print ("Error!")



def banner ():
    print ("""
     _  ___  _  _   ___  ___ ___ _____   _____ _____ _ 
  _ | |/ _ \| \| | |   \| __/ __| _ \ \ / / _ \_   _| |
 | || | (_) | .` | | |) | _| (__|   /\ V /|  _/ | | |_|
  \__/ \___/|_|\_| |___/|___\___|_|_\ |_| |_|   |_| (_)
                                                       
                                                       for exit press (e)""")

def dec():
  file = input("Filename with extention: ")
  if file in "e":
    print("see u later! chech me from github. https://github.com/darkao")
    exit()
  
  if not os.path.isfile(file):
    print("No such file was found.")
  
  else:


    my_password = input("Key -> ").encode()
    key = hashlib.md5(my_password).hexdigest()
    key_64 = base64.urlsafe_b64encode(key.encode("utf-8"))
        
    decrypt(file, key_64)
    exit()


banner()

while True:
  dec()