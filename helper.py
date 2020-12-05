from tkinter import *



class MainMenu:
    def __init__(self, master):
        menubar = Menu(master)
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label='Exit', command=master.quit)
        menubar.add_cascade(label='File', menu=filemenu)
        master.config(menu=menubar)


class EntryWithPlaceholder(Entry):
    placeholder_input = ''
    def __init__(self, master, placeholder, color='grey'):
        super().__init__(master)

        placeholder_input = placeholder
        self.placeholder = placeholder
        self.placeholder_color = color
        self.default_fg_color = self['fg']
        if placeholder == "Password" or placeholder == "Create a password":
            self._is_password = True 
        else:self._is_password = False

        self.bind("<FocusIn>", self.on_focus_in)
        self.bind("<FocusOut>", self.on_focus_out)

        self.put_placeholder(self.placeholder)

    def put_placeholder(self, placeholder=placeholder_input):
        self.configure(show='')
        self.delete('0', 'end')
        self._state = 'placeholder'
        self.insert(0, self.placeholder)
        self['fg'] = self.placeholder_color


    def on_focus_in(self, event):
        if self._is_password:
          self.configure(show='*')

        if self._state == 'placeholder':
            self._state = ''
            self.delete('0', 'end')
            self['fg'] = self.default_fg_color


    def on_focus_out(self, event):
        if not self.get():
          if self._is_password:
            self.configure(show='')

          self._state = 'placeholder'
          self.insert(0, self.placeholder)
          self['fg'] = self.placeholder_color
          
