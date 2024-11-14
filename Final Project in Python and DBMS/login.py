from tkinter import * #imports all classes and methods inside the tkinter module!
from tkinter import messagebox # imports message box (pop up!)
from PIL import ImageTk # Display Image

def login():
    if usernameEntry.get()=='' or passwordEntry.get()=='':
        messagebox.showerror('Error', 'Fields cannot be empty!')
    elif usernameEntry.get()=='Zomoi' and passwordEntry.get()=='HanniPham':
        messagebox.showinfo('Success', 'Welcome!')
        window.destroy() # login window will be closed!
        import cmms # once clicked ok, it will go to the next file.
    else:
        messagebox.showerror('Error', 'Please enter correct credentials!')

window = Tk() #tk for GUI!

window.geometry('1280x700+0+0') # size of window
window.title('Login System of Community Member Management System')


window.resizable(False,False)

backgroundImage = ImageTk.PhotoImage(file='bg.jpg') # linking the image

bgLabel = Label(window, image = backgroundImage) # to call the image
bgLabel.place(x = 0, y = 0 ) # size of the image

loginFrame = Frame(window, bg = 'white') # changes bg color to white (to match the bg)
loginFrame.place(x = 460, y = 150)

logoImage = PhotoImage(file='logo.png')

logoLabel = Label(loginFrame, image = logoImage)
logoLabel.grid(row = 0, column = 0, columnspan = 2, pady = 10) # logoLabel will now take 2 spaces.

usernameImage = PhotoImage (file='user.png')
usernameLabel = Label (loginFrame, image = usernameImage, text='Username', compound = LEFT
                       , font = ('times new roman',20,'bold'), bg = 'white')
usernameLabel.grid(row = 1, column = 0, pady = 10, padx = 5) # pady - vertical spaces

usernameEntry = Entry(loginFrame, font = ('times new roman',15,'bold'), bd = 2) # Creates entry field!
usernameEntry.grid(row = 1, column = 1, pady = 10, padx = 5) # padx - horizontal spaces


passwordImage = PhotoImage (file='password.png')
passwordLabel = Label (loginFrame, image = passwordImage, text='Password', compound = LEFT
                       , font = ('times new roman',20,'bold'), bg = 'white')
passwordLabel.grid(row = 2, column = 0, pady = 10, padx = 5) # pady - vertical spaces

passwordEntry = Entry(loginFrame, font = ('times new roman',15,'bold'), bd = 2)
passwordEntry.grid(row = 2, column = 1, pady = 10, padx = 5)

loginButton = Button(loginFrame, text = 'Login', font = ('times new roman',15,'bold'), width = 5, activebackground= 'gray'
                     , cursor = 'hand2', command = login)
loginButton.grid(row = 3, column = 1, pady = 5)

window.mainloop() 
# this mainloop is present inside the window class!
# will keep your window on a loop, hence the term, "mainloop" (WOW! :O)


