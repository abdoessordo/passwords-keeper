from tkinter import *
import main
from helper import EntryWithPlaceholder, MainMenu

def login_btn(controller):
	global username
	username = SP_username.get() 
	user_name['text'] = username
	if main.login(username, SP_password.get()):
		controller.show_frame(PageOne)
		label['text'] = f'Welcome {main.USERS_DATA[username]["firstname"]}'

	else:
		SP_error_label['fg'] = 'red'

def logout_btn(controller):
	SP_error_label['fg'] = StartPage.bg_color
	SP_username.put_placeholder()
	SP_password.put_placeholder()
	controller.show_frame(StartPage)

def create_account():
	result = main.add_user(PT_first.get(), PT_last.get(), PT_username.get(), PT_email.get(), PT_password.get())
	PT_promp_user['text'] = result
	if result == main.add_user_results[0]:
		PT_promp_user['fg'] = 'red'
	else:
		PT_first.put_placeholder()
		PT_last.put_placeholder()
		PT_username.put_placeholder()
		PT_email.put_placeholder()
		PT_password.put_placeholder()

		PT_promp_user['fg'] = 'green'

def deleteacc(user, controller):
	logout_btn(controller)
	main.remove_USERS_DATA(user)

def add_password(controller):
	result = main.add_password(username, appname_entry.get(), applink_entry.get(), app_password_entry.get())
	PF_promp_user['text'] = result
	if result == main.add_password_results[0]:
		PF_promp_user['fg'] = 'red'
	else:
		appname_entry.put_placeholder()
		applink_entry.put_placeholder()
		app_password_entry.put_placeholder()

		PF_promp_user['fg'] = 'green'


class App(Tk):
	WIDTH = 600
	HEIGHT = 500
	def __init__(self, *args, **kwargs):
		Tk.__init__(self, *args, **kwargs)

		#SetupMenu
		MainMenu(self)

		#set up frame
		canvas = Canvas(self, height=self.HEIGHT, width=self.WIDTH).pack()
		container = Frame(self)
		container.place(x=0, y=0,relwidth=1, relheight=1)

		self.frames = {}

		for F in (StartPage, PageOne, PageTwo, PageThree, PageFour):
			frame = F(container, self)
			frame['bg'] = '#a8a4a3'
			self.frames[F] = frame
			frame.place(x=0, y=0, relwidth=1, relheight=1)

		self.show_frame(StartPage)

	def show_frame(self, context):
		frame = self.frames[context]
		frame.tkraise()

class StartPage(Frame):  #SP_ stands for StartPage
	bg_color = '#121212'
	def __init__(self, parent, controller):
		Frame.__init__(self, parent)

		holder = Frame(self, bg=StartPage.bg_color)
		holder.place(relx=0.2, rely=0.1, relwidth= 0.6, relheight=0.8)


		label = Label(holder, text='Passwords Keeper', bg=StartPage.bg_color, fg='white', font=('Helvetica', 16))
		label.pack(padx=10, pady=10)

		global SP_username, SP_password, SP_error_label
		SP_username = EntryWithPlaceholder(holder, 'Username')
		SP_username.pack()

		SP_password = EntryWithPlaceholder(holder, 'Password')
		SP_password.pack()
		

		SP_login_BTN = Button(holder, text='LOG IN', activebackground='orange',command = lambda:login_btn(controller))
		SP_login_BTN.pack()

		SP_error_label = Label(holder, text='Username or password not valid.', bg=StartPage.bg_color, fg=StartPage.bg_color)
		SP_error_label.pack()

		SP_signin = Label(holder, text="Don't have an account? SIGN IN", bg=StartPage.bg_color, fg='white')
		SP_signin.pack()

		SP_signin_BTN = Button(holder, text='SIGN IN', activebackground='orange',command = lambda:controller.show_frame(PageTwo))
		SP_signin_BTN.pack()

class PageOne(Frame):
	bg_color = '#a8a4a3'
	def __init__(self, parent, controller):
		Frame.__init__(self, parent)
		
		global label, user_name
		user_name = Label(self, text='', bg=PageOne.bg_color)
		label = Label(self, text='', bg=PageOne.bg_color)
		label.place(relx=0.4, rely=0)

		access_acc_BTN = Button(self, text='Access Account', activebackground='orange', command=lambda:controller.show_frame(PageThree))
		access_acc_BTN.place(relx=0.4, rely=0.25)

		delete_acc_BTN = Button(self, text='Delete account', bg='red', fg='white', command=lambda:deleteacc(user_name['text'], controller))
		delete_acc_BTN.place(relx=0.4, rely=0.45)

		PO_logout_BTN = Button(self,text='LOG OUT', activebackground='orange',  command = lambda:logout_btn(controller))
		PO_logout_BTN.place(relx=0.4, rely=0.9)

