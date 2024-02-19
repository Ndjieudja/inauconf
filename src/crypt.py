# --*-- encodng: utf8 --*--
# !/usr/bin/env python3

from random import randrange
import os, stat
import hashlib
import argparse

class EncryptAll:
	def __init__(self):
		"""
            Define differents var to generate CryptData
        """
		self.code_data = None
		self.uncode_data = None
		self.key = "<YOUR_ENCRYPTION_KEY>"

	def encrypt(self, input: str):

		"""
			Function to code text input
		"""
		if type(input) == str:
			key_val = list()
			key = list()
			values = list()

			container = list()
			for value in range(len(input)):
				if ord(input[value]) < 10:
					key_val.append((ord(input[value]), chr(randrange(1, 10))))

				elif ord(input[value]) < 100:
					interline = randrange(10, 100)
					if interline in range(48, 58):
						interline = 71
					key_val.append((ord(input[value]), chr(interline)))

				elif ord(input[value]) < 1000:
					key_val.append((ord(input[value]), chr(randrange(100, 1000))))

				elif ord(input[value]) < 10000:
					key_val.append((ord(input[value]), chr(randrange(1000, 10000))))

				else:
					key_val.append((ord(input[value]), chr(randrange(10000, 1000000))))

			for value in key_val:
				values.append(value[1])
				values.append(value[0])

			string_int = [str(int) for int in values]
			self.code_data = "".join(string_int)

			return self.code_data

		else:
			print("La valeur a entre dois etre de type String")

	def decrypt(self, input: str):

		"""
			Function de uncode data who will code with the same script
		"""
		if type(input) == str:
			key = list()
			keys = list()
			values = list()

			for value in range(len(input)):
				try:
					chr(int((input[value])))

				except:
					key.append(ord(input[value]))

			for value in key:
				if value < 10:
					keys.append(1)

				elif value < 100:
					keys.append(2)

				elif value < 1000:
					keys.append(3)

				elif value < 10000:
					keys.append(4)

				else:
					keys.append(5)

			n = 1
			for key in keys:
				values.append(chr(int(input[n:n + key])))
				n += (key + 1)

			self.uncode_data = "".join(values)

			return self.uncode_data

		else:
			print("La valeur a entre dois etre de type String")

	def get_file_hash(self, content):
		"""Calculates the SHA-256 hash of a file"""
		encoded_string = content.encode('utf-8')

		# Hash the encoded bytes
		hash_object = hashlib.sha256(encoded_string)
		hash_value = hash_object.hexdigest()
		return hash_value

	def crypt_file(self, file_name):
		"""
        	Encrypt file contents
        """
		try:
			# Check if the file is already encrypted
			if file_name.endswith(".inc"):
				print("File is already encrypted.")
				return

			with open(file_name, 'r') as file:
				read = file.read()

			_name, _ext = os.path.splitext(file_name)
			new_name = "{0}.inc".format(_name)
			hash_file_name = "{0}.txt".format(_name)

			# Encrypt the file contents
			encrypted_content = self.encrypt(read)

			# Write encrypted content to the new file
			with open(new_name, 'w') as encrypted_file:
				encrypted_file.write(encrypted_content)

			# Calculate hash of the original file
			hash_value = self.get_file_hash(read)

			# Append hash to the encrypted file
			with open(hash_file_name, 'w') as hash_file:
				hash_file.write(f"{hash_value}")

			# Set file permissions
			os.chmod(new_name, stat.S_ENFMT)
			os.chmod(hash_file_name, stat.S_ENFMT)

			# Remove the original file
			os.remove(file_name)

		except Exception as error:
			print(error)

	def uncrypt_file(self, file_name):
		"""
			Decrypt file contents and restore the original file
		"""
		try:
			# Check if the file is already decrypted
			if not file_name.endswith(".inc"):
				print("File is not encrypted.")
				return

			with open(file_name, 'r') as file:
				lines = file.read()

			_name, _ext = os.path.splitext(file_name)
			original_file_name = "{0}".format(_name)

			hash_file = "{0}.txt".format(_name)
			with open(hash_file, 'r') as file:
				hashvalue = file.read()

			# Decrypt the file contents
			decrypted_content = self.decrypt(lines)

			# Verify hash of the decrypted content
			decrypted_hash = hashlib.sha256(decrypted_content.encode()).hexdigest()
			if decrypted_hash != hashvalue:
				print("Hash verification failed. File may have been tampered with.")
				return

			# Write decrypted content to the original file
			with open(original_file_name, 'w') as original_file:
				original_file.write(decrypted_content)

			# Set file permissions
			os.chmod(original_file_name, stat.S_ENFMT)

			# Remove the encrypted file
			os.remove(file_name)
			os.remove(hash_file)

		except Exception as error:
			print(error)


if __name__ == "__main__":
	parser = argparse.ArgumentParser(description="Encrypt or decrypt a file")
	parser.add_argument("-f", "--file", type=str, help="Specify the file to encrypt or decrypt")
	parser.add_argument("-d", "--decrypt", action="store_true", help="Decrypt the file")
	parser.add_argument("-e", "--encrypt", action="store_true", help="Encrypt the file")
	parser.add_argument("--string", type=str, help="Decrypt a string using the encrypt function")
	args = parser.parse_args()

	encrypt_all = EncryptAll()

	if args.string:
		if args.encrypt:
			encrypted_string = encrypt_all.encrypt(args.string)
			print("Encrypted string:", encrypted_string)
		elif args.decrypt:
			decrypted_string = encrypt_all.decrypt(args.string)
			print("Decrypted string:", decrypted_string)
		else:
			print("Please specify whether to encrypt or decrypt the string using the -e or -d option.")

	elif args.file:
		if args.encrypt:
			encrypt_all.crypt_file(args.file)
			print("File encrypted successfully.")
		elif args.decrypt:
			encrypt_all.uncrypt_file(args.file)
			print("File decrypted and restored successfully.")
		else:
			print("Please specify whether to encrypt or decrypt the file using the -e or -d option.")
	else:
		parser.print_help()