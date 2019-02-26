'''
Created on Jun 12, 2017

@author: chenz
https://docs.python.org/3/library/xml.etree.elementtree.html#xml.etree.ElementTree.Element.tail
'''
import xml.etree.ElementTree as ET

name = 'example.xml'
tree = ET.parse(name)
root = tree.getroot()


#As an Element, root has a tag and a dictionary of attributes:
print(root.tag)
print(root.attrib)

#It also has children nodes over which we can iterate:

for child in root:
    print(child.tag)
    print(child.attrib)
    
    
#Children are nested, and we can access specific child nodes by index:
print (root[0][1].text)

#Element has some useful methods that help iterate recursively over all the sub-tree below it 
#(its children, their children, and so on). For example, Element.iter():
for neighbor in root.iter('neighbor'):
    print (neighbor.tag)    
    print(neighbor.attrib)
    
    
#Element.findall() finds only elements with a tag which are direct children of the current element. Element.find() finds the first child with a particular tag, 
#and Element.text accesses the element’s text content. Element.get() accesses the element’s attributes:
for country in root.findall('country'):
     rank = country.find('rank').text
     name = country.get('name')
     print(name, rank)