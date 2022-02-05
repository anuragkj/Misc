# using SendGrid's Python Library
# https://github.com/sendgrid/sendgrid-python
import os
import sendgrid
from sendgrid.helpers.mail import *

message = Mail(
    from_email='anurag.jha.in@gmail.com',
    to_emails=['jha.ashish.in@gmail.com','anurag.jha.in@gmail.com','jha.ashish.jvm@gmail.com'],
    subject='Sending with Twilio SendGrid is Fun',
    html_content='<strong>and easy to do anywhere, even with Python</strong>')
try:
    sg = sendgrid.SendGridAPIClient("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")
    response = sg.send(message)
    print(response.status_code)
    print(response.body)
    print(response.headers)
    print("Suceess")
except Exception as e:
    print("Error")
    print(e)