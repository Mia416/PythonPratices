'''
Created on Jun 26, 2017

@author: chenz
'''
class Example1:
    def __init__(self,age,name):
         print('init')
         self.age = age
         self.name = name
    
    
    def test1(self):
        return 'this is method 1 return'
    
    

class Example2:
    def __init__(self,account):
        self.ac = account
    
    def testAC(self,account):
        return self.ac + account

e = Example1(100,'2')
mess = e.test1()
print (mess)
print (e.age)

c = Example2(1000)
mess1 = c.testAC(900)
print(mess1)

summary = int(e.age) + int(mess1) 
print (summary)


 



 