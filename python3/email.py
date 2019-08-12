#coding:utf-8  
import smtplib
from email.mime.text import MIMEText
import sys
mail_host = 'smtp.qq.com' #腾讯服务器
mail_user = '邮箱账号'
mail_pass = '邮箱密码'

def send_mail(to_list,subject,content):
    me = "zabbix3.2监控告警平台"+"<"+mail_user+">"
    msg = MIMEText(content, 'plain', 'utf-8')
    msg['Subject'] = subject
    msg['From'] = me
    msg['to'] = to_list
    try:
        s = smtplib.SMTP()
        s.connect(mail_host)
        s.login(mail_user,mail_pass)
        s.sendmail(me,to_list,msg.as_string())
        s.close()
        return True
    except Exception as e:
        print (str(e))
        return False
if __name__ == "__main__":
    send_mail(sys.argv[1], sys.argv[2], sys.argv[3])

#邮箱地址 邮箱标题 邮箱内容 三个传参