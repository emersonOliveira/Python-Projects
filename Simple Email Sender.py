import smtplib
from email.message import EmailMessage

email = EmailMessage()
email['from'] = 'Emerson Oliveira' #Insert your name here
email['to'] = 'example@gmail.com' #Email you want to contact
email['subject'] = 'Email subject goes here'

email.set_content('Email content goes here')

#Login to your account
with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('example@gmail.com','passwordgeneratedhere') #Use your email and password generated for this app on your Google Security settings
    smtp.send_message(email)
    print('Email(s) sent!')