'''
Created on Jun 28, 2017

@author: chenz
'''
import chentestPython1
from chentestPython1.Classpkg.Product import Product


class Factory:
    def __init__(self):
        print ('init execute')
    
    def produceApple(self,Product):  
        des  = Product.GetDescription('this is apple')     
        return des + '   has been produced'
    
    