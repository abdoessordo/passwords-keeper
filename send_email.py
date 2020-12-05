
import os
import smtplib
from email.message import EmailMessage
from datetime import datetime

DATE, TIME = datetime.now().strftime("%d/%m/%Y, %H:%M:%S").split(', ')

EMAIL_ADRESS ='abdoessordo01@gmail.com'
EMAIL_PASSWORD = 'qixnzsfvvxuszcgg'

def new_user(name, user_email):
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


def new_password_added(name, app, user_email):
	global EMAIL_ADRESS, EMAIL_PASSWORD
	msg = EmailMessage()
	msg['Subject'] = 'New password added to your account.'
	msg['From'] = EMAIL_ADRESS
	msg['To'] = user_email
	msg.set_content(
		f"Hi {name},\nYou have successfully added a password for your {app} account on {DATE} at {TIME}. \nFor any help, contact us on this email, and we'll do our best to help you.\n\nEA corp."
		)

	with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
		smtp.login(EMAIL_ADRESS, EMAIL_PASSWORD)
		smtp.send_message(msg)


def app_password_removed(name, app, user_email):
	global EMAIL_ADRESS, EMAIL_PASSWORD
	msg = EmailMessage()
	msg['Subject'] = 'A password have been removed.'
	msg['From'] = EMAIL_ADRESS
	msg['To'] = user_email
	msg.set_content(
		f"Hi {name},\nYou have successfully removed the password for your {app} account on {DATE} at {TIME}. \nFor any help, contact us on this email, and we'll do our best to help you.\n\nEA corp."
		)

	with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
		smtp.login(EMAIL_ADRESS, EMAIL_PASSWORD)
		smtp.send_message(msg)


def all_passwords_removed(name, user_email):
	global EMAIL_ADRESS, EMAIL_PASSWORD
	msg = EmailMessage()
	msg['Subject'] = 'All password have been removed.'
	msg['From'] = EMAIL_ADRESS
	msg['To'] = user_email
	msg.set_content(
		f"Hi {name},\nYou have successfully removed all your passwords on {DATE} at {TIME}. \nFor any help, contact us on this email, and we'll do our best to help you.\n\nEA corp."
		)

	with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
		smtp.login(EMAIL_ADRESS, EMAIL_PASSWORD)
		smtp.send_message(msg)

def account_removed(name, user_email):
	global EMAIL_ADRESS, EMAIL_PASSWORD
	msg = EmailMessage()
	msg['Subject'] = 'Account removed.'
	msg['From'] = EMAIL_ADRESS
	msg['To'] = user_email
	msg.set_content(
		f"Hi {name},\nYou have successfully deleted your account on {DATE} at {TIME}. \nFor any help, contact us on this email, and we'll do our best to help you.\n\nEA corp."
		)

	with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
		smtp.login(EMAIL_ADRESS, EMAIL_PASSWORD)
		smtp.send_message(msg)