from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
message = MIMEMultipart()
message["from"] = "Aryan Ibrahim"
message["to"] = "aryanibrahimion@gmail.com"
message.attach(MIMEText("I used python!"))
with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login(user="aryanibrahimion@gmail.com", password="07112010")
    smtp.send_message(message)
    print("Message Sent")