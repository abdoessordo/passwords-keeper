import os
import json
import send_email

USERS_DATA = {}
USERNAMES = []
EMAILS = []
PATH = "C:/Users/hp/Desktop/passwords-keeper/"


def load_DATA(file):
	if os.path.isfile(file):
		with open(file, "r") as f:
			return json.load(f)


def get_Usernames(dicti):
	return list(dicti.keys())


def get_emails(dicti):
	users = get_Usernames(dicti)
	emails = []
	for user in users:
		emails.append(dicti[user]["email"])
	return emails


def add_user(firstname, lastname, username, email, password):
	global USERNAMES
	global EMAILS
	global add_user_results

	EMAILS = get_emails(USERS_DATA)
	USERNAMES = get_Usernames(USERS_DATA)

	results = ["Username or Email is already taken please enter another one.",
				 f"{firstname} {lastname} have been added successfully."]

	if username in USERNAMES or email in EMAILS:
		return add_user_results[0]
	else:
		USERS_DATA[username] = {
			"firstname" : firstname,
			"lastname" : lastname,
			"username" : username,
			"email" : email,	
			"password" : password
		}
		send_email.new_user(firstname, email)

		with open(f'{PATH}/data/passwords_DATA/{username}_passwords.json', 'w') as f:
			json.dump({}, f)
		with open(f"{PATH}/data/users_data.json", "w") as f:
			json.dump(USERS_DATA, f, indent=4)

	
	print(USERS_DATA)
	USERS = get_Usernames(USERS_DATA)
	EMAILS = get_emails(USERS_DATA)
	return add_user_results[1]


def remove_USERS_DATA(mode):
	global USERS_DATA

	if mode == all:
		USERS_DATA = {}
		for file in os.listdir('passwords_DATA'):
			os.remove(f'{PATH}/data/passwords_DATA/{file}')
		print("All users have been deleted")
		return USERS_DATA

	elif mode in(get_Usernames(USERS_DATA)):
		send_email.account_removed(USERS_DATA[mode]['firstname'], USERS_DATA[mode]['email'])
		USERS_DATA.pop(mode)
		os.remove(f'{PATH}/data/passwords_DATA/{mode}_passwords.json')
		print(f"{mode} have been removed")

		with open(f"{PATH}/data/users_data.json", "w") as f:
			json.dump(USERS_DATA, f, indent=4)
		return USERS_DATA

	else: print("User you selected can't be found")

	with open(f"{PATH}/data/users_data.json", "w") as f:
			json.dump(USERS_DATA, f, indent=4)


def login(username, password):
	if username not in(get_Usernames(USERS_DATA)):
		print("Username not valid.")
		return False
	else:
		for user in get_Usernames(USERS_DATA):
			if USERS_DATA[user]["username"] == username and USERS_DATA[user]["password"] == password:
				print('logged in')
				return USERS_DATA[user]["email"]
			elif USERS_DATA[user]["username"] == username and USERS_DATA[user]["password"] != password: 
				print("Password not valid.")
				return False



def add_password(username, app, link, password):
	global add_password_results
	add_password_results = [f"A password for this app have already been added to {username}.", f"Password for {app} has been added added successfully"]
	temp = load_passwords(username)
	if app in list(load_passwords(username).keys()):   #check if the password is existing
		print(add_password_results[0])
		return add_password_results[0]
	else:
		temp[app] = {
			"appname" : app,
			"link" : link,
			"password" : password
		}
		
		send_email.new_password_added(
			USERS_DATA[username]["firstname"], app, USERS_DATA[username]["email"]
			)

		with open(f"{PATH}/data/passwords_DATA/{username}_passwords.json", "w") as f:
			json.dump(temp, f, indent=4)

		print(add_password_results[1])
		return add_password_results[1]	


def load_passwords(username):
	return load_DATA(f"{PATH}/data/passwords_DATA/{username}_passwords.json")


def remove_passwords(username, mode):
	if mode == all:
		send_email.all_passwords_removed(
			USERS_DATA[username]['firstname'], USERS_DATA[username]['email']
			)
		with open(f"{PATH}/data/passwords_DATA/{username}_passwords.json", "w") as f:
			json.dump({}, f)	
	elif mode in list(load_passwords(username).keys()):
		temp = load_passwords(username)
		temp.pop(mode)
		send_email.password_removed(
			USERS_DATA[username]["firstname"], mode, USERS_DATA[username]["email"]
			)
		with open(f"{PATH}/data/passwords_DATA/{username}_passwords.json", "w") as f:
			json.dump(temp, f, indent=4)	
	else:
		print("Password you selected can't be found")



USERS_DATA = load_DATA(f"{PATH}/data/users_data.json")
print("USERS_DATA :", USERS_DATA)
