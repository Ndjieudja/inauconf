# --*-- coding:utf8 --*--

import sys
sys.path.insert(0, './src/inauconf/')
sys.path.insert(0, './')

from crypt import EncriptAll

e = EncriptAll()

word = "ndjieudja Gabriel"
print('''
    function cript(data)
        input entry: ''' + word )

hiden = e.encript(word)
print("""\n
    hidden values: """
     + hiden)

show  = e.decript(hiden)
print(''''\n 
    function show hidden 
        show hidden: ''' + show)

try:
    with open("LICENCE", "r") as file:
        read = file.read()
        print(e.encript(read))
        
        print(e.decript(e.encript(read)))
        
except Exception as error:
    print(error)
    
    