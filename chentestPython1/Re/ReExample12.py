'''
Created on Jun 2, 2017

@author: chenz

aeiou

to

a_e_i_o_u
'''


import re 

# [eo]  means e.................o  all match
test = 'aeiou'
resp = re.sub(r'([eo])',r'_\1_',test) 
print(resp)

