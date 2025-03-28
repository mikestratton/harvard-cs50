import smtplib

# SMTP connection
s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()
s.login("mikestratton2010@gmail.com", "your app password here")

# Message
message = "Hello, this is a test email from Python!"

# Sending the email
s.sendmail("mike@mikestratton.net", "mike@mikestratton.net", message)
s.quit()