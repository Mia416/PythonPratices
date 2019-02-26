'''
Created on May 23, 2017

@author: chenz
A dictionary is an example of a key value store also known as Mapping in Python. It allows you to store and retrieve elements by referencing a key. 
As dictionaries are referenced by key, they have very fast lookups. As they are primarily used for referencing items by key, they are not sorted.
'''

def printformat(inputstring):
    print("=====:%s======"%inputstring) 
    print("\n") 


d = {'a': 1, 'b': 2, 'c':3}

printformat('list all element by default')
print (d)


printformat('list all element')
for key in d:
    print(key, d[key])
    
#print one element by id
printformat('show element by id')
print(d['b'])

#add one element
d['aaa'] = 888
d['sdfg'] = '888'
printformat('add one element ')
print(d)


#delete one element by id
del d['aaa']
del d['sdfg']
printformat('delete one element ')
print(d)


#list dictionary keys 
res = list(d.keys())
printformat('list dictionary keys  ')
print(res)

#sort dictionary keys 
res = sorted(d.values()) 
printformat('sort dictionary values  ')
print(res)

#check whether a key is in the dictionary

res = 'a' in d
res1 = 'aa' not in d
printformat('check whether a in the dictionary ')
print(res)
print(res1)


#merge two list into one dictionary
l1 = {1,2,3,4,5}
l2 = {'a','b','c','d','e'}
d = dict(zip(l1,l2))
printformat('merge list to dictionary')
print(d)

d1 = {}
for l1_ in l1:
    for l2_ in l2:
        d1[l1_] = l2_
        l2.remove(l2_)
        break
printformat('merge list to dictionary withour zip')        
print (d1)


