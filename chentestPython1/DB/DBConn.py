'''
Created on Jun 13, 2017

@author: chenz
http://www.oracle.com/technetwork/articles/dsl/python-091105.html
'''

import os
os.chdir("D:\\instantclient_12_2")
import cx_Oracle

order = []
order_sub =[]

 
 
def createDit():
    sql = '''
select ORDER_ID from TAS_ORDER_ITEM_HISTORY_  
where CREATED_ON > TO_TIMESTAMP ('2017-6-12 00:00:00.000000', 'YYYY-MM-DD HH24:MI:SS.FF') 
and CREATED_ON < TO_TIMESTAMP ('2017-6-13 02:00:00.000000', 'YYYY-MM-DD HH24:MI:SS.FF')  
and rownum < 3
'''
    con = cx_Oracle.connect('tas/welcome1@slcm19-scan1.us.oracle.com:1521/qagainfc')
    cur = con.cursor()
    cur.execute(sql)
    for result in cur:
         order_sub.append(result[0])         
    cur.close()
    con.close() 

def queryHistory(id):  
         sql = "select * from tas_orders_v where order_id= :id"          
         con = cx_Oracle.connect('tas/welcome1@slcm19-scan1.us.oracle.com:1521/qagainfc')
         cur = con.cursor()         
         cur.execute(sql,id=id)         
         for result in cur:
             #print (result)
             order.append(result)         
         cur.close()
         con.close() 
    
    
createDit()
for i in order_sub:
    print(i)
    queryHistory(i)
for i in order:
    print(i)
    
    