'''
Created on Jun 2, 2017

@author: chenz

aaaaaaaa;aa;aaa;aaa;aaaaaaaaaa;


to 

aaaaaaa,aa,aaa,aaa,aaaaaaaaaa,



GCGGG

to

GCGAA
'''

import re

x='aaaaaaaa;aa;aaa;aaa;aaaaaaaaaa;'
x=re.sub(r';',r'.',x)
print (x)


test ='GCGGG'
#resp = re.sub(r'(\w+)GG',r'\1AA',test)
resp=re.sub(r"(?<=[GAT])G", "A", test)
print (resp)

