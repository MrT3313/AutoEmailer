###########
# IMPORTS #
###########
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

##########
# CONFIG #
##########
# Get Variables
email = os.environ.get('M2LD_GMAIL_USERNAME')
pw = os.environ.get('M2LD_GMAIL_PASSWORD')
appPW = os.environ.get('APP_PASSWORD')

# Assign YOUR Gmail Credentials
sending = email
sending_pw = pw

# Add THEIR Gmail
recieving = input('Please Enter Recieving Email: ')
print(recieving)

##########
# CREATE #
##########
# Create Message
msg = MIMEMultipart()
subject = 'H & H Monthly Update'

msg['From'] = sending
msg['To'] = recieving
msg['Subject'] = subject

body = 'THIS IS WHAT I AM SENDING'

msg.attach(MIMEText(body, 'plain'))
text = msg.as_string()

# Make Server
server = smtplib.SMTP('smtp.gmail.com', 587)

# Secure Connection
server.starttls()

# Login
# server.login(email, pw)
server.login(email, appPW)

# Send Message
server.sendmail(sending, recieving, text)

# Quit
server.quit()