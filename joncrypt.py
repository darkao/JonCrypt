"""
  Author: darkao
  Date: 05.08.2021

TR

  Bu modül, herhangi bir dosyayı şifrelemek içindir. Fernet AES-128 algoritmasını kullanmaktadır. Kullanımından dolayı doğacabilecek olan zarardan geliştirici sorumlu tutulamaz. Eğitim amaçlıdır.

  Kullanım:
    - python joncrpyt.py -e 'şifrelemek için' ya da -d 'deşifrelemek için' -f [dosya_yolu] -k [anahtar]

    *** Şifreliyici anahtarı lütfen not alınız aksi takdirde dosyanıza bir daha erişemeyebilirsiniz.
"""

"""
ENG

   This module is for encrypting any file. It uses the fernet AES-128 algorithm. The developer cannot be held responsible for any damage that may arise from its use. Education purpose only.

   Usage:
     - python joncrpyt.py -e 'for encryption' or -d 'for decryption' -f [file_destination] -k [key]

     *** Please make a note of the encryption key, otherwise you may not be able to access your file again.
"""

from cryptography.fernet import Fernet
import base64, hashlib, os, argparse


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
            os.rename(filename, filename+ ".jcrypt")
            print("its done! "+ filename + " was successfuly encrypted.")
    except:
        print("Error!")

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
    except:
        print ("Error!")



def banner():
    print("""
      _              ____                  _   
     | | ___  _ __  / ___|_ __ _   _ _ __ | |_ 
  _  | |/ _ \| '_ \| |   | '__| | | | '_ \| __|
 | |_| | (_) | | | | |___| |  | |_| | |_) | |_ 
  \___/ \___/|_| |_|\____|_|   \__, | .__/ \__|
                               |___/|_|        


                               Author: https://github.com/darkao/
    """)

def main():

  banner()
  parser = argparse.ArgumentParser()

  parser.add_argument("--encrypt","-e", nargs='?',const='arg_was_not_given', help="For encryption")
  parser.add_argument("--decrypt","-d", nargs='?',const='arg_was_not_given',help="For decryption")
  parser.add_argument("--file", "-f", help="Select a file.")
  parser.add_argument("--key","-k", help="Encrytion key.")

  data = parser.parse_args()

  if(data.file):

    if not os.path.isfile(data.file):
      print("No such file was found.")

    else:

      if(data.encrypt and data.file and data.key):
        m_key = data.key.encode()
        key = hashlib.md5(m_key).hexdigest()
        key_64 = base64.urlsafe_b64encode(key.encode("utf-8"))
        encrypt(data.file, key_64)
        print("Key is: " + data.key)

      elif (data.decrypt and data.file and data.key):
        m_key = data.key.encode()
        key = hashlib.md5(m_key).hexdigest()
        key_64 = base64.urlsafe_b64encode(key.encode("utf-8"))
        decrypt(data.file, key_64)


if __name__ == "__main__":
    main()
