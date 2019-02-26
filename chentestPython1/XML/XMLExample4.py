'''
Created on Jun 13, 2017

@author: chenz
How to pull all the child nodes of country?

For Example, I need the output as ['rank','year','gdp','neighbor']
'''
import xml.etree.ElementTree as ET

name = '4.xml'
tree = ET.parse(name)
root = tree.getroot()

ditresult =[]

for child in root:
    for child1 in child:         
         ditresult.append(child1.tag)
          
print (ditresult)
