'''
Created on May 31, 2017

@author: chenz
'''
import json

data =  {
  "businesses": [
    {
      "id": "gaumont-wilson-toulouse-2",
      "name": "Gaumont Wilson",
      "city": "Toulouse"           
    },
                 
    {
      "id": "la-cinémathèque-de-toulouse-toulouse",
      "name": "La Cinémathèque de Toulouse",
      "city": "Toulouse"
       },
    {
      "id": "abc-toulouse",
      "name": "ABC",
      "city": "Toulouse"
       },
  ]
}

jsonobject = json.dumps(data)
 
jsonobjectToString = json.loads(jsonobject)
for resp in jsonobjectToString['businesses']:
    print(resp['id'])
    print(resp['name'])
    print(resp['city'])