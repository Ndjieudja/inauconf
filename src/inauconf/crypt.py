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
import hashlib
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
        
        

if __name__ == "__main__":
    warnings.warn("use 'python -m inauconf', not 'python -m inauconf.crypt'", DeprecationWarning)