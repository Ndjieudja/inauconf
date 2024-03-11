
# --*-- encodng: utf8 --*--
# !/usr/bin/env python3
##############################################################################
#
#    Simple Solution, Open Source Security package
#    Copyright (C) 2023 (<https://gabrielhack.pythonanywhere/start>).
#    Gabriel Ndjieudja < ssolutionets@gmail.com | gabrielndjieudja@gmail.com >
#
##############################################################################

from inauconf.crypt import EncryptAll
import hashlib, os, stat, warnings

class UnCryptFile(EncryptAll):

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
            _file_name_checksum = "{0}.checksum".format(_name)
            
            # Set file permissions
            os.chmod(_file_name_inc, stat.S_IRWXU)
            os.chmod(_file_name_checksum, stat.S_IRWXU)


            # Check if the file is already decrypted
            if not file_name.endswith(".inc"):
                print("File is not encrypted.")
                return

            with open(file_name, 'r') as file:
                read_crypted_file = file.read()
                
                            
            # Capturing of hash-passphrase
            index = read_crypted_file.index("$")
            
            hiden_hash_password = read_crypted_file[index+1 : index + 65]
            
            get_hash_password = "".join(hiden_hash_password)
        
            if hash_passphrase == get_hash_password:
                print(' \n ================== Successuf verify passwaord =================')
                extension = read_crypted_file[:index].strip('[]')

                # Remove obfuscation value( extension, and hash password)
                retrieving_obfuscation = read_crypted_file.replace(read_crypted_file[:index+65], "")
                
                # Decrypt the file contents
                decrypted_content = self.decrypt(retrieving_obfuscation)

                # Get hash value for comparaison before unluck it
                with open(_file_name_checksum, 'r') as file:
                    hash_value_for_verification = file.read()
                
                # Verify hash of the decrypted content
                decrypted_hash = hashlib.sha256(decrypted_content.encode()).hexdigest()
                                
                if decrypted_hash != hash_value_for_verification:
                    print("Hash verification failed. File may have been tampered with.")
                    return

                # Write decrypted content to the original file
                original_file_name = f"{_name}{extension}"
                with open(original_file_name, 'w') as original_file:
                    original_file.write(decrypted_content)

                # Remove the encrypted file
                os.remove(_file_name_inc)
                os.remove(_file_name_checksum)
                
                return True
                
            else:
                return False

        except Exception as error:
            print(error)
            
            
if __name__ == "__main__":
    warnings.warn("use 'python -m inauconf', not 'python -m inauconf.crypt'", DeprecationWarning)