class PageTwo(Frame):
	bg_color = '#121212'
	def __init__(self, parent, controller):
		Frame.__init__(self, parent)

		holder = Frame(self, bg=StartPage.bg_color)
		holder.place(relx=0.2, rely=0.1, relwidth= 0.6, relheight=0.8)

		label = Label(holder, text='Sign up for a free account.', bg=PageTwo.bg_color, fg='white')
		label.pack()

		global PT_first, PT_last, PT_email, PT_password, PT_username, PT_promp_user
		PT_first = EntryWithPlaceholder(holder, "Enter your firstname")
		PT_first.place(relx=0.3, rely=0.1)
		
		PT_last = EntryWithPlaceholder(holder, "Enter your lastname")
		PT_last.place(relx=0.3, rely=0.2)

		PT_email = EntryWithPlaceholder(holder, 'Email')
		PT_email.place(relx=0.3, rely=0.3)

		PT_password = EntryWithPlaceholder(holder, "Create a password")
		PT_password.place(relx=0.3, rely=0.4)

		PT_username = EntryWithPlaceholder(holder, "What should we call you?")
		PT_username.place(relx=0.3, rely=0.5)

		PT_add_account = Button(holder, text="Create account", activebackground='orange',  command = lambda: create_account())
		PT_add_account.place(relx=0.3, rely=0.6)

		PT_promp_user = Label(holder, text='', bg=PageTwo.bg_color, fg=PageTwo.bg_color)
		PT_promp_user.place(relx=0.1, rely=0.7)

		PT_hp_BTN = Button(holder,text='Home Page', activebackground='orange',  command = lambda:controller.show_frame(StartPage))
		PT_hp_BTN.place(relx=0.15, rely=0.9)

class PageThree(Frame):
	bg_color = '#a8a4a3'
	def __init__(self, parent, controller):
		Frame.__init__(self, parent)

		label = Label(self, text="Your Passwords", bg=PageThree.bg_color)
		label.place(relx=0.4, rely=0)

		# holder = Frame(self, bg=StartPage.bg_color)
		# holder.place(relx=0.15, rely=0.1, relwidth= 0.7, relheight=0.8)

		# appname_label = Label(holder, text='', bg= StartPage.bg_color, fg='white')
		# appname_label  

		# applink_label = Label(holder, text='', bg= StartPage.bg_color, fg='white')

		# app_password_label =  Label(holder, text='', bg= StartPage.bg_color, fg='white')

		account_BTN = Button(self, text="Back", activebackground='orange', command=lambda:controller.show_frame(PageOne))
		account_BTN.place(relx=0.2, rely=0.9)

		add_password_BTN = Button(self, text="Add Password", activebackground='orange', command=lambda:controller.show_frame(PageFour))
		add_password_BTN.place(relx=0.6, rely=0.9)

class PageFour(Frame):
	def __init__(self, parent, controller):
		Frame.__init__(self, parent)

		label = Label(self, text="Add a Passwords", bg=PageThree.bg_color, fg='white')
		label.place(relx=0.4, rely=0)

		holder = Frame(self, bg=StartPage.bg_color)
		holder.place(relx=0.2, rely=0.1, relwidth= 0.6, relheight=0.8)

		global appname_entry, applink_entry, app_password_entry, PF_promp_user, add_password_BTN

		appname_entry = EntryWithPlaceholder(holder, 'App Name')
		appname_entry.place(relx=0.3, rely=0.1)
		
		applink_entry = EntryWithPlaceholder(holder, 'App Link')
		applink_entry.place(relx=0.3, rely=0.3)
		
		app_password_entry = EntryWithPlaceholder(holder, 'Enter Password')
		app_password_entry.place(relx=0.3, rely=0.5)

		PF_promp_user = Label(holder, text='', bg=PageTwo.bg_color, fg=PageTwo.bg_color)
		PF_promp_user.place(relx=0.1, rely=0.7)

		add_password_BTN = Button(holder, text='Add Password', command=lambda:add_password(controller))
		add_password_BTN.place(relx=0.4, rely=0.9)

		back_BTN = Button(self, text='Back', command=lambda:controller.show_frame(PageThree))
		back_BTN.place(relx=0.2, rely=0.95)





app = App()
app.mainloop()