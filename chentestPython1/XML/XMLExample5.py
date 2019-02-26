'''
Created on Jun 13, 2017

@author: chenz
My problem is with "TEXTA". I have tried  TagA.text, which always returned None. Does anyone have any idea how I should get the "TEXTA" out?
'''
import xml.etree.ElementTree as ET

name = 'tail.xml'
tree = ET.parse(name)
root = tree.getroot()

print(root.find('TAGB').tail.strip())