'''
Created on May 24, 2017

@author: chenz
'''

def addonemore(input):
    return input +1 

list1 = {1,2,3,4,5}
listresp = list(map(addonemore, list1))
print (listresp)


#turn a string to char
a = "Hello world!"
listresp = list(map(list, a))
listff =[]
print (listresp)
for charersp in listresp:
     for charfinnal in charersp:
         listff.append(charfinnal)
print (listff)
        

 