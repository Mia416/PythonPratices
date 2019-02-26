import sys
import os

targetLocation = '/u01/local/wls/user_projects/domains/base_domain/servers/tas_server1/logs'



def query_str(queryString):
    print ('%s has been found in below file' %queryString)
    files = os.listdir(targetLocation)    
    for file in files:        
        if file.endswith('.log') or ('out' in file) or ('log' in file):
           #print file
           filefull =  targetLocation + '/' + file
           #print file
           f = open(filefull,'r')
           for line in f:
                if queryString in line:
                     print (file)
                     break
           f.close()
                

    
pcount = len(sys.argv)
#print str(pcount)
list = [pcount]
i = 1
while (i<=pcount-1):
         #list.insert(i, sys.argv[i])
         #print str(i) +'/n'
         #print sys.argv[i]+'/n'
         query_str(sys.argv[i])
         i = i + 1


