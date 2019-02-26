'''
Created on Jun 1, 2017

@author: chenz

images/:id/size

to

images/<span>:id</span>/size
'''

import re

test = 'images/:id/size'
#resp =  re.sub(r'/:id/','<span>:id</span>',test)
resp =  re.sub(r':\w\w',r'<span>:id</span>',test)
print (resp)


#re.sub(r'(:[a-z]+)', r'<span>\1</span>', method)

