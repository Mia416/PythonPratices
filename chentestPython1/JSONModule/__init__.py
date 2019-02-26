import json
import urllib.request
from urllib.request import urlopen
import xml.etree.ElementTree as ET
import XMLModule
#https://docs.python.org/3/library/json.html
#load() loads JSON from a file or file-like object
#loads() loads JSON from a given string or unicode object
#Encode过程，是把python对象转换成json对象的一个过程，常用的两个函数是dumps和dump函数。两个函数的唯一区别就是dump把python对象转换成json对象生成一个fp的文件流，而dumps则是生成了一个字符串：
#python_to_json = json.dumps(jsonstring)
#python_to_json2 = json.dumps(jsonstring,sort_keys=True,indent =4,separators=(',', ': '),ensure_ascii=True )
#json_to_python = json.loads(python_to_json2)


#dumps takes an object and produces a string:json dumps -> returns a string representing a json object from an object.
#load would take a file-like object, read the data from that object, and use that string to create an object: returns an object from a string representing a json object.


def load_fromURL():
    url = 'http://idoru.oraclecorp.com:8080/v1/services/_/versions/_/artifacts?release=17.2.1&previous_release=17.1.6&qualifiers=tasbp'
    response = urlopen(url)
    json_to_python = json.load(response)
    #print (json_to_python)
    #urlpath = (json_to_python["artifacts"][1]["uri"])
    for node in json_to_python["artifacts"]:
        print (node["uri"])
        
def load_fromString():
    jsonstring ={
     'artifacts':
     [
     {
      'qualifier':'tasbp',
      'service':{
        'release':'17.2.1',
        'display_name':'Application Container Cloud',
        'artifact_id':'apaas',
        'version':'17.2.1-531',
        'target_maturity':'production',
        'service_id':'c7928dd7-dca5-4225-9486-f2286e417e45'
        },
     'uri':'http://almrepo.us.oracle.com/artifactory/opc-woodhouse-release/com/oracle/opc/definition/tasbp-apaas/17.2.1-1703131042/tasbp-apaas-17.2.1-1703131042.zip'
     },
     {
      'qualifier':'tasbp',
      'service':{
        'release':'17.2.1',
        'display_name':'psm',
        'artifact_id':'psm',
        'version':'17.2.1-548',
        'tags':[
        '17.2.1.2'
               ],
     'target_maturity':'production',
     'service_id':'8720ac6d-c99b-4bbe-9958-094ee35bc99c'
     },
     'uri':'http://almrepo.us.oracle.com/artifactory/opc-woodhouse-release/com/oracle/opc/definition/tasbp-psm-jaas/17.1.5-543/tasbp-psm-jaas-17.1.5-543.zip'
     },
     ]
     }
    python_to_json2 = json.dumps(jsonstring,sort_keys=True,indent =4,separators=(',', ': '),ensure_ascii=True )
    json_to_python = json.loads(python_to_json2)
    for node in json_to_python["artifacts"]:
        urladdress = node["uri"]
        filename = urladdress.split('/')[-1]
        req = urllib.request.urlretrieve(urladdress, filename) 
        print (node["uri"])
    





    
def load_xml_node():
        xmltree = ET.parse('tasbp-psm-JaaSTASBlueprint.xml')
        for node in xmltree.findall('.//{http://xmlns.schemas.oracle.com/tasBlueprint}name'):
            print (node.tag, node.text)
            break
        for node in xmltree.iter('{http://xmlns.schemas.oracle.com/tasBlueprint}name'):
            print (node.tag, node.text)
            break
     



#exec  
load_fromString()

 