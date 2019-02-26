'''
Created on Feb 20, 2017

@author: chenz
'''

from flask import Flask,url_for,request,json
 

application = Flask(__name__)

#By default, a route only answers to GET requests, but that can be changed by providing the methods argument to the route() decorator


#call http://127.0.0.1:5000/  GET
@application.route("/")
def hello():  
    return "Hello World!111111111111111111111111111"

#call http://127.0.0.1:5000/product  GET
@application.route("/product")
def hellow():  
    return "Hello World!22222222222222"

#call http://127.0.0.1:5000/user/zhangchen  GET
@application.route("/user/<username>")
def Function1(username):
    return "User: %s " % username


#call http://127.0.0.1:5000/post/33 GET
@application.route('/post1/<int:post_id>')
def show_post(post_id):   
    return 'Post %d' % post_id


#call http://127.0.0.1:5000/putmultiplePara?uname=zhangchen&pass=123456  GET
@application.route('/putmultiplePara/')
def show_multiple():
    username = request.args.get('uname')
    password = request.args.get('pass')
 
    return 'Username:  %s' %username + 'Password:  %s' %password


#call http://127.0.0.1:5000/testpost POST 
 
@application.route('/testpost',methods=['POST'])
def posthello(): 
    return "post here"


#call http://127.0.0.1:5000/testpostdata POST 
# ROWPayload  name=aaaa&age=122  or DataForm name=aaaa   age =122
 
@application.route('/testpostdata',methods=['POST'])
def postdata():
       print (request.form)
       print (request.form['name'])
       print (request.form['age'])
       name = request.form['name']
       age =  request.form['age']
       return "Name is %s and age is %s" %(name,age)
 

#call http://127.0.0.1:5000/testJson  POST  Content-Type: application/json
#ROWPayload:  {"username":"xyz","password":"xyz"}

@application.route('/testJson',methods=['POST'])
def postjson():
    if request.headers['Content-Type'] == 'application/json':
        return "JSON Message: " + json.dumps(request.json)
    

if __name__ == "__main__":  
    application.run()
