import os
import sys
import platform
 
 
def input_paramter():
    inputName = input("Enter the name:")
    inputAge = input ("Enter the age:")
    write_file(inputName + inputAge)
    
    
def write_file(infomation):
    filename = getcurrentPath() + "PythonTest1.log"     
    if not os.path.isfile(filename):
      f = open(filename,"w+")    
    else:
      f = open(filename,"w")  
    f.write("information  is : %s" % infomation)
    f.write("\n")
    f.close()
    print ("write the login information into file done")
        
#./demo.py input.txt output.txt
def get_inputparameter():
    paramterAccount = len (sys.argv)
    cmdargs = str(sys.argv)
    print ("The total number of args are :%d" % paramterAccount)
    print ("Args list: %s" %cmdargs)
    print ("first: %s" % str(sys.argv[0]))
    print ("second argument: %s" % str(sys.argv[1]))
    print ("third argument: %s" % str(sys.argv[2]))
 
 
#create file and write string
def create_file():
    print("create file function start\n")
    
    filename = getcurrentPath() + "PythonTest1.log" 
               
    if os.path.isfile(filename):
      f = open(filename,"a+")
      f.write("append file and hello world\n")
    else:
      f = open(filename,"w+")
      f.write("new file and hello world\n")
    
    
    f.close()
    print("create file function end\n")
    
#get current path
def getcurrentPath():
    cwd = os.getcwd()
    if (platform.system().find('Windows')!=-1):
        cwd = cwd + '\\'
    if (platform.system().find('Linux')!=-1):   
         cwd = cwd + '/'      
    return cwd 

#read file
def read_file():
    print("read file function start\n")
    filename = getcurrentPath() + "PythonTest1.log"
    if os.path.isfile(filename):
      f = open(filename,"r")
      t1 = f.readline()
      print("read file function end\n")
      return t1
  
  
def list_file():
      targetLocation = getcurrentPath();
      files = os.listdir(targetLocation)
      for file in files:
        print (file+"\n")
          
def query_string(queryString):    
      targetLocation = getcurrentPath();
      files = os.listdir(targetLocation)
      for file in files:
          if file.endswith(".log"):
            with open(file) as f:
               for line in f:
                 if queryString in line:
                   print (file+"\n")
      
  