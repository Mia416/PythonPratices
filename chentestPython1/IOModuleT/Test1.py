'''
Created on Mar 6, 2017

@author: chenz
'''
import sys
import os

targetLocation = '/u01/local/wls/user_projects/domains/base_domain/servers/tas_server1/logs'

def query_str(queryString):
    files = os.listdir(targetLocation)
    
    for file in files:
        if file.endswith(".log"):
            with open(file) as f:
                for line in f:
                    if queryString in line:
                        print (file.name + 'found %s ' %queryString)
                        print ('/n')

pcount = len(sys.argv)
print str(pcount)
list = [pcount]
i = 1
while (i<=pcount-1):
         list.insert(i, sys.argv[i])
         print str(i) +'/n'
         print sys.argv[i]+'/n'
         i = i +1
         query_str(sys.argv[i])


