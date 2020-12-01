import os
import json
from send_email import send_email_for_new_users, send_email_new_password_added

USERS_DATA = {}
USERS = []


def load_DATA(file):
	if os.path.isfile(file):
		with open(file, "r") as f:
			return json.load(f)



def get_Users(dicti):
	users = []
	for key in dicti.keys():
			users.append(key)
	return users


def get_emails(dicti):
	users = get_Users(dicti)
	emails = []
	for user in users:
		emails.append(dicti[user]["email"])
	return emails


def add_user(firstname, lastname, username, email, password):
	global USERS

	if (username in USERS) or email in(get_emails(USERS_DATA)):
		print("Username or Email is already taken please enter another one.")
	else:
		USERS_DATA[username] = {
			"firstname" : firstname,
			"lastname" : lastname,
			"username" : username,
			"email" : email,	
			"password" : password
		}
		send_email_for_new_users(firstname, email)
		print(f"{firstname} {lastname} have been added")

		with open(f'./passwords_DATA/{username}_passwords.json', 'w') as f:
			json.dump({}, f, indent=4)

		print(USERS_DATA)
		USERS = get_Users(USERS_DATA)


def clear_USERS_DATA(mode):
	global USERS_DATA

	if mode == all:
		USERS_DATA = {}
		for file in os.listdir('passwords_DATA'):
			os.remove(f'./passwords_DATA/{file}')
		print("All users have been deleted")
		return USERS_DATA

	elif mode in(get_Users(USERS_DATA)):
		USERS_DATA.pop(mode)
		os.remove(f'./passwords_DATA/{mode}_passwords.json')
		print(f"{mode} have been removed")
		return USERS_DATA

	else: print("User you selected can't be found")


def login(username, password):
	if username not in(get_usernames(USERS_DATA)):
		print("Username not valid.")
		return False
	else:
		for user in get_Users(USERS_DATA):
			if USERS_DATA[user]["username"] == username and USERS_DATA[user]["password"] == password:
				return USERS_DATA[user]["email"]
			elif USERS_DATA[user]["username"] == username and USERS_DATA[user]["password"] != password: 
				return False


def add_password(username, app, link, password):
	temp = load_passwords(username)
	if app in list(load_passwords(username).keys()):
		print("A password for this app have already been added to your account.")
	else:
		temp[app] = {
			"appname" : app,
			"link" : link,
			"password" : password
		}
		
		send_email_new_password_added(USERS_DATA[username]["firstname"], app, USERS_DATA[username]["email"])

		with open(f"./passwords_DATA/{username}_passwords.json", "w") as f:
			json.dump(temp, f, indent=4)	

def load_passwords(username):
	return load_DATA(f"./passwords_DATA/{username}_passwords.json")



USERS_DATA = load_DATA("users_data.json")









# add_password("abdoessordo", "facebook", "facebook.com", "Tanger.2001")
add_password("abdoessordo", "gmail", "gmail.com", "Tanger.2001")

print(list(load_passwords("abdoessordo").keys()))


# if login("abdoessordo", "Tanger.2001"): print("logged in succesfully,", login("abdoessordo", "Tanger.2001"))


# add_user("Abdellah", "Essordo", "abdoessordo", "abdoessordo01@gmail.com", "Tanger.2001")
# add_user("Ayman", "Essordo", "ayman2272002", "ayman2272002@gmail.com", "Tanger.2002")


# clear_USERS_DATA("ayman2272002")
# clear_USERS_DATA(all)

# print("USERS :", get_Users(USERS_DATA))
# print("USERNAMES :", get_usernames(USERS_DATA))
# print("EMAILS :", get_emails(USERS_DATA))


with open("users_data.json", "w") as f:
	json.dump(USERS_DATA, f, indent=4)