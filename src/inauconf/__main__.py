# -*- coding: utf-8 -*-
##############################################################################
#
#    Simple Solution, Open Source Security package
#    Copyright (C) 2023 (<https://gabrielhack.pythonanywhere/start>).
#    Gabriel Ndjieudja < ssolutionets@gmail.com | gabrielndjieudja@gmail.com >
#
##############################################################################

from inauconf.crypt import EncryptAll
import argparse

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