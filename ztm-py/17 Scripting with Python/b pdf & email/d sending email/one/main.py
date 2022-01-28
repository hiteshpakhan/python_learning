import smtplib
from email.message import EmailMessage

email = EmailMessage()
email["from"] = "hitesh pakhan"
email["to"] = "hitesh5pakhan@gmail.com"
email["subject"] = "hee nice work"

email.set_content("learning python good luck")

with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login("abcdfga566@gmail.com", "Luci@714")
    smtp.send_message(email)
    print("all good")

# to run this code you shoud enter the account that has less security
# you can do this by visiting th efollowing link
# https://www.google.com/settings/security/lesssecureapps