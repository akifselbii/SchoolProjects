#Mehmet Akif SELBİ

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

#mail atmak için
def mail(konu,yazi,mail): 
    msg = MIMEMultipart()

    password = #email password
    msg['From'] = "COMU Duyuru"
    msg['To'] = str(mail)
    msg['Subject'] = str(konu)

    body = str(yazi)
    body_text = MIMEText(body, "plain")
    msg.attach(body_text)
     
    server = smtplib.SMTP('smtp.gmail.com: 587')
     
    server.starttls()
     
    server.login("", password)#email and password
     
     
    server.sendmail(msg['From'], msg['To'], msg.as_string())
     
    server.quit()
     
    print ("Mail Gönderildi %s:" % (msg['To']))
