# --*-- encodng: utf8 --*--
# !/usr/bin/env python3
##############################################################################
#
#    Simple Solution, Open Source Security package
#    Copyright (C) 2023 (<https://gabrielhack.pythonanywhere/start>).
#    Gabriel Ndjieudja < ssolutionets@gmail.com | gabrielndjieudja@gmail.com >
#
##############################################################################

from random import randrange
import os, stat
import hashlib, re
import warnings


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
            values = list()

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
                try:
                    values.append(chr(int(input[n:n + key])))
                    n += (key + 1)
                except Exception as Error:
                    print(Error)
                    break

            self.uncode_data = "".join(values)

            return self.uncode_data

        else:
            print("La valeur a entre dois etre de type String")

    def _get_file_hash(self, content):
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
                return False

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
            hash_value = self._get_file_hash(read)

            # Append hash to the encrypted file
            with open(hash_file_name, 'w') as hash_file:
                hash_file.write(f"{hash_value}")

            # Set file permissions
            os.chmod(new_name, stat.S_ENFMT)
            os.chmod(hash_file_name, stat.S_ENFMT)

            # Remove the original file
            os.remove(file_name)
            
            return True

        except Exception as error:
            print(error)
            # print("An error occured when trying to crypt file")
            return False
        
    def crypt_file_with_pass(self, file_name, passphrase):
        """
        	Encrypt file contents with password
        """
        try:
            # Check if the file is already encrypted
            if file_name.endswith(".inc"):
                print("File is already encrypted.")
                return False

            with open(file_name, 'r') as file:
                read = file.read()

            _name, _ext = os.path.splitext(file_name)
            new_name = "{0}.inc".format(_name)
            hash_file_name = "{0}.txt".format(_name)

            # Encrypt the file contents
            encrypted_content = self.encrypt(read)

            # hiden with password
            extension = f"[{_ext}]"
            list_coding_input = list(encrypted_content)
            list_coding_input.insert(0, extension)
            
            print(passphrase)
            for i in range(len(passphrase)):
                position = ord(passphrase[i]) + i
                list_coding_input.insert(position, passphrase[i])
                
            encrypted_content_with_pass = "".join(list_coding_input)

            # Write encrypted content to the new file
            with open(new_name, 'w') as encrypted_file:
                encrypted_file.write(encrypted_content_with_pass)

            # Calculate hash of the original file
            hash_value = self._get_file_hash(read)

            # Append hash to the encrypted file
            with open(hash_file_name, 'w') as hash_file:
                hash_file.write(f"{hash_value}")

            # Set file permissions
            os.chmod(new_name, stat.S_ENFMT)
            os.chmod(hash_file_name, stat.S_ENFMT)

            # Remove the original file
            os.remove(file_name)
            
            return True

        except Exception as error:
            print(error)
            # print("An error occured when trying to crypt file")
            return False 

    def uncrypt_file(self, file_name):
        """
			Decrypt file contents and restore the original file
		"""
        try:
            _name, _ext = os.path.splitext(file_name)

            # Remove roots acces to the files
            _file_name_inc = "{0}.inc".format(_name)
            _file_name_txt = "{0}.txt".format(_name)
            # Set file permissions
            os.chmod(_file_name_inc, stat.S_IRWXU)
            os.chmod(_file_name_txt, stat.S_IRWXU)


            # Check if the file is already decrypted
            if not file_name.endswith(".inc"):
                print("File is not encrypted.")
                return

            with open(file_name, 'r') as file:
                lines = file.read()

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

            # Remove the encrypted file
            os.remove(file_name)
            os.remove(hash_file)

        except Exception as error:
            print(error)
            
    def uncrypt_file_with_pass(self, file_name, hash_passphrase):
        """
			Decrypt file contents and restore the original file
		"""
        try:
            _name, _ext = os.path.splitext(file_name)

            # Remove roots acces to the files
            _file_name_inc = "{0}.inc".format(_name)
            _file_name_txt = "{0}.txt".format(_name)
            # Set file permissions
            os.chmod(_file_name_inc, stat.S_IRWXU)
            os.chmod(_file_name_txt, stat.S_IRWXU)


            # Check if the file is already decrypted
            if not file_name.endswith(".inc"):
                print("File is not encrypted.")
                return

            with open(file_name, 'r') as file:
                read_crypted_file = file.read()            
                
            # Capturing of hash-passphrase
            compil = r'\[\.([^]]+)\]'

            # readonly_file_in_list = list(read_crypted_file)
            
            get_has_password = list()
            
            for i in range(len(hash_passphrase)):
                real_position = ord(hash_passphrase[i]) + i
                get_has_password.append(read_crypted_file[real_position])
        
            print(get_has_password, hash_passphrase)
            if hash_passphrase == get_has_password:
                
                extension = re.findall(compil, read_crypted_file)
                read_crypted_file = re.sub(compil, read_crypted_file)

                # Remove obfuscation value( extension, and hash password)
                read_crypted_file_in_list = list(read_crypted_file)
                for x_position in hash_passphrase:
                    index = chr(x_position)
                    del read_crypted_file_in_list[index]
                
                # Decrypt the file contents
                decrypted_content = self.decrypt("".join(read_crypted_file_in_list))

                # Get hash value for comparaison before unluck it
                hash_file = "{0}.txt".format(_name)
                with open(hash_file, 'r') as file:
                    hash_value_for_verification = file.read()
                
                # Verify hash of the decrypted content
                decrypted_hash = hashlib.sha256(decrypted_content.encode()).hexdigest()
                if decrypted_hash != hash_value_for_verification:
                    print("Hash verification failed. File may have been tampered with.")
                    return

                # Write decrypted content to the original file
                original_file_name = f"{_name}.{extension}"
                with open(original_file_name, 'w') as original_file:
                    original_file.write(decrypted_content)

                # Remove the encrypted file
                os.remove(file_name)
                os.remove(hash_file)
                
                return True
                
            else:
                return False

        except Exception as error:
            print(error)
    
    def hidden_hash_value(self, input_: str, password: str):
        """
            function to crypt file with hidden password
        """
        hash_value = self._get_file_hash(password)
        return self.crypt_file_with_pass(input_, hash_value)
    
    def obtain_hidden_value(self, input_: str, password: str):
        """
            function to decrypt file with hidden password
        """
        hash_value_return  = self._get_file_hash(password)
        return self.uncrypt_file_with_pass(input_, hash_value_return)
        
        

if __name__ == "__main__":
    warnings.warn("use 'python -m inauconf', not 'python -m inauconf.crypt'", DeprecationWarning)