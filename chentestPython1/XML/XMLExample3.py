'''
Created on Jun 13, 2017

@author: chenz
I need to fetch the username from this XML script.
'''
import xml.etree.ElementTree as ET

name = '3.xml'
tree = ET.parse(name)
root = tree.getroot()
 
    
    
print (root[1][0].get('name'))    

for neighbor in root.iter('part'):
    print(neighbor.get('name'))
    #print (neighbor.tag)    
    #print(neighbor.attrib)