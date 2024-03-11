# --*-- encodng: utf8 --*--
# !/usr/bin/env python3
##############################################################################
#
#    Simple Solution, Open Source Security package
#    Copyright (C) 2023 (<https://gabrielhack.pythonanywhere/start>).
#    Gabriel Ndjieudja < ssolutionets@gmail.com | gabrielndjieudja@gmail.com >
#
##############################################################################

import hashlib, warnings
from inauconf.file import CryptFile
from inauconf.file import UnCryptFile

class GetHashValue(CryptFile, UnCryptFile):
    
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

    def _get_file_hash(self, content):
        """Calculates the SHA-256 hash of a file"""
        encoded_string = content.encode('utf-8')

        # Hash the encoded bytes
        hash_object = hashlib.sha256(encoded_string)
        hash_value = hash_object.hexdigest()
        return hash_value
    
    
if __name__ == "__main__":
    warnings.warn("Use 'python -m inauconf', not 'python -m inauconf.crypt'", DeprecationWarning)