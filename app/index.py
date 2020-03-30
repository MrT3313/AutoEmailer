import smtplib

server = smtplib.SMTP('smtp.gmail.com', 587)

# Secure Connection
server.starttls()

# Credentials
email_user = 'your_email'
email_password = 'your_password'
email_send = 'recipient_email'

