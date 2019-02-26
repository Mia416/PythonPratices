'''
Created on May 24, 2017

@author: chenz
'''

#sortE = sorted(d.items(), key=lambda value: value[1])
#print (sortE)
    
    
#sort dictionary by key
d = {'a1': 'fsdfds', 'g5': 'aa3432ff', 'ca':'zz23432'}
 
sortvaluelist = sorted(d.keys())
sortresult ={}
 
for i1 in sortvaluelist:   
    sortresult[i1] = d[i1]   
print('=====sort by key=====')
print(sortresult)
print('=====================')
 


# sort dictionary by value
d = {'a1': 'fsdfds', 'g5': 'aa3432ff', 'ca':'zz23432'}
def getkeybyvalue(d,i):
    for k, v in d.items():
        if v == i:
            return (k)
        
sortvaluelist = sorted(d.values())
sortresult ={}
for i1 in sortvaluelist:   
    key = getkeybyvalue(d,i1)
    sortresult[key] = i1
print ('=====sort by value=====')
print (sortresult)
print ('=======================')
    
    
     


 
     