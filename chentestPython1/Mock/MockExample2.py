'''
Created on Jun 27, 2017

@author: chenz
'''
import unittest
from unittest.mock import  Mock  
import urllib.request
from urllib.request import urlopen


class TestClient(unittest.TestCase):  
      
    def send_request(self,url):
        response = urlopen(url)
        return response.status_code


    def visit_ustack(self):
        return TestClient.send_request('http://www.ustack.com')


    #success_send is mock method 
    def test_success_request(self):                        
        success_send = Mock(return_value='200')
        TestClient.send_request = success_send           
        testclient1 = TestClient()        
        resultstring = testclient1.visit_ustack()
        print (resultstring)
        #self.assertEqual(TestClient.visit_ustack(), '200')
    
    #fail_send is mock method 
    def test_fail_request(self):
        fail_send = Mock(return_value='404')
        TestClient.send_request = fail_send
        testclient1 = TestClient()        
        resultstring = testclient1.visit_ustack()
        print (resultstring)
        #self.assertEqual(TestClient.visit_ustack(), '404')
        
            
    def test_access_request(self):
        mock_access = Mock(name='mock_access')
        mock_access.return_value = '500'
        TestClient.send_request = mock_access
        testclient1 = TestClient()        
        resultstring = testclient1.visit_ustack()
        print (resultstring)
        
    
    def test_list_request(self):
        mock_list = Mock(name='mock_list')
        listresult = {'404','500','405'}
        mock_list.return_value = listresult
        TestClient.send_request = mock_list
        testclient1 = TestClient()        
        resultstring = testclient1.visit_ustack()
        print (resultstring)
 

t1 = TestClient()
t1.test_success_request()
t1.test_fail_request()
t1.test_access_request()
t1.test_list_request()
