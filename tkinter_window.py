import tkinter as tk
from tkinter import filedialog

class Window:
    def __init__(self):

        self.username = ''
        self.password = ''
        self.folder_path = ''
        self.contest_url = ''

        root=tk.Tk()
        
    # setting the windows size
        root.geometry("800x800")
        root.title('HackerRank Contest Scraper')
        
    # declaring string variable for storing username, password and folder path
        username_var = tk.StringVar()
        password_var = tk.StringVar()
        folder_path_var = tk.StringVar()
        contest_url_var = tk.StringVar()

    # defining a function that will get the name and password and print them on the screen
        def submit():
            self.username = str(username_var.get())
            self.password = str(password_var.get())
            self.contest_url = str(contest_url_var.get())
            
            root.destroy()

        def browse_button():
            # Allow user to select a directory and store it folder_path
            filename = filedialog.askdirectory()
            self.folder_path = str(filename)

    # creating a label and entry for username
        username_label = tk.Label(root, text = 'Username', font=('calibre',10, 'bold'))
        username_entry = tk.Entry(root,textvariable = username_var, font=('calibre',10,'normal'))
        
    # creating a label and entry for password
        password_label = tk.Label(root, text = 'Password', font = ('calibre',10,'bold'))
        password_entry = tk.Entry(root, textvariable = password_var, font = ('calibre',10,'normal'), show = '*')

    # creating a label and entry for contest url
        contest_url_label = tk.Label(root, text = 'Contest URL', font = ('calibre',10,'bold'))
        contest_url_entry = tk.Entry(root, textvariable = contest_url_var, font = ('calibre',10,'normal'))

    # creating a button for access save folder path
        folder_path_entry = tk.Button(root, text = 'Choose save folder', command = browse_button)
    # creating a label to display folder path
        display_folder_path = tk.Label(root, textvariable = self.folder_path, font = ('calibre',10,'bold'))

    # creating a button using the widget that will call the submit function
        sub_btn=tk.Button(root, text = 'Submit', command = submit)

        username_label.grid(row = 0, column = 0)
        username_entry.grid(row = 0, column = 1)

        password_label.grid(row = 1, column = 0)
        password_entry.grid(row = 1, column = 1)

        contest_url_label.grid(row = 2, column = 0)
        contest_url_entry.grid(row = 2, column = 1)

        folder_path_entry.grid(row = 3, column = 0)
        display_folder_path.grid(row = 3, column = 3)

        sub_btn.grid(row = 4, column = 1)

        root.mainloop()