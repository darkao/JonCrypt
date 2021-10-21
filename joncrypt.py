"""
  Author: darkao
  Date: 05.08.2021
  v2 Update: 20.08.2021

TR

  Bu modül, herhangi bir dosyayı/dosyaları şifrelemek içindir. Fernet AES-128 algoritmasını kullanmaktadır. Kullanımından dolayı doğacabilecek olan zarardan geliştirici sorumlu tutlamaz. Eğitim amaçlıdır.

  Kullanım:
    - python joncrypt.py -e 'şifrelemek için' ya da -d 'deşifrelemek için' [dosya_yolu] -p [şifre]

    *** Şifreliyici anahtarı lütfen not alınız aksi takdirde dosyalarınıza bir daha erişemeyebilirsiniz.
"""

"""
ENG

   This module is for encrypting any file/files. It uses the fernet AES-128 algorithm. The developer cannot be held responsible for any damage that may arise from its use. Education purpose only.

   Usage:
     - python joncrypt.py -e 'for encryption' or -d 'for decryption' [file_destination] -p [password]

     *** Please take a note of the encryption password, otherwise you may not be able to access your files again.
"""

from cryptography.fernet import Fernet
import base64, hashlib, os, argparse

def encrypt(filename, key):
    extension = ".jcrypt"
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
            os.rename(filename, filename+ extension)
            print("its done! "+ filename + " was successfuly encrypted.")
    except Exception as e:
        print(e)
        quit()

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
            os.rename(filename, os.path.splitext(filename)[0])
            print("its done! "+ filename + " was successfuly decrypted.")
    except Exception as e:
        print(e)
        quit()



def banner():
    print("""
      _              ____                  _   
     | | ___  _ __  / ___|_ __ _   _ _ __ | |_ 
  _  | |/ _ \| '_ \| |   | '__| | | | '_ \| __|
 | |_| | (_) | | | | |___| |  | |_| | |_) | |_ 
  \___/ \___/|_| |_|\____|_|   \__, | .__/ \__|
                               |___/|_|        v2


                               Author: https://github.com/darkao/
    """)

def main():

  banner()
  parser = argparse.ArgumentParser()

  parser.add_argument("--encrypt","-e", help="For encryption file or folder")
  parser.add_argument("--decrypt","-d", help="For decryption file or folder")
  parser.add_argument("--password","-p", help="Encrytion key.")

  data = parser.parse_args()

  if(data.encrypt and data.password):
    m_key = data.password.encode()
    key = hashlib.md5(m_key).hexdigest()
    key_64 = base64.urlsafe_b64encode(key.encode("utf-8"))
    if os.path.isdir(data.encrypt):
      directory = os.listdir(data.encrypt)
      os.chdir(data.encrypt)
      for file in directory:
          encrypt(file, key_64)

    else:
      encrypt(data.encrypt, key_64)

    print("Password is: " + data.password)

  elif (data.decrypt and data.password):
    m_key = data.password.encode()
    key = hashlib.md5(m_key).hexdigest()
    key_64 = base64.urlsafe_b64encode(key.encode("utf-8"))
    if os.path.isdir(data.decrypt):
      directory = os.listdir(data.decrypt)
      os.chdir(data.decrypt)
      for file in directory:
        decrypt(file, key_64)
    else:
      decrypt(data.decrypt, key_64)
  else:
    print("""
    Usage: joncrypt.py [Option] [file]
    """)

if __name__ == "__main__":
    main()
