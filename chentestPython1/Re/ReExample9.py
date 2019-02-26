'''
Created on Jun 2, 2017

@author: chenz

change word upper or lower
'''

import re

text="verified, vERIFIED, VERIFIED"
text=re.sub(r'verified', 'Verified', text, flags=re.IGNORECASE)
print (text)