import smtplib, ssl
import os

host = "smtp.gmail.com"
port = 465 # 465  for ssl, use 587 for TLS

PASSWORD = os.getenv("python_email_password")
USER_NAME = "fransiTestMail@gmail.com"


def send_mail(contact_email, message):
    context = ssl.create_default_context()
    
    message = f"""\
Subject: New contact-email

{message} from {contact_email}
"""

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(USER_NAME, PASSWORD)
        server.sendmail(USER_NAME, contact_email, message)