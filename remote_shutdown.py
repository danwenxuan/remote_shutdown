# coding:utf-8

import smtplib
import poplib
import email
from email.mime.text import MIMEText
from email.header import decode_header
import os
import time


"""
此函数用来重置邮箱里面的内容，如果不重置，下次打开程序就会立即获取邮箱里面的命令（关机）
"""
def Reset():
    sent=smtplib.SMTP('smtp.sina.com')
    sent.login('your_own_email@sina.com','************')
    content=MIMEText('')
    to='your_own_email@sina.com'
    content['Subject']='reset'
    content['To']='your_own_email@sina.com'
    content['From']='your_own_email@sina.com'
    sent.sendmail('your_own_email@sina.com',to,content.as_string())
    sent.close()

"""
用POP3来读取远程邮箱内容作为命令
"""
while True:
    host='pop.sina.com'
    duyoujian=poplib.POP3(host)
    duyoujian.user('your_own_email@sina.com')
    duyoujian.pass_('************')
    total=duyoujian.stat()

    str=duyoujian.top(total[0],0)
#    print str 
    strr=[]
    for x in str[1]:
        try:
            strr.append(x.decode())
        except:
            try:
                strr.append(x.decode('gbk'))
            except:
                strr.append(x.decode('big5'))
    msg=email.message_from_string('\n'.join(strr))
    Titt=decode_header(msg['subject'])
# 	 content=decode_header(msg[''])
#    print Titt

    if Titt[0][1]:
        ttle=Titt[0][0].decode[0][1]
        
    else:
        ttle=Titt[0][0]
        
#    print ttle
    if ttle=='guanji':
        Reset()
        
        os.system('shutdown -s -t 60')
        