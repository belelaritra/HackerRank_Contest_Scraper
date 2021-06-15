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
        root.geometry("400x175+0+0")
        root.minsize(400, 175)
        root.maxsize(400, 175)

    # Esc & Enter Button Bind
        root.bind("<Escape>", lambda x: root.destroy())
        root.bind('<Return>', lambda event=None: sub_btn.invoke())

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

        #Frame
        F1 = LabelFrame(root, bd = 7, relief=GROOVE, bg="#2EC866")
        F1.place(x=0, y=0, width = 400, height=175)

    # creating a label and entry for username
        username_label = tk.Label(root, text = 'Username or Email', font=('arial',11, 'bold'),fg="BLACK",bg="#2EC866")
        username_label.grid(row = 0, column = 0,padx = 10, pady=9)

        username_entry = tk.Entry(root,textvariable = username_var, font=('Courier',10,'normal'),bd=4, relief = SUNKEN)
        username_entry.grid(row = 0, column = 1,padx = 10, pady=9)
    # creating a label and entry for password
        password_label = tk.Label(root, text = 'Password', font = ('arial',11,'bold'),fg="BLACK",bg="#2EC866")
        password_label.grid(row = 1, column = 0,padx = 10, pady=6)

        password_entry = tk.Entry(root, textvariable = password_var, font = ('Courier',10,'normal'),bd=4, relief = SUNKEN, show = '*')
        password_entry.grid(row = 1, column = 1,padx = 10, pady=6)

    # creating a label and entry for contest url
        contest_url_label = tk.Label(root, text = 'Challenge URL', font = ('arial',11,'bold'),fg="BLACK",bg="#2EC866")
        contest_url_label.grid(row = 2, column = 0,padx = 10, pady=7)

        contest_url_entry = tk.Entry(root, textvariable = contest_url_var, font = ('Courier',10,'normal'),bd=4, relief = SUNKEN)
        contest_url_entry.grid(row = 2, column = 1,padx = 10, pady=7)

    # creating a button for access save folder path
        folder_path_entry = tk.Button(root, text = 'Choose Save Folder', command = browse_button,bd=4, font=("Arial", 10, "bold"))
        folder_path_entry.grid(row = 3, column = 0,padx = 20, pady=8)

    # creating a label to display folder path
        display_folder_path = tk.Label(root, textvariable = self.folder_path, font = ('calibre',10,'bold'))
        display_folder_path.grid(row = 3, column = 3,padx = 30, pady=10)
    # creating a button using the widget that will call the submit function
        sub_btn=tk.Button(root, text = 'Submit', command = submit, bd=4, font=("Arial", 10, "bold"))
        sub_btn.grid(row = 3, column = 1,padx = 10, pady=8)
    
        root.mainloop()
