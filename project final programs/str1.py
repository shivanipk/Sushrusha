'''
Created on 27-Oct-2016

@author: Aishwarya-HP
'''
import re
string='XXXVI'
print(re.search('[a-zA-Z]+',string))

if(any(c.isalpha() for c in string)):
    print("contain")
else:
    print("not")

id=1
id1=str(id)
print(type(id))  


import os
print(os.path.relpath("speechDB"))  


s="hello"+" "+"hi"
print(s)