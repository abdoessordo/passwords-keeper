import os
import json
from send_email import send_email_for_new_users

DATA = {}
USERS = []


def load_DATA():
	global DATA
	if os.path.isfile("data.json"):
		with open("data.json", "r") as f:
			DATA = json.load(f)


def get_Users(dicti):
	users = []
	for key in dicti.keys():
			users.append(key)
	return users

	
def get_usernames(dicti):
	users = get_Users(dicti)
	usernaems = []
	for user in users:
		usernaems.append(dicti[user]["username"])
	return usernaems


def get_emails(dicti):
	users = get_Users(dicti)
	emails = []
	for user in users:
		emails.append(dicti[user]["email"])
	return emails


def add_user(firstname, lastname, username, email, password):
	if username in(get_usernames(DATA)) or email in(get_emails(DATA)):
		print("Username or Email is already taken please enter another one.")
	else:
		DATA[f"{firstname} {lastname}"] = {
											"firstname" : firstname,
											"lastname" : lastname,
											"username" : username,
											"email" : email,
											"password" : password
										}
		send_email_for_new_users(firstname, email)
		print(f"Welcome {firstname}! We garantee you that all your passwords are in safe hands :) .")

		global USERS
		USERS = get_Users(DATA)


def clear_DATA(mode=all):
	global DATA

	if mode == all:
		DATA = {}
		get_Users(DATA)
		return DATA

	elif mode in(get_Users(DATA)):
		get_Users(DATA)
		DATA.pop(mode)
		return DATA


def login(username, password):
	if username not in(get_usernames(DATA)):
		print("Username not valid.")
		return False
	else:



		for user in get_Users(DATA):
			if DATA[user]["username"] == username and DATA[user]["password"] == password:
				print("loged in succesfully")
				return True
			elif DATA[user]["username"] == username and DATA[user]["password"] != password: 
				print("Password incorrect. Try again.")
				return False

				

load_DATA()

# login("abdoessordo", "Tanger.2001")

# add_user("Abdellah", "Essordo", "abdoessordo", "abdoessordo01@gmail.com", "Tanger.2001")
# add_user("firstname", "lastname", "username", "email", "password")
# add_user("Ayman", "Essordo", "ayman272002", "ayman2272002@gmail.com", "Tanger.2002")


# clear_DATA("Ayman Essordo")
# clear_DATA()

print("DATA :", DATA, "\n")
# print("USERS :", get_Users(DATA))
# print("USERNAMES :", get_usernames(DATA))
# print("EMAILS :", get_emails(DATA), '\n')


with open("data.json", "w") as f:
	json.dump(DATA, f, indent=4)