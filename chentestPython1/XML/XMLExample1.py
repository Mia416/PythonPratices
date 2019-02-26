'''
Created on Jun 12, 2017

@author: chenz
'''
import xml.etree.ElementTree as ET

name = '1.xml'
tree = ET.parse(name)
root = tree.getroot()
element = root[0].tag
first_text = root[0].text #This is the first sentence
button = root[0][0].tag #button
buttontext = root[0][0].text #click

for node in tree.iter('element'):
    print(node.text)
    print(node.attrib)