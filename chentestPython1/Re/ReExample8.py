'''
Created on Jun 2, 2017

@author: chenz


a bunch of random text here.
to
<verse osisID="lol">a bunch of random text here.</verse>

'''

import re 

test = 'a bunch of random text here.'
resp = re.sub(r'(.*)',r'<verse osisID="lol">\1</verse>',test)
print (resp)

