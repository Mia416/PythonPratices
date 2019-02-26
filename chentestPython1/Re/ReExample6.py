'''
Created on Jun 1, 2017

@author: chenz
'aaa.bbb.ccc.com' to 'www.example.com'

print re.sub(r'(^auth_redirect_url\s*=\s*)([^/]*)(.*)',
                 r'\g<1>{}\g<3>'.format(host), url)
'''

import re 

urls = [
    'auth_redirect_url = aaa.bbb.ccc.com/auth-web',
    'auth_redirect_url = aaa.bbb.ccc.com'
]

for url in urls:
    resp =  re.sub(r'(auth_redirect_url\s*=\s*) \w+.\w+.\w+.com',r'\g<1>www.example.com',url)
    print (resp)