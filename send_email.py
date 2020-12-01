
import os
import smtplib
from email.message import EmailMessage

EMAIL_ADRESS ='abdoessordo01@gmail.com'
EMAIL_PASSWORD = 'qixnzsfvvxuszcgg'

def send_email_for_new_users(name, user_email):
	global EMAIL_ADRESS, EMAIL_PASSWORD
	msg = EmailMessage()
	msg['Subject'] = 'Welcome on board.'
	msg['From'] = EMAIL_ADRESS
	msg['To'] = user_email
	msg.set_content(
		f"Welcome {name}!\nWe are glad to have you with on board and to put your trust in us. We guarantee you that all your passwords are in safe hands :) .\nFor any help, contact us on this email, and we'll do our best to help you.\n\nEA corp."
		)

	with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
		smtp.login(EMAIL_ADRESS, EMAIL_PASSWORD)
		smtp.send_message(msg)


def send_email_new_password_added(name, app, user_email):
	global EMAIL_ADRESS, EMAIL_PASSWORD
	msg = EmailMessage()
	msg['Subject'] = 'New password added to your account.'
	msg['From'] = EMAIL_ADRESS
	msg['To'] = user_email
	msg.set_content(
		f"Hi {name},\nYou have successfully added a password for your {app} account. \nFor any help, contact us on this email, and we'll do our best to help you.\n\nEA corp."
		)

	with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
		smtp.login(EMAIL_ADRESS, EMAIL_PASSWORD)
		smtp.send_message(msg)





