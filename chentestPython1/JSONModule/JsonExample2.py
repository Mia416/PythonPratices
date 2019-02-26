'''
Created on May 27, 2017

@author: chenz
'''

import json

data = {"project":"platform/xxxxx/xxxxxx/build/repo","branch":"xxxxx_xx.xxxxx.xxx.1.0-dev","id":"T19797TIE76757IT78689899G",
        "number":"1917095","subject":"xxxxx-2.0: blah blah blah","owner":{"name":"David","email":"david@xxxx.com","username":"david"},
        "url":"https://link_to_repo.com/1917095","createdOn":"1493282302","lastUpdated":"1493813064","sortKey":"000899786887","open":"false","status":"MERGED"}

jsonobject = json.dumps(data)
print (jsonobject)
jsonobjectToString = json.loads(jsonobject)
print (jsonobjectToString)

print (jsonobjectToString["number"])
 