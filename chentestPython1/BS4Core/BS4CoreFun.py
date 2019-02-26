from bs4 import BeautifulSoup
import io
import sys
import time
import urllib.request
import urllib
import traceback 
import os
import logging
import MyLog
 
'''
Created on Feb 15, 2017

@author: chenz
'''
logging = MyLog.get_logger('x.ini','Lianjia.log')



def agent_set():
    headers = {}
    headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
    return headers
   

def proxy_set():
    proxy_support = urllib.request.ProxyHandler({'http': 'http://cn-proxy.jp.oracle.com:80'})
    opener = urllib.request.build_opener(proxy_support)
    urllib.request.install_opener(opener)
    logging.info("proxy added")
   # urllib.urlopen("http://www.google.com", proxies=proxies)
    
def get_information(proxy):         
     # 连公司网络，urlopen打不开, 如何解决公司网络有代理的问题
     #更改ecslipe eclipse.ini , add "-Dfile.encoding=UTF-8"
     
    #sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')   
          
    url="http://tj.lianjia.com/ershoufang/co32/"         
    call(url,proxy)
    pageint = 2      
    while (pageint<100):
        url = "http://tj.lianjia.com/ershoufang/pg%s"  %str(pageint)+"co32"
        print ("page %s" %str(pageint))
        call(url,proxy)
        time.sleep(5)
        logging.info("page %s" %str(pageint))
        pageint = pageint+1
    

def create_logfile(info):
    logging.info("create file function start\n")
    mailpath = "D:\\PythonDataLog\\"
    filename = mailpath + info + ".log"    
    if os.path.isfile(filename):
      f = open(filename,"a+")      
      f.write(info)
    else:
      f = open(filename,"w+")
      f.write(info)   
    
    f.close()
    logging.info("create file function end\n")
        
def call(url,proxy):   
    if(proxy): 
        proxies=proxy_set()
        
        
    headers = agent_set()    
    req = urllib.request.Request(url, headers = headers)
    page = urllib.request.urlopen(req)    
    soup = BeautifulSoup(page.read(),"html.parser");    
    universities=soup.find_all(class_='lj-lazy')
    for university in universities:           
      try:
        print(university['alt'])
        print(university['data-original'])
       #logging.info(university['alt'])
       #create_logfile(university['alt'])
        name = university['alt'].strip()
        path = university['data-original']
        create_logfile(university['alt'])
        save_pic(path,name)
      except:
       logging.error("not found")    

       
       
     
   
def save_pic(path,name):
    image_local_path = "D:\\PythonDataLog\\"
    try:  
        image_local_path = image_local_path + name + '.jpg'
        print (image_local_path)
        urllib.request.urlretrieve(path,image_local_path)
    except Exception as err:
         print(err)   # something wrong with local path
     
       
       