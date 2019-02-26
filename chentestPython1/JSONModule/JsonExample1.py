'''
Created on May 27, 2017

@author: chenz
'''

import json
import csv

data = {
  "products": [
    {
      "product_cp": 100.0,  
      "product_sp": 120.0, 
      "product_name": "coke", 
    }, 
    {
      "product_cp": 100.5, 
      "product_sp": 120.0, 
      "product_name": "fanta", 
    }, 
    {
      "product_cp": 70.5,  
      "product_sp": 100.5, 
      "product_name": "pepsi", 
    }
  ]
}

jsonobject = json.dumps(data)
#print (jsonobject)
jsonobjectToString = json.loads(jsonobject)
#print (jsonobjectToString)


resultresp=[]
for level1 in jsonobjectToString["products"]:
    str = level1["product_cp"],level1["product_sp"],level1["product_name"]
    resultresp.append(str)
    with open('output.csv', 'a+', newline='', encoding='utf-8') as f_output:
        csv_output = csv.writer(f_output)
        csv_output.writerow(str)
        
    
   
    #print (level1["product_cp"],level1["product_sp"],level1["product_name"])
print(resultresp)

#print (jsonobjectToString["products"])
 