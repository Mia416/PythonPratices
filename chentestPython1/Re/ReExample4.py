'''
Created on Jun 1, 2017

@author: chenz



How can I replace 'foobar' to 'foo123bar'?
'''

import re 

test = 'foobar'
resp = re.sub(r'foo',r'foo123',test)
print (resp)


'''
<cross_sell id="123" sell_type="456"> --> <cross_sell>

'''

test = '<cross_sell id="123" sell_type="456">'
resp = re.sub(r'\w+="\w+"' ,r'',test)

#resp=re.sub(r'(\w+)[^>]+',r'\1',test)
print (resp)