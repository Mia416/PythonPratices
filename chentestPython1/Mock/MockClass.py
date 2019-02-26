'''
Created on Jun 30, 2017

@author: chenz
'''
 

import unittest

from unittest.mock import  MagicMock,Mock 
from chentestPython1.Classpkg.Factory import Factory
from chentestPython1.Classpkg.Product import Product


class mocktest(unittest.TestCase):
    def test1(self):
        e = Factory()      
        p = Product()   
        
        #mock here
        mock_inst = Mock(name='mock_p')
        mock_inst.return_value = 'this is mock product'
        e.produceApple = mock_inst
        #
        
        result  = e.produceApple(p)
        print (result)
 
        
        
        
test1  =mocktest()
test1.test1()