# --*-- encodng: utf8 --*--
# !/usr/bin/env python3
##############################################################################
#
#    Simple Solution, Open Source Security package
#    Copyright (C) 2023 (<https://gabrielhack.pythonanywhere/start>).
#    Gabriel Ndjieudja < ssolutionets@gmail.com | gabrielndjieudja@gmail.com >
#
##############################################################################

from inauconf.crypt  import EncryptAll
import os, stat, warnings

class CryptFile(EncryptAll):
    
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
            hash_file_name = "{0}.checksum".format(_name)

            # Encrypt the file contents
            encrypted_content = self.encrypt(read)

            # hiden with password
            extension = f"[{_ext}]"
            list_coding_input = list(encrypted_content)
            list_coding_input.insert(0, f"{extension}${passphrase}")
                
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


if __name__ == "__main__":
    warnings.warn("use 'python -m inauconf', not 'python -m inauconf.crypt'", DeprecationWarning)