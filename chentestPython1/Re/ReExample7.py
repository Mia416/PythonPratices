'''
Created on Jun 1, 2017

@author: chenz

re.findall(r"([^.]*?apple[^.]*\.)",txt) 
'''

import re 

test = 'This is a warning to inform you that youve reached the following soft resource limit on your Oracle Database Cloud Service (Identity Domain: cntest4444). Access My Services for soft quota breach details.Oracle Database Cloud ServiceResources that have exceeded the quota:DCS_EE_PAAS_GP_OCPU_HOUR :  Soft Limit: 0  Current Usage: 4'
#test = 'fsd bhfg Soft Limit:8'

resp = re.sub(r'^This .+quota:','',test)

data = resp.split(' ',0)
for d in data:
    print (d)
#print (resp.split(' '))
#print(resp)
 
pattern = re.compile(r'^This .+quota')
match = pattern.finditer(test)
for m in match:
    print (m.group(0))
 