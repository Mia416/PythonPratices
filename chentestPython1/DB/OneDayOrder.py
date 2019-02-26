'''
Created on Jun 14, 2017

@author: chenz

DB select return is turle type
'''
import cx_Oracle
import xml.etree.cElementTree as ET
 
from xml.etree.ElementTree import Element, SubElement, tostring, XML
import time
from _overlapped import NULL

order = []
order_id =[]
order_cost =[]
order_history =[]


 
    
def createcostxml(order):
      
     root = Element('opc')
     root.set('version', '1.0')
     root.set('count',str(len(order)))
     root.set('date',time.strftime("%Y%m%d"))     
     for i in order:     
            
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
     tree.write(name)


def createxml(order):
     #order =['3123','dsadas','vdgfd','dfsdfdsf']
     root = Element('opc')
     root.set('version', '1.0')
     root.set('count',str(len(order)))
     root.set('date',time.strftime("%Y%m%d"))
     #head = SubElement(root, 'Order')
     for i in order:     
            
         head = SubElement(root, 'Order')  
         head.text = str(i[1])         
         root.extend(head) 
            
         order_id = SubElement(head, 'order_id')
         order_id.text = str(i[0])
         root.extend(order_id)
         
         order_external_id = SubElement(head, 'EXTERNAL_ORDER_ID')
         order_external_id.text = str(i[1])         
         root.extend(order_external_id)
         
         SERVICE_DISPLAY_NAME = SubElement(head, 'SERVICE_DISPLAY_NAME')
         SERVICE_DISPLAY_NAME.text = str(i[2])         
         root.extend(SERVICE_DISPLAY_NAME)
         
         SERVICE_TYPE = SubElement(head, 'SERVICE_TYPE')
         SERVICE_TYPE.text = str(i[3])         
         root.extend(SERVICE_TYPE)
         
         SYSTEM_NAME = SubElement(head, 'SYSTEM_NAME')
         SYSTEM_NAME.text = str(i[4])         
         root.extend(SYSTEM_NAME)
         
         DATA_CENTER_ID = SubElement(head, 'DATA_CENTER_ID')
         DATA_CENTER_ID.text = str(i[7])         
         root.extend(DATA_CENTER_ID)
         
         OPERATION_TYPE = SubElement(head, 'OPERATION_TYPE')
         OPERATION_TYPE.text = str(i[8])         
         root.extend(OPERATION_TYPE)
         
         ORDER_STATUS = SubElement(head, 'ORDER_STATUS')
         ORDER_STATUS.text = str(i[9])         
         root.extend(ORDER_STATUS)
         
         SUBSCRIPTION_TYPE = SubElement(head, 'SUBSCRIPTION_TYPE')
         SUBSCRIPTION_TYPE.text = str(i[10])         
         root.extend(SUBSCRIPTION_TYPE)
         
         SUBSCRIPTION_ID = SubElement(head, 'SUBSCRIPTION_ID')
         SUBSCRIPTION_ID.text = str(i[11])         
         root.extend(SUBSCRIPTION_ID)
         
         CREATED_ON = SubElement(head, 'CREATED_ON')
         CREATED_ON.text = i[5].strftime("%d/%m/%y %H:%M")       
         root.extend(CREATED_ON)
         
         COMPLETION_DATE = SubElement(head, 'COMPLETION_DATE')
         try:          
            COMPLETION_DATE.text = i[6].strftime("%d/%m/%y %H:%M")    
         except Exception as e:
            COMPLETION_DATE.text = '';
         finally:   
            root.extend(COMPLETION_DATE)      
                  
         Cost_Time = SubElement(head, 'Cost_Time')       
         try:               
             Cost_Time.text = str(((i[6]-i[5]).seconds/60))             
         except Exception as e:
            Cost_Time.text = '';
         finally:   
            root.extend(Cost_Time)
         
     tree = ET.ElementTree(root)
     name  = time.strftime("%Y%m%d")+'.xml'
     tree.write(name)
 

def createDitForComplete():
    
    sql = "select order_id,EXTERNAL_ORDER_ID,SERVICE_DISPLAY_NAME,SERVICE_TYPE,SYSTEM_NAME,TO_TIMESTAMP(CREATED_ON),TO_TIMESTAMP(COMPLETION_DATE),DATA_CENTER_ID,OPERATION_TYPE,ORDER_STATUS,SUBSCRIPTION_TYPE,SUBSCRIPTION_ID  from tas_orders_v  where  CREATED_ON > TO_TIMESTAMP ('2017-6-14 02:00:00.000000', 'YYYY-MM-DD HH24:MI:SS.FF')  and CREATED_ON < TO_TIMESTAMP ('2017-6-15 02:00:00.000000', 'YYYY-MM-DD HH24:MI:SS.FF') and COMPLETION_DATE is not null" 
    con = cx_Oracle.connect('tas/welcome1@slcm19-scan1.us.oracle.com:1521/qagainfc')
    cur = con.cursor()
    cur.execute(sql)
    for result in cur:         
         order_cost.append(result)         
    cur.close()
    con.close()  
     
     
def createDit():
    #and rownum < 3
    sql = "select order_id,EXTERNAL_ORDER_ID,SERVICE_DISPLAY_NAME,SERVICE_TYPE,SYSTEM_NAME,TO_TIMESTAMP(CREATED_ON),TO_TIMESTAMP(COMPLETION_DATE),DATA_CENTER_ID,OPERATION_TYPE,ORDER_STATUS,SUBSCRIPTION_TYPE,SUBSCRIPTION_ID  from tas_orders_v  where  CREATED_ON > TO_TIMESTAMP ('2017-6-14 02:00:00.000000', 'YYYY-MM-DD HH24:MI:SS.FF')  and CREATED_ON < TO_TIMESTAMP ('2017-6-15 02:00:00.000000', 'YYYY-MM-DD HH24:MI:SS.FF') " 
    con = cx_Oracle.connect('tas/welcome1@slcm19-scan1.us.oracle.com:1521/qagainfc')
    cur = con.cursor()
    cur.execute(sql)
    for result in cur:
         order_id.append(result[0])
         order.append(result)         
    cur.close()
    con.close() 

def queryHistory(id):  
         sql = "select * from TAS_ORDER_HISTORY where ID= :id"                  
         con = cx_Oracle.connect('tas/welcome1@slcm19-scan1.us.oracle.com:1521/qagainfc')
         cur = con.cursor()         
         cur.execute(sql,id=id)         
         for result in cur:
             #print (result)
             order_history.append(result)         
         cur.close()
         con.close() 
    



createDit()
createxml(order)

for i in order:
    if (i[6] is not None ):
        order_cost.append(i)
    

#createDitForComplete()
createcostxml(order_cost)
print ('done')
'''
createDit()
for i in order:
    print(i)    
createxml(order)
'''
#for i in order_id:  
    #queryHistory(i)
#for i in order:
    #print(i)
#for i in order_history:
    #print(i)
    
    