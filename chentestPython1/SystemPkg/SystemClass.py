'''
Created on Jun 30, 2017

@author: chenz
'''
import platform
 

class SystemEntity:
    def __init__(self):
        print ('this is system class')
    
    def getSystem(self):
        return platform.uname().system
    
    def getAllSystem(self):
        return platform.uname()
    
    def getRelease(self):
        return platform.release()

    def getSupport_Linux(self):
        return platform._supported_dists
    
    def getArc(self):
        return platform.architecture()

system1 = SystemEntity()
print (system1.getSystem())
print (system1.getAllSystem())
print (system1.getRelease())
print (system1.getSupport_Linux())
print (system1.getArc())