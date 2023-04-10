# --*-- coding:utf8 --*--

import sys
sys.path.insert(0, './src/inauconf/')
sys.path.insert(0, './')

from shuffle import EncriptAll

e = EncriptAll()

word = "ndjieudja Gabriel"
print('''
    function cript(data)
        input entry: ''' + word )

hiden = e.cript(word)
print("""\n
    hidden values: """
     + hiden)

show  = e.uncript(hiden)
print(''''\n 
    function show hidden 
        show hidden: ''' + show)

try:
    with open("LICENCE", "r") as file:
        read = file.read()
        print(e.cript(read))
        
        print(e.uncript(e.cript(read)))
        
except Exception as error:
    print(error)
    
    