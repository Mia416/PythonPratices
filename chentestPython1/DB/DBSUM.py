'''
Created on Jul 3, 2017

@author: chenz

database result is tuple , and tuple is immutable, when we use mock data, change to use list instead,. 
'''
import os
from _datetime import datetime

os.chdir("D:\\instantclient_12_2")
import cx_Oracle
import xml.etree.cElementTree as ET 
from xml.etree.ElementTree import Element, SubElement, tostring, XML
import time
import logging
from datetime import date, timedelta
 
import unittest
from unittest.mock import  Mock 

import os
import sys
import platform

class DBSUM:
    
    def __init__(self):
        print ('init DB class')
        
    
    #log = logging.basicConfig(filename='d:\\mylog.log', filemode='a',level=logging.INFO,format='%(levelname)s  %(asctime)s  %(message)s')  
    logging.basicConfig(filename='d:\\mylog.log', filemode='a',level=logging.INFO)    
    order = []
    order_sub =[]
    
    '''
    time1= datetime.now()     
    d = (date.today() - timedelta(1))     
    time2 =datetime.combine(d, datetime.min.time())
    sql_1 = "select order_id,EXTERNAL_ORDER_ID,SERVICE_DISPLAY_NAME,SERVICE_TYPE,SYSTEM_NAME,TO_TIMESTAMP(CREATED_ON),TO_TIMESTAMP(COMPLETION_DATE),DATA_CENTER_ID,OPERATION_TYPE,ORDER_STATUS,SUBSCRIPTION_TYPE,SUBSCRIPTION_ID  from tas_orders_v  where  CREATED_ON > TO_TIMESTAMP(%s,'YYYY-MM-DD HH24:MI:SS.FF') and CREATED_ON <  TO_TIMESTAMP(%s,'YYYY-MM-DD HH24:MI:SS.FF')and COMPLETION_DATE is not null" %(time2, time1)
    '''
    
    sql_query_oneday ='''
    select order_id,EXTERNAL_ORDER_ID,SERVICE_DISPLAY_NAME,SERVICE_TYPE,SYSTEM_NAME,TO_TIMESTAMP(CREATED_ON),TO_TIMESTAMP(COMPLETION_DATE),DATA_CENTER_ID,OPERATION_TYPE,ORDER_STATUS,SUBSCRIPTION_TYPE,SUBSCRIPTION_ID  from tas_orders_v  where  CREATED_ON > TO_TIMESTAMP ('2017-7-16 02:00:00.000000', 'YYYY-MM-DD HH24:MI:SS.FF')  and CREATED_ON < TO_TIMESTAMP ('2017-7-17 02:00:00.000000', 'YYYY-MM-DD HH24:MI:SS.FF') and COMPLETION_DATE is not null
    '''
    sql_connection = 'tas/welcome1@slcm19-scan1.us.oracle.com:1521/qagainfc'   
    
    def getcurrentPath(self):
        cwd = os.getcwd()
        if (platform.system().find('Windows')!=-1):
             cwd = cwd + '\\'
        if (platform.system().find('Linux')!=-1):   
             cwd = cwd + '/'      
        return cwd 
    
    def readmockdata(self):
         print("read file function start\n")
         filename = "D:/mockdata.log"          
         if os.path.isfile(filename):
             f = open(filename,"r")
             t1 = f.readline()
             #print(t1)
         print("read file function end\n")
         return t1  

     
    def  onedaysummary(self):
        try:
            con = cx_Oracle.connect(self.sql_connection)
            cur = con.cursor()             
            cur.execute(self.sql_query_oneday)
            for result in cur:      
                print (result)           
                self.order_sub.append(result)                 
                logging.info(datetime.now()) 
                logging.info(result)                                
                 
        except Exception as e:
             logging.error(str(e))
             raise ValueError(str(e)) 
             
              
        finally:   
            cur.close()
            con.close()   
            return self.order_sub
     
            
    def createcostxml(self,order_inst):  
        try:         
            
            root = Element('opc')
            root.set('version', '1.0')
            root.set('count',str(len(order_inst)))
            root.set('date',time.strftime("%Y%m%d"))     
            for i in order_inst:
                print (i)   
                print (str(i[0]))
                print (str(i[1]))
                print (str(i[2]))      
                head = SubElement(root, 'Order')  
                head.text = str(i[1])         
                root.extend(head)             

                order_external_id = SubElement(head, 'EXTERNAL_ORDER_ID')
                order_external_id.text = str(i[1])         
                root.extend(order_external_id)
         
                SERVICE_DISPLAY_NAME = SubElement(head, 'SERVICE_DISPLAY_NAME')
                SERVICE_DISPLAY_NAME.text = str(i[2])         
                root.extend(SERVICE_DISPLAY_NAME)
         
                SERVICE_TYPE = SubElement(head, 'SERVICE_TYPE')
                SERVICE_TYPE.text = str(i[3])         
                root.extend(SERVICE_TYPE)        

         
                OPERATION_TYPE = SubElement(head, 'OPERATION_TYPE')
                OPERATION_TYPE.text = str(i[8])         
                root.extend(OPERATION_TYPE)
         
                ORDER_STATUS = SubElement(head, 'ORDER_STATUS')
                ORDER_STATUS.text = str(i[9])         
                root.extend(ORDER_STATUS)       
    
                  
                Cost_Time = SubElement(head, 'Cost_Time')       
                try:               
                    Cost_Time.text = str(((i[6]-i[5]).seconds/60))             
                except Exception as e:
                     Cost_Time.text = '';
                finally:   
                      root.extend(Cost_Time)
         
            tree = ET.ElementTree(root)
            name  = time.strftime("%Y%m%d")+'_cost.xml'              
            tree.write('d:\\%s' %name) 
            #print ('done')
        except Exception as e:
            logging.error(str(e))
            raise ValueError(str(e))    
            
     

mocktemp =[]
order = []
order_cost = []
a = DBSUM()
try:
    
    #below code for mock test#
    mocklist = Mock(name='mock_list')  
    mocktemp = a.readmockdata().split(',')  
     
    
     
    #result = ('1000001', 'T100000', '2017', '2016', 'MOCK', 'MOCK', 'MOCK', 'MOCK', 'MOCK', 'MOCK', 'MOCK','MOCK','MOCK')
    order.append(mocktemp)
    mockresult = order   
    print(mockresult)   
    mocklist.return_value = mockresult    
    a.onedaysummary = mocklist
    #####
    
    order = a.onedaysummary()     
    a.createcostxml(order)
    
except Exception as e:     
    print (str(e))    
#print ('done111')            
