'''
Created on Jun 12, 2017

@author: chenz
'''
import xml.etree.ElementTree as ET

name = 'XMLNamespace.xml'
tree = ET.parse(name)
root = tree.getroot()

tag1 = root.find('.//{http://some/www.hello.com}tag1')  # accessing tag with namespace

print(tag1.text)
