'''
Created on May 25, 2017

@author: chenz
'''

# t1.join ==== main thread waits at t1.join() until thread t1 finishes before it moves on to t2.join().
import threading
import time
 

def music(name):
    for i in range(5):        
        print ("play music at %s: %s" % ( name, time.ctime(time.time()) ))    
        time.sleep(1)

def movie(name):
    for i in range(5):        
        print ("watch movie at %s: %s" % ( name, time.ctime(time.time()) ))    
        time.sleep(5)
        

threads = []
t1 = threading.Thread(target=music,args=(u'sing one',))
threads.append(t1)
t2 = threading.Thread(target=movie,args=(u'movie one',))
threads.append(t2)
t3 = threading.Thread(target=movie,args=(u'movie two',))
threads.append(t3)



 
#These threads run in parallel
t1.start()
t2.start()
t3.start()
t1.join()
t2.join()
 
 
'''
 #these run sequentially
for t in threads:
    t.setDaemon(True)
    t.start()
    t.join()
 '''   

print ("all over : %s" % (time.ctime(time.time()) ))  
    