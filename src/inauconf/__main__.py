# -*- coding: utf-8 -*-
##############################################################################
#
#    Simple Solution, Open Source Security package
#    Copyright (C) 2023 (<https://gabrielhack.pythonanywhere/start>).
#    Gabriel Ndjieudja < ssolutionets@gmail.com | gabrielndjieudja@gmail.com >
#
##############################################################################

from inauconf import *
import argparse
import os, subprocess
from getpass import getpass

parser = argparse.ArgumentParser(description="Encrypt or decrypt a file")
parser.add_argument("-f", "--file", type=str, help="Specify the file to encrypt or decrypt")
parser.add_argument("-d", "--decrypt", action="store_true", help="Decrypt the file")
parser.add_argument("-e", "--encrypt", action="store_true", help="Encrypt the file")
parser.add_argument("--string", type=str, help="Decrypt a string using the encrypt function")
parser.add_argument("-p", "--path", type=str, help="Crypt or Decrypt all file insid this pwd")
parser.add_argument("-P", "--password", action="store_true", help="Crypt or Decrypt using password")


args = parser.parse_args()
        

encrypt_all = EncryptAll()
get_hash = GetHashValue()

if args.string:
    if args.encrypt:
        if args.password:
            passphrase = getpass()
            get_hash.hidden_hash_value(args.string, passphrase)
            print('crypt with password')
                    
        else:
            encrypted_string = encrypt_all.encrypt(args.string)
            print("Encrypted string:", encrypted_string)
        
    elif args.decrypt:
        decrypted_string = encrypt_all.decrypt(args.string)
        print("Decrypted string:", decrypted_string)
        
    else:
        print("Please specify whether to encrypt or decrypt the string using the -e or -d option.")
        

elif args.file:
    if args.encrypt:
        if args.password:
            passphrase = getpass('password: ')
            get_hash.hidden_hash_value(args.file, passphrase)
                    
        else:
            encrypt_all.crypt_file(args.file)
            print("File encrypted successfully.")
            
    elif args.decrypt:   
        if args.password:
            passphrase = getpass('password: ')
            verify = get_hash.obtain_hidden_value(args.file, passphrase)
            if verify:
                pass
            else:
                print('Incorrect password')
                    
        else:
            encrypt_all.uncrypt_file(args.file)
            print("File decrypted and restored successfully.")
        
    else:
        print("Please specify whether to encrypt or decrypt the file using the -e or -d option.")
        
elif args.path:
    if args.encrypt:
        try:
            file = "output.txt"
            commande = f"find {os.path.abspath(args.path)} -type f > {file}"
            process = subprocess.Popen(commande, shell=True)
            
            process.wait()
            
            with open(file, 'r') as file_read:
                data_path = file_read.read().split('\n')
                for path in data_path:
                    if os.path.isfile(path):
                        encrypt_all.crypt_file(path)
                        if encrypt_all.crypt_file(path) == True:
                            print('========== Successfull crypt all content of {0} ========'.format(path))
                            
            os.remove(file)

        
        except Exception as error:
            print(('Commande execution falled'))
            
    elif args.decrypt:
        try:
            file = "output.txt"
            commande = f"find {os.path.abspath(args.path)} -type f > {file}"
            process = subprocess.Popen(commande, shell=True)
            
            process.wait()
            
            with open(file, 'r') as file_read:
                data_path = file_read.read().split('\n')
                for path in data_path:
                    if os.path.isfile(path):
                        encrypt_all.uncrypt_file(path)
                        if encrypt_all.uncrypt_file(path) == True:
                            print('========== Successfull uncrypt all content of {0} ========'.format(path))
                            
            os.remove(file)


        except Exception as error:
            print('Commande execution falled')
                    
else:
    parser.print_help()