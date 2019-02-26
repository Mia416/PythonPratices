'''
Created on Jun 12, 2017

@author: chenz
'''
i = iter('abcd')


for i in iter(i):
    print(i)
    
 

s = {'one':1,'two':2,'three':3}
for i in iter(s):
    print(i)