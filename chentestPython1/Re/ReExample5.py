'''
Created on Jun 1, 2017

@author: chenz

(...)
Matches whatever regular expression is inside the parentheses, and indicates the start and end of a group; 

[   ]
Used to indicate a set of characters. In a set:
'''
import re 

'''
<cross_sell id="123" sell_type="456"> --> <cross_sell>

'''

test = "abcdef123"
resp = re.sub(r'\w+[A-Za-z](\d+)',r'\1',test)
print (resp)

 