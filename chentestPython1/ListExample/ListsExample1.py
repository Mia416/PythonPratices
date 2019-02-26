'''
Created on May 23, 2017

@author: chenz
List comprehensions in Python are concise, syntactic constructs. 
They can be utilized to generate lists from other lists by applying functions to each element in the list.
 The following section explains and demonstrates the use of these expressions
'''

fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
print('=====original Result=====')
print (fruits)
#Return the number of times x appears in the list.
print (fruits.count('apple'))
#Return the index x appears in the list
print (fruits.index('pear'))

#reverse the list
fruits.reverse()
print('=====Reverse Result=====')
for p in fruits:
    print (p);

#append
fruits.append('zhangchen')
print('=====Append Result=====')
for p in fruits:
    print (p);
    
#sort 
fruits.sort()
print('=====Sort Result=====')
for p in fruits:
    print (p);
    
#pop
fruits.pop()
print('=====Pop Result=====')
for p in fruits:
    print (p);
    
    
    
