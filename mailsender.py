from email.message import EmailMessage
from passcode import password
import ssl
import smtplib

mail_sender = 'kimberlypeters301@gmail.com'
mail_password = password

mail_receiver = 'tapeve1312@iunicus.com'

subject = "Keep Practicing"
body ="""
Practice is the only way you'll get better
"""

em = EmailMessage()
em['From'] = mail_sender
em['To'] = mail_receiver
em['subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(mail_sender, mail_password)
    smtp.sendmail(mail_sender, mail_receiver, em.as_string())
