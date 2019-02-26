import xml.etree.ElementTree as ET

# when the xml like <s:name>Oracle Bare Metal Cloud Service</s:name> , find method need to input full property name include namespace
# './/{http://xmlns.schemas.oracle.com/tasBlueprint}name'

xmlpath = 'test.xml'
#xmlpath = 'pic-tas-blueprint.xml'
 
def list_tree():
    xmltree = ET.parse(xmlpath)
    for node in xmltree.iter():
        print (node.tag, node.attrib)

 
def list_node():
    xmltree = ET.parse(xmlpath)
    root = xmltree.getroot()   
    for child in root:
        print(child.tag, child.attrib)


#XMLModule.list_node_subvalue('outline')        
def list_node_subvalue(nodename):
    xmltree = ET.parse(xmlpath)
    for node in xmltree.iter(nodename):
        name = node.attrib.get('name')
        url = node.attrib.get('foo')
        type = node.attrib.get('type')
        htmlUrl = node.attrib.get('htmlUrl')
        if name and url:
             print ('  %s :: %s :: %s :: %s' %(name, url,type,htmlUrl))
        else:
             print (name)

#query node attribute 
#XMLModule.find_node_attrib('outline')
def find_node_attrib(nodename):
    xmltree = ET.parse(xmlpath)
    for node in xmltree.findall('.//%s' %nodename):
        url = node.attrib.get('xmlUrl')
        name = node.attrib.get('text')
        print (' %s   ::   %s' %(name, url))


#query node property        
#XMLModule.find_node('outline')  test.xml
#XMLModule.find_node_property('{http://xmlns.schemas.oracle.com/tasBlueprint}name')   pic-tas-blueprint.xml
def find_node_property(nodename):
    xmltree = ET.parse(xmlpath)
    for node in xmltree.findall('.//%s' %nodename):    
         print ('  %s  ::  %s ::   %s' %(node.tag,node.text ,node.tail))


#query node attribute and property
def find_node_all(nodename):
    xmltree = ET.parse(xmlpath)
    for node in xmltree.findall('.//%s' %nodename):
        name = node.attrib.get('name')
        foo = node.attrib.get('foo')
        print (' %s   ::   %s' %(name, foo))
        print ('  %s  ::  %s ::   %s' %(node.tag,node.text ,node.tail))
        
        

#XMLModule.find_node_one('title','Podcasts')  using 'pic-tas-blueprint.xml'
def find_node_one(nodename,value):
    xmltree = ET.parse(xmlpath)
    for node in xmltree.findall('.//%s' %nodename):
        t = node.find('rank').text
        print (t)
        t1 = node.text  
        if value in t1 :
            print ('  %s  ::  %s ::   %s' %(node.tag,node.text ,node.tail))   
 
         
      
#query the  node attribute and property using iter
#iter using value not the fullname 
#XMLModule.find_node_property('{http://xmlns.schemas.oracle.com/tasBlueprint}name')   pic-tas-blueprint.xml
def find_node_iter(nodename):
    xmltree = ET.parse(xmlpath)
    #if findall ,need use './/nodename' it iter using node name directly
    for node in xmltree.iter(nodename):
        #name = node.attrib.get('name')
        #foo = node.attrib.get('foo')
        #print (' %s   ::   %s' %(name, foo))
        print ('  %s  ::  %s ::   %s' %(node.tag,node.text ,node.tail))
           

 