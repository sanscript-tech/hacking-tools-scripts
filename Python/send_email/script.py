import smtplib

server = smtplib.SMTP("smtp.gmail.com",587)
server.starttls()
senderEmail = input(str("Enter sender's Email:"))
password = input(str("Enter password:"))
receiverEmail = input(str("Enter receiver's Email:"))
subject = input(str("Enter subject"))
body = input(str("Enter message"))
message = "Subject:{}\n\n{}".format(subject,body)
server.login(senderEmail,password)
server.sendmail(senderEmail,receiverEmail,message)
print("Email sent successfully !!!")
server.quit()