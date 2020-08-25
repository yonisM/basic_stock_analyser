#### Where ever you see python comments, is what you should change. IF it doesnt contain a python comment do not change!!!

import smtplib, ssl
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders

fromaddr="yonis838@googlemail.com" #Person sending in the email. 
sendto =['yonis.mohamoud@live.co.uk','yonis838@googlemail.com'] #List of email address you will be sending the email to
password = 'odqhescsdicrxbdx' #create an APP Password with Google 


msg = MIMEMultipart()
msg['From'] = fromaddr
msg['Bcc'] = ', '.join(sendto) #Feel free to change to change BCC to CC or To. 
msg['Subject'] = "Basic: Ticker Symbol trade volume and price yesterdays report" # The email subect line

body = """
Hello Everyone, 

Please see attached document for the latest analysis of yesterday's stocks and indexes. 

If you have any questions, queries, or comments, please feel free to get in touch with me and I will be more than happy to assist you. 

With Regards,

Yonis Mohamoud

#### This is a test run scheduler.

""" # The body of the email, write whatever you like


msg.attach(MIMEText(body, 'plain'))

filename = 'stock_analysis.html' # This is the name you will give your new attached document 
attachment = open('stock_analysis.html', 'rb') # add in the filepath and filename of the file you want to attach

part = MIMEBase('application', "octet-stream")
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', 'attachment; filename= %s' % filename)

msg.attach(part)


try:
    smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
    smtpObj.ehlo()
    smtpObj.starttls()
    smtpObj.login(fromaddr, password)

    text = msg.as_string()
    smtpObj.sendmail(fromaddr, sendto , text)
    smtpObj.quit()
    print("Success")
except Exception as e:
    print(e)