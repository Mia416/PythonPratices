'''
Created on Jul 20, 2017

@author: chenz
'''
print('aaaaaaa')
listtemp = []
list1 =[]
filename = "D:/mockdata.log" 
f = open(filename,"r")
t1 = f.readline()
listtemp = t1.split(',')  
#tur1 = ('%s,%s,%s,%s,%s,%s,%s,%s' % (temp[0],temp[1],temp[2],temp[3],temp[4],temp[5],temp[6],temp[7])) 
list1.append(listtemp)
print (list1)
for i in list1:
    print (i)
    print (str(i[0]))
