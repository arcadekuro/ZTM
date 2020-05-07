"""
smtp is a protocol for sending emails.
stands for simple, mail transfer protocol.
sending an email through python <- access a domain.
Automate process of sending an email.
"""
import smtplib

# set a domain name and a port. SMTP method takes a domain and a port.
# 587 is the general port number according the the encryption standard TLS.
# base64 key value pair encoded 4 login
# or best way is to use libray or keystore - valut.
smtpObj = smtplib.SMTP('smtp.gmail.com', 587)

SENDER = 'arcadekuro@gmail.com'
RECIPIENT = 'fill in later'

# communicating between servers.
smtpObj.ehlo()
smtpObj.starttls()
smtpObj.login('{}@gmail.com', '{}'.format())  # - to login
smtpObj.sendmail('{SENDER}', '{RECIPIENT}',
                 'subject: SMTPcheck \n')
smtpObj.quit()
