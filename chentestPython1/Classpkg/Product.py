'''
Created on Jun 28, 2017

@author: chenz
'''

class Product:
    def __init__(self):
        print ('init done')
    
    def GetPrice(self,price):
        return 100 + int(price)
    
    def GetSize(self,size):
        return 50 + int(size)
    
    def GetDescription(self,des):
        return des