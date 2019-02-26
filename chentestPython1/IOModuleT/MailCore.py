'''
Created on Mar 14, 2017

@author: chenz
'''
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_mail():
    me = "xiyurui@sina.cn"
    you = "3411379@qq.com"
    username = "xiyurui@sina.cn"
    password = "820311@xiyu"

# Create message container - the correct MIME type is multipart/alternative.
    msg = MIMEMultipart('alternative')
    msg['Subject'] = me
    msg['From'] = me
    msg['To'] = you
    text = "from:xiyurui@sina.cn Hi! \nHow are you?\nHere is the link you wanted:\nhttps://www.python.org"
    part1 = MIMEText(text, 'plain')
    msg.attach(part1)
    #server = smtplib.SMTP('smtp.gmail.com',587)
    server = smtplib.SMTP('smtp.sina.com',25)
    server.set_debuglevel(1)
    server.ehlo()
    server.starttls()
    server.login(username,password)
    server.sendmail(me, you, text)
    server.quit()
    print ('done')
    
    
send_mail()