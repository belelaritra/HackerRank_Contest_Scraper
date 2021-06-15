import tkinter as tk
from tkinter import filedialog
from tkinter import *

class Window:
    def __init__(self):

        self.username = ''
        self.password = ''
        self.folder_path = ''
        self.contest_url = ''

        root=tk.Tk()
        
    # Windows size (Max & Min)
        root.geometry("410x175+0+0")
        root.minsize(410, 175)
        root.maxsize(410, 175)

    # Title
        root.title('HackerRank Contest Scraper')
        
    # String variables for username, password and folder path
        username_var = tk.StringVar()
        password_var = tk.StringVar()
        filename = tk.StringVar()
        contest_url_var = tk.StringVar()

    # defining a function that will get the name and password and print them on the screen
        def submit():
            self.username = str(username_var.get())
            self.password = str(password_var.get())
            self.contest_url = str(contest_url_var.get())

        # counts the number of blank strings
            count = [self.username, self.password, self.contest_url, self.folder_path].count('')
        # if a blank string is found
            if count >= 1:
                error_window = Toplevel(root)            
                # sets the geometry of toplevel
                error_window.geometry("200x100")
                error_window.minsize(200, 100)
                error_window.maxsize(200, 100)
                # A Label widget to show in toplevel
                Label(error_window, text ="Error!", padx = 30, pady = 90).pack()
            else:
                root.destroy()

        def browse_button():
            # Allow user to select a directory and store it folder_path
            filename = filedialog.askdirectory()
            self.folder_path = str(filename)
            pathlabel.config(text=filename)

#Frame
        F1 = LabelFrame(root, bd = 7, relief=GROOVE, bg="#2EC866")
        F1.place(x=0, y=0, width = 410, height=175)

# creating a label and entry for username
        username_label = tk.Label(F1, text = 'Username or Email', font=('arial',11, 'bold'),fg="BLACK",bg="#2EC866")
        username_label.grid(row = 0, column = 0,padx = 15, pady=5)

        username_entry = tk.Entry(F1,textvariable = username_var, font=('Courier',10,'normal'),bd=4, relief = SUNKEN)
        username_entry.grid(row = 0, column = 1,padx = 15, pady=5)

        username_entry.config(fg='grey')
        username_entry.insert(0,"Example: hackerrank@gmail.com")

# creating a label and entry for password
        password_label = tk.Label(F1, text = 'Password', font = ('arial',11,'bold'),fg="BLACK",bg="#2EC866")
        password_label.grid(row = 1, column = 0,padx = 10, pady=5)

        password_entry = tk.Entry(F1, textvariable = password_var, font = ('Courier',10,'normal'),bd=4, relief = SUNKEN, show = '*')
        password_entry.grid(row = 1, column = 1,padx = 10, pady=5)

        password_entry.config(fg='grey')
        password_entry.insert(0,"Example: 123456789")

# creating a label and entry for contest url
        contest_url_label = tk.Label(F1, text = 'Challenge URL', font = ('arial',11,'bold'),fg="BLACK",bg="#2EC866")
        contest_url_label.grid(row = 2, column = 0,padx = 10, pady=5)

        contest_url_entry = tk.Entry(F1, textvariable = contest_url_var, font = ('Courier',10,'normal'),bd=4, relief = SUNKEN)
        contest_url_entry.grid(row = 2, column = 1,padx = 10, pady=5)

        contest_url_entry.config(fg='grey')
        contest_url_entry.insert(0,"Example: www.google.com")

# creating a button for access save folder path
        folder_path_entry = tk.Button(F1, text = 'Choose Save Folder', command = browse_button,bd=4, font=("Arial", 10, "bold"))
        folder_path_entry.grid(row = 3, column = 0,padx = 20, pady=10)

        pathlabel = Label(root)
        pathlabel.pack(side=TOP, anchor=NW)

# creating a label to display folder path
        display_folder_path = tk.Label(F1, textvariable = self.folder_path, font = ('calibre',10,'bold'),bg="#2EC866")
        display_folder_path.grid(row = 3, column = 3,padx = 30, pady=10)

 # creating a button using the widget that will call the submit function
        sub_btn=tk.Button(F1, text = 'Submit', command = submit, bd=4, font=("Arial", 10, "bold"))
        sub_btn.grid(row = 3, column = 1,padx = 10, pady=10)
        
#Username Focus In
        def handle_focus_in_Username(_):
            if username_entry.get() == 'Example: hackerrank@gmail.com':
                username_entry.delete(0, tk.END)
                username_entry.insert(0, '')
                username_entry.config(fg='black')

#Password Focus In
        def handle_focus_in_pass(_):
            if password_entry.get() == 'Example: 123456789':
                password_entry.delete(0, tk.END)
                password_entry.insert(0, '')
                password_entry.config(fg='black')

#URL Focus
        def handle_focus_in_url(_):
            if contest_url_entry.get() == 'Example: www.google.com':
                contest_url_entry.delete(0, tk.END)
                contest_url_entry.insert(0, '')
                contest_url_entry.config(fg='black')
                
#Enter Button Focus wise invoke & focus
        def enterfocus(event):
            if str(root.focus_get()) == '.':
                username_entry.focus()
            elif str(root.focus_get()) == '.!labelframe.!entry':
                password_entry.focus()
            elif str(root.focus_get()) == '.!labelframe.!entry2':
                contest_url_entry.focus()
            elif str(root.focus_get()) == '.!labelframe.!entry3':
                folder_path_entry.focus()
            elif str(root.focus_get()) == '.!labelframe.!button':
                folder_path_entry.invoke()
                sub_btn.focus()
            elif str(root.focus_get()) == '.!labelframe.!button2':
                sub_btn.invoke()
                
#Entry Button Bind (Focus IN)
        username_entry.bind("<FocusIn>", handle_focus_in_Username)
        password_entry.bind("<FocusIn>", handle_focus_in_pass)
        contest_url_entry.bind("<FocusIn>", handle_focus_in_url)

#Enter Button Bind
        root.bind("<Return>", enterfocus)
# Esc Button Bind
        root.bind("<Escape>", lambda x: root.destroy())
    
        root.mainloop()
