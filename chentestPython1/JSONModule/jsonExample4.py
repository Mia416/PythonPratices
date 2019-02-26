'''
Created on May 31, 2017

@author: chenz
'''

import json

data = {"hostname": "DESKTOP-A5C21U7", "ts": 1494334366.1905415, "parameters":
[{"label": "T16", "name": "T16", "unit": "K", "value": 78.84589895546188}, 
{"label": "PID Mode", "name": "pid_mode", "unit": "", "value": "off"}, 
 {"label": "IDN", "name": "IDN", "unit": "", "value": 
 {"vendor": "null", "model": "dummy", "serial": "null", "firmware": "null"}}, 
 {"label": "PID Mode", "name": "pid_ramp", "unit": "", "value": "off"}, 
 {"label": "PID heater range", "name": "pid_range", "unit": "mA", "value": 0.316},
 {"label": "Status", "name": "status", "unit": "", "value": "Error"}, 
 {"label": "PID temperature setpoint", "name": "pid_setpoint", "unit": "K", "value": 0.0},
 {"label": "PID ramp rate", "name": "pid_rate", "unit": "K/min", "value": 0.0},
 {"label": "Current action", "name": "action", "unit": "", "value": "Idle"},
 {"label": "T6", "name": "T6", "unit": "K", "value": 180.17461269853666}]}

jsonobject = json.dumps(data)
 
jsonobjectToString = json.loads(jsonobject)
 

for resp in jsonobjectToString["parameters"]:
    print (resp["label"])
    print (resp["name"])
    print (resp["unit"])
    print (resp["value"])
 




