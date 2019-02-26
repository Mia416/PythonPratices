'''
Created on Jun 27, 2017

@author: chenz
'''
import unittest

from unittest.mock import  MagicMock,Mock 

class TestCla1:        
    def count(self,num1,num2):
        return num1 + num2   
 


class mocktest(unittest.TestCase):
    
 
    def testvalue1(self):
        e = TestCla1()
        e.count = Mock(return_value =10000)
        result = e.count(100,1000)
        print (result)
    
 
    
    def testvalue2(self):
        f = TestCla1
        f.count = MagicMock(return_value =30000)
        result = f.count(100,1000)
        print (result)
        
 
             
 

a = TestCla1()
print ('========real test=========')
print (a.count(10,20))
print ('==========================')

print ('=======mock test==========')
a = mocktest()
a.testvalue1()
print ('==========================')

print ('=======mock test2==========')
a = mocktest()
a.testvalue2()
print ('==========================') 

