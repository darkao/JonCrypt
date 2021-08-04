"""
  Author: darkao
  Date: 16.05.21

TR

  Bu modül, herhangi bir dosyayı şifrelemek içindir. AES algoritmasını kuulanmaktadır. Kullanımından dolayı doğacabilecek olan zarardan geliştirici sorumlu tutlamaz. Eğitim amaçlıdır.

  Kullanım:
    - Dosyayı çalıştırın - python encrypt.py
    - Şifrelemek istediğiniz dosyanın adını uzatısı ile birlikte yazınız.
    - Dosyanızın şifreleyici anahtarını giriniz.

    *** Şifreliyici anahtarı lütfen not alınız aksi takdirde dosyanıza bir daha erişemeyebilirsiniz.
    *** Oluşturduğunuz key, md5 ile şifrelenmiştir
"""

"""
ENG

   This module is for encrypting any file. It uses the AES algorithm. The developer cannot be held responsible for any damage that may arise from its use. Education purpose only.

   Usage:
     - Run the file - python encrypt.py
     - Type the name of the file you want to encrypt with its extension.
     - Enter the encryption key of your file.

     *** Please make a note of the encryption key, otherwise you may not be able to access your file again.
     *** The key you created is encrypted with md5
"""
from cryptography.fernet import Fernet
import base64, hashlib, os


def encrypt(filename, key):
    try:
        f = Fernet(key)
        with open(filename, "rb") as file:
            # read the encrypted data
            file_data = file.read()
        # encrypt data
        encrypted_data = f.encrypt(file_data)
        # write the encrypted file
        with open(filename, "wb") as file:
            file.write(encrypted_data)
            print("its done!")
    except:
        print("Error!")


def banner():
    print("""
     _  ___  _  _   ___ _  _  ___ _____   _____ _____ 
  _ | |/ _ \| \| | | __| \| |/ __| _ \ \ / / _ \_   _|
 | || | (_) | .` | | _|| .` | (__|   /\ V /|  _/ | |  
  \__/ \___/|_|\_| |___|_|\_|\___|_|_\ |_| |_|   |_|  
                                                      for exit press (e)
    """)

def enc():
  file = input("Filename with extention: ")
  if file in ('e'):
    exit()

  if not os.path.isfile(file):
    print('No such file was found.')
  
  else:
    my_password = input("Key -> ")
    my_key = my_password.encode()
    key = hashlib.md5(my_key).hexdigest()
    key_64 = base64.urlsafe_b64encode(key.encode("utf-8"))

    encrypt(file,key_64)
    print("Please do not forget your password: "+ my_password)
    print("Your key with MD5: "+ key)
    exit()

banner()
while True:
  enc()