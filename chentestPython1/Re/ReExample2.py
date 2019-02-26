'''
Created on Jun 1, 2017

@author: chenz
'''


#replace file content
import re

#replace ab using &&
with open("test1.txt",'r+') as e:
    text = e.read()
    text = str(text)
    print (text)
    resp = re.sub(r'a\w*','$$',text)
    print (resp)
    e.write(resp)
   
e.close()

with open('test1.txt','r') as e1:
    print (e1.read())

e1.close()
