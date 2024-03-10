import emails
import os
import email.message
import mimetypes
import smtplib

from datetime import datetime
x=datetime.date.today()

sender = "automation@example.com"
receiver = "{}@example.com".format(os.environ.get('USER'))
subject = "Upload Completed - Online Fruit Store"
body = "All fruits are uploaded to our website successfully. A detailed list is attached to this email."

message = emails.generate(sender, receiver, subject, body, "/tmp/report.pdf")
emails.send(message)
