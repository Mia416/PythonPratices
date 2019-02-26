'''
Created on May 24, 2017

@author: chenz
'''




# if the json string has [] , when we get value, need to use[0......5] , otherwise , will use string like ['a']['b']

#dumps takes an object and produces a string:json dumps -> returns a string representing a json object from an object.
#load would take a file-like object, read the data from that object, and use that string to create an object: returns an object from a string representing a json object.



import json


# if the original is string like '' . we could use json.loads directly , and below code will retrive all the key and value for the json-dictionary 
s = '[{"i":"imap.gmail.com","p":"someP@ss"},{"i":"imap.aol.com","p":"anoterPass"}]'
jdata = json.loads(s)
print (jdata)
for d in jdata:
    for key, value in d.items():
        print (key, value)


# The u means a unicode string which should be perfectly fine to use
json_data={u'mimeType': u'application/vnd.google-apps.folder', u'version': u'17', u'appDataContents': False, u'labels':u'aaaa'}
data = json.dumps(json_data)
json_to_python = json.loads(data)
print (json_to_python['version'])


 
# there has dup info, so after dump, the first one removed. and since there has [] , so we use [0] to get the first data element
json_data = { "action":"postRecord", "data":{ "data":[ { "info":{ "lid":999, "cid":1234 }, "info":{ "lid":111, "cid":"6789" } } ] } }
data = json.dumps(json_data)
json_to_python = json.loads(data)
print (json_to_python)
print (json_to_python['data']['data'][0]['info']['cid'])



# there is no [] , so all the element get by ['xxx']
jsonstring = {
    "1":    
    {
        "name": "foo",
        "color": "black",
        "children": ["2", "3"]
     },
    "2": {
        "name": "foo2",
        "color": "green",
        "children": ["1","6"]
     },
     
}

print (list(jsonstring.keys()))
print (list(jsonstring.values()))

#dumps the json object into an element
data = json.dumps(jsonstring)

#load the json to a string
json_to_python = json.loads(data)

print (json_to_python)
print (json_to_python["1"]["name"])
print (json_to_python["1"]["children"])

 
      



