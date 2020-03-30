import os
# import smtplib

# Get Variables
email = os.environ.get('M2LD_GMAIL_USERNAME')
pw = os.environ.get('M2LD_GMAIL_PASSWORD')

# Assign YOUR Gmail Credentials
sending = email
sending_pw = pw

# Add THEIR Gmail
recieving = input('Please Enter Recieving Email: ')
print(recieving)


# Make Server
# server = smtplib.SMTP('smtp.gmail.com', 587)

# Secure Connection
# server.starttls()


