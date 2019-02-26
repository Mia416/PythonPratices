'''
Created on Jun 2, 2017

@author: chenz

<place of birth="Stockholm">

to

Stockholm
'''

import re 

test =  '<place of birth="Stockholm">'
resp = re.sub(r'.*="(\w+)">',r'\1',test)
print (resp)
