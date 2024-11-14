from tkinter import *
import time # for clock() 
import ttkthemes # pip install
from tkinter import ttk, messagebox # helps in applying theme on button 
import pymysql
# Functionality Part : 

def iexit():
  result = messagebox.askyesno('Confirm','Do you want to exit?')
  if result :
    root.destroy()
  else:
    pass

def update_member():

  def update_data():
    query = 'update member set name=%s, mobile=%s, email=%s, gender=%s, address=%s, age=%s, volunteer_hours=%s, activity=%s, volunteer_role=%s, added_date=%s, added_time=%s where id =%s'
    mycursor.execute(query,(nameEntry.get(), mobilenoEntry.get(), 
    emailEntry.get(), genderEntry.get(), addressEntry.get(), ageEntry.get(),
    vhEntry.get(), activityEntry.get(), vrEntry.get(), date, currenttime,idEntry.get()))
    con.commit()
    messagebox.showinfo('Success',f'ID {idEntry.get()} is modified successfully!', parent = update_window)
    update_window.destroy()
    show_member()


    update_window = Toplevel()
    update_window.title('Update Member')
    update_window.grab_set() # you can't type to anything aside from the window you opened. 
    update_window.resizable(False,False)
    idLabel = Label(update_window,text = 'ID', font =('times new roman',20,'bold'))
    idLabel.grid(row = 0, column = 0, padx = 30, pady = 15, sticky = W) # sticky to make it align to left broski
    idEntry = Entry(update_window, font = ('roman', 15, 'bold'), width = 24)
    idEntry.grid(row = 0, column = 1, pady = 15, padx = 10)

    nameLabel = Label(update_window,text = 'Name', font =('times new roman',20,'bold'))
    nameLabel.grid(row = 1, column = 0, padx = 30, pady = 10, sticky = W)
    nameEntry = Entry(update_window, font = ('roman', 15, 'bold'), width = 24)
    nameEntry.grid(row = 1, column = 1, pady = 10, padx = 10)

    mobilenoLabel = Label(update_window,text = 'Mobile No.', font =('times new roman',20,'bold'))
    mobilenoLabel.grid(row = 2, column = 0, padx = 30, pady = 10, sticky = W)
    mobilenoEntry = Entry(update_window, font = ('roman', 15, 'bold'), width = 24)
    mobilenoEntry.grid(row = 2, column = 1, pady = 10, padx = 10)

    emailLabel = Label(update_window,text = 'Email', font =('times new roman',20,'bold'))
    emailLabel.grid(row = 3, column = 0, padx = 30, pady = 10, sticky = W)
    emailEntry = Entry(update_window, font = ('roman', 15, 'bold'), width = 24)
    emailEntry.grid(row = 3, column = 1, pady = 10, padx = 10)

    genderLabel = Label(update_window,text = 'Gender', font =('times new roman',20,'bold'))
    genderLabel.grid(row = 4, column = 0, padx = 30, pady = 10, sticky = W)
    genderEntry = Entry(update_window, font = ('roman', 15, 'bold'), width = 24)
    genderEntry.grid(row = 4, column = 1, pady = 10, padx = 10)

    addressLabel = Label(update_window,text = 'Address', font =('times new roman',20,'bold'))
    addressLabel.grid(row = 5, column = 0, padx = 30, pady = 10, sticky = W)
    addressEntry = Entry(update_window, font = ('roman', 15, 'bold'), width = 24)
    addressEntry.grid(row = 5, column = 1, pady = 10, padx = 10)

    ageLabel = Label(update_window,text = 'Age', font =('times new roman',20,'bold'))
    ageLabel.grid(row = 6, column = 0, padx = 30, pady = 10, sticky = W)
    ageEntry = Entry(update_window, font = ('roman', 15, 'bold'), width = 24)
    ageEntry.grid(row = 6, column = 1, pady = 10, padx = 10)

    vhLabel = Label(update_window,text = 'Volunteer Hours', font =('times new roman',20,'bold'))
    vhLabel.grid(row = 7, column = 0, padx = 30, pady = 10, sticky = W)
    vhEntry = Entry(update_window, font = ('roman', 15, 'bold'), width = 24)
    vhEntry.grid(row = 7, column = 1, pady = 10, padx = 10)

    activityLabel = Label(update_window,text = 'Activity', font =('times new roman',20,'bold'))
    activityLabel.grid(row = 8, column = 0, padx = 30, pady = 10, sticky = W)
    activityEntry = Entry(update_window, font = ('roman', 15, 'bold'), width = 24)
    activityEntry.grid(row = 8, column = 1, pady = 10, padx = 10)

    vrLabel = Label(update_window,text = 'Volunteer Role', font =('times new roman',20,'bold'))
    vrLabel.grid(row = 9, column = 0, padx = 30, pady = 10, sticky = W)
    vrEntry = Entry(update_window, font = ('roman', 15, 'bold'), width = 24)
    vrEntry.grid(row = 9, column = 1, pady = 10, padx = 10)

    update_member_button = ttk.Button(update_window, text = 'UPDATE MEMBER', command = update_data) # BUTTONS YO!!
    update_member_button.grid(row = 10, columnspan = 2, pady = 10)

    indexing = memberTable.focus() # selected data
    content = memberTable.item(indexing) # will give us the content
    listdata = content['values'] # all value selected from specific ID
    idEntry.insert(0, listdata[0])
    nameEntry.insert(0, listdata[1])
    mobilenoEntry.insert(0, listdata[2])
    emailEntry.insert(0, listdata[3])
    genderEntry.insert(0, listdata[4])
    addressEntry.insert(0, listdata[5])
    ageEntry.insert(0, listdata[6])
    vhEntry.insert(0, listdata[7])
    activityEntry.insert(0, listdata[8])
    vrEntry.insert(0, listdata[9])



def show_member():
    query = 'select * from member'
    mycursor.execute(query)
    fetched_data = mycursor.fetchall()
    memberTable.delete(*memberTable.get_children())
    for data in fetched_data:
      memberTable.insert('', END, values = data)


def delete_member():
    indexing = memberTable.focus()
    print(indexing)
    content = memberTable.item(indexing) # will give complete content corresponding to that index
    content_id = content['values'][0] # value is the key, (the complete row), [0] to access ID only.
    query = 'delete from member where id=%s'
    mycursor.execute(query,content_id) 
    con.commit()
    messagebox.showinfo('Deleted',f'ID {content_id} is deleted successfully!')
    query = 'select * from member'
    mycursor.execute(query)
    fetched_data = mycursor.fetchall()
    memberTable.delete(*memberTable.get_children())
    for data in fetched_data:
      memberTable.insert('', END, values = data)


def search_member():
    def search_data():
        query = '''
                SELECT * FROM member 
                WHERE id=%s OR name=%s OR mobile=%s OR email=%s OR gender=%s 
                OR address=%s OR age=%s OR volunteer_hours=%s OR activity=%s OR volunteer_role=%s
                '''
        mycursor.execute(query,(
                idEntry.get(), nameEntry.get(), mobilenoEntry.get(), emailEntry.get(),
                genderEntry.get(), addressEntry.get(), ageEntry.get(),
                vhEntry.get(), activityEntry.get(), vrEntry.get())) # Whatever ID you'll get %s will replace
        memberTable.delete(*memberTable.get_children())
        fetched_data = mycursor.fetchall()
        for data in fetched_data:
          memberTable.insert('', END, values = data)

    search_window = Toplevel()
    search_window.title('Search Student')
    search_window.grab_set() # you can't type to anything aside from the window you opened. 
    search_window.resizable(False,False)
    idLabel = Label(search_window,text = 'ID', font =('times new roman',20,'bold'))
    idLabel.grid(row = 0, column = 0, padx = 30, pady = 15, sticky = W) # sticky to make it align to left broski
    idEntry = Entry(search_window, font = ('roman', 15, 'bold'), width = 24)
    idEntry.grid(row = 0, column = 1, pady = 15, padx = 10)

    nameLabel = Label(search_window,text = 'Name', font =('times new roman',20,'bold'))
    nameLabel.grid(row = 1, column = 0, padx = 30, pady = 10, sticky = W)
    nameEntry = Entry(search_window, font = ('roman', 15, 'bold'), width = 24)
    nameEntry.grid(row = 1, column = 1, pady = 10, padx = 10)

    mobilenoLabel = Label(search_window,text = 'Mobile No.', font =('times new roman',20,'bold'))
    mobilenoLabel.grid(row = 2, column = 0, padx = 30, pady = 10, sticky = W)
    mobilenoEntry = Entry(search_window, font = ('roman', 15, 'bold'), width = 24)
    mobilenoEntry.grid(row = 2, column = 1, pady = 10, padx = 10)

    emailLabel = Label(search_window,text = 'Email', font =('times new roman',20,'bold'))
    emailLabel.grid(row = 3, column = 0, padx = 30, pady = 10, sticky = W)
    emailEntry = Entry(search_window, font = ('roman', 15, 'bold'), width = 24)
    emailEntry.grid(row = 3, column = 1, pady = 10, padx = 10)

    genderLabel = Label(search_window,text = 'Gender', font =('times new roman',20,'bold'))
    genderLabel.grid(row = 4, column = 0, padx = 30, pady = 10, sticky = W)
    genderEntry = Entry(search_window, font = ('roman', 15, 'bold'), width = 24)
    genderEntry.grid(row = 4, column = 1, pady = 10, padx = 10)

    addressLabel = Label(search_window,text = 'Address', font =('times new roman',20,'bold'))
    addressLabel.grid(row = 5, column = 0, padx = 30, pady = 10, sticky = W)
    addressEntry = Entry(search_window, font = ('roman', 15, 'bold'), width = 24)
    addressEntry.grid(row = 5, column = 1, pady = 10, padx = 10)

    ageLabel = Label(search_window,text = 'Age', font =('times new roman',20,'bold'))
    ageLabel.grid(row = 6, column = 0, padx = 30, pady = 10, sticky = W)
    ageEntry = Entry(search_window, font = ('roman', 15, 'bold'), width = 24)
    ageEntry.grid(row = 6, column = 1, pady = 10, padx = 10)

    vhLabel = Label(search_window,text = 'Volunteer Hours', font =('times new roman',20,'bold'))
    vhLabel.grid(row = 7, column = 0, padx = 30, pady = 10, sticky = W)
    vhEntry = Entry(search_window, font = ('roman', 15, 'bold'), width = 24)
    vhEntry.grid(row = 7, column = 1, pady = 10, padx = 10)

    activityLabel = Label(search_window,text = 'Activity', font =('times new roman',20,'bold'))
    activityLabel.grid(row = 8, column = 0, padx = 30, pady = 10, sticky = W)
    activityEntry = Entry(search_window, font = ('roman', 15, 'bold'), width = 24)
    activityEntry.grid(row = 8, column = 1, pady = 10, padx = 10)

    vrLabel = Label(search_window,text = 'Volunteer Role', font =('times new roman',20,'bold'))
    vrLabel.grid(row = 9, column = 0, padx = 30, pady = 10, sticky = W)
    vrEntry = Entry(search_window, font = ('roman', 15, 'bold'), width = 24)
    vrEntry.grid(row = 9, column = 1, pady = 10, padx = 10)

    search_member_button = ttk.Button(search_window, text = 'SEARCH MEMBER', command = search_data) # BUTTONS YO!!
    search_member_button.grid(row = 10, columnspan = 2, pady = 10)
  

def add_member():
   def add_data():
      if idEntry.get() == '' or nameEntry.get()=='' or mobilenoEntry.get()== '' or emailEntry.get()=='' or genderEntry.get() == '' or addressEntry.get() == '' or ageEntry.get() == '' or vhEntry.get() == '' or activityEntry.get() == '' or vrEntry.get() == '':
        messagebox.showerror('Error', 'All Fields are required!', parent = add_window) # This will appear if one of the fields are empy!

      else:
        currentdate = time.strftime('%d/%m/%Y')
        currenttime = time.strftime('%H:%M:%S')
        try:
          query ='insert into member values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
          mycursor.execute(query,(idEntry.get(),nameEntry.get(),mobilenoEntry.get(),emailEntry.get(),
                          genderEntry.get(),addressEntry.get(),ageEntry.get(),vhEntry.get(), activityEntry.get(), 
                          vrEntry.get(),currentdate,currenttime))
          con.commit()
          result = messagebox.askyesno('Confirm','Data added successfully. Do you want to clean the form?', parent = add_window)
          if result:
            idEntry.delete(0, END)
            nameEntry.delete(0, END)
            mobilenoEntry.delete(0, END)
            emailEntry.delete(0, END)
            genderEntry.delete(0, END)
            addressEntry.delete(0, END)
            ageEntry.delete(0, END)
            vhEntry.delete(0, END)
            activityEntry.delete(0, END)
            vrEntry.delete(0, END)
          else: 
            pass
        except:
          messagebox.showerror('Error', 'ID cannot be repeated', parent = add_window)
          return 

      query = 'select * from member' # command to call all the data
      mycursor.execute(query) # executes the query
      fetched_data = mycursor.fetchall() # receives the called data
      memberTable.delete(*memberTable.get_children()) # delete the previous called data 
      for data in fetched_data: # this converts the data into lists.
          memberTable.insert('', END, values = data) # inserts the data inside


   add_window = Toplevel()
   add_window.grab_set() # you can't type to anything aside from the window you opened. 
   add_window.resizable(False,False)
   idLabel = Label(add_window,text = 'ID', font =('times new roman',20,'bold'))
   idLabel.grid(row = 0, column = 0, padx = 30, pady = 15, sticky = W) # sticky to make it align to left broski
   idEntry = Entry(add_window, font = ('roman', 15, 'bold'), width = 24)
   idEntry.grid(row = 0, column = 1, pady = 15, padx = 10)

   nameLabel = Label(add_window,text = 'Name', font =('times new roman',20,'bold'))
   nameLabel.grid(row = 1, column = 0, padx = 30, pady = 10, sticky = W)
   nameEntry = Entry(add_window, font = ('roman', 15, 'bold'), width = 24)
   nameEntry.grid(row = 1, column = 1, pady = 10, padx = 10)

   mobilenoLabel = Label(add_window,text = 'Mobile No.', font =('times new roman',20,'bold'))
   mobilenoLabel.grid(row = 2, column = 0, padx = 30, pady = 10, sticky = W)
   mobilenoEntry = Entry(add_window, font = ('roman', 15, 'bold'), width = 24)
   mobilenoEntry.grid(row = 2, column = 1, pady = 10, padx = 10)

   emailLabel = Label(add_window,text = 'Email', font =('times new roman',20,'bold'))
   emailLabel.grid(row = 3, column = 0, padx = 30, pady = 10, sticky = W)
   emailEntry = Entry(add_window, font = ('roman', 15, 'bold'), width = 24)
   emailEntry.grid(row = 3, column = 1, pady = 10, padx = 10)

   genderLabel = Label(add_window,text = 'Gender', font =('times new roman',20,'bold'))
   genderLabel.grid(row = 4, column = 0, padx = 30, pady = 10, sticky = W)
   genderEntry = Entry(add_window, font = ('roman', 15, 'bold'), width = 24)
   genderEntry.grid(row = 4, column = 1, pady = 10, padx = 10)

   addressLabel = Label(add_window,text = 'Address', font =('times new roman',20,'bold'))
   addressLabel.grid(row = 5, column = 0, padx = 30, pady = 10, sticky = W)
   addressEntry = Entry(add_window, font = ('roman', 15, 'bold'), width = 24)
   addressEntry.grid(row = 5, column = 1, pady = 10, padx = 10)

   ageLabel = Label(add_window,text = 'Age', font =('times new roman',20,'bold'))
   ageLabel.grid(row = 6, column = 0, padx = 30, pady = 10, sticky = W)
   ageEntry = Entry(add_window, font = ('roman', 15, 'bold'), width = 24)
   ageEntry.grid(row = 6, column = 1, pady = 10, padx = 10)

   vhLabel = Label(add_window,text = 'Volunteer Hours', font =('times new roman',20,'bold'))
   vhLabel.grid(row = 7, column = 0, padx = 30, pady = 10, sticky = W)
   vhEntry = Entry(add_window, font = ('roman', 15, 'bold'), width = 24)
   vhEntry.grid(row = 7, column = 1, pady = 10, padx = 10)

   activityLabel = Label(add_window,text = 'Activity', font =('times new roman',20,'bold'))
   activityLabel.grid(row = 8, column = 0, padx = 30, pady = 10, sticky = W)
   activityEntry = Entry(add_window, font = ('roman', 15, 'bold'), width = 24)
   activityEntry.grid(row = 8, column = 1, pady = 10, padx = 10)

   vrLabel = Label(add_window,text = 'Volunteer Role', font =('times new roman',20,'bold'))
   vrLabel.grid(row = 9, column = 0, padx = 30, pady = 10, sticky = W)
   vrEntry = Entry(add_window, font = ('roman', 15, 'bold'), width = 24)
   vrEntry.grid(row = 9, column = 1, pady = 10, padx = 10)

   add_member_button = ttk.Button(add_window, text = 'ADD MEMBER', command = add_data) # BUTTONS YO!!
   add_member_button.grid(row = 10, columnspan = 2, pady = 10)

def connect_database():
    def connect():
        global mycursor, con # make variable used in other functions!
        try: # IF RIGHT THEN THIS WILL EXECUTE
            con = pymysql.connect(host = hostEntry.get(), user = usernameEntry.get(), password = passwordEntry.get())
        # con variable will help in executing the commands that we type in sql.
            mycursor = con.cursor()
            messagebox.showinfo('Success','Database Connection is successful!',parent = connectWindow)
        except: # IF WRONG THEN THIS WILL EXECUTE
           messagebox.showerror('Error','Invalid Details', parent = connectWindow)
           return
        try:
            query = 'create database communitymanagementsystem'
            mycursor.execute(query)
            query = 'use communitymanagementsystem'
            mycursor.execute(query)
            query = '''
                CREATE TABLE member(
                id INT NOT NULL PRIMARY KEY,
                name VARCHAR(30),
                mobile VARCHAR(15),
                email VARCHAR(30),
                gender VARCHAR(20),
                address VARCHAR(50),
                age INT,
                volunteer_hours INT,
                activity VARCHAR(50),
                volunteer_role VARCHAR(30),
                added_date VARCHAR(50),
                added_time VARCHAR(50))'''
            mycursor.execute(query)
        except:
           query='use communitymanagementsystem'
           mycursor.execute(query) 
        messagebox.showinfo('Success', 'Database Connection is successsful', parent = connectWindow)
        connectWindow.destroy()
        addmemberButton.config(state = NORMAL)
        searchmemberButton.config(state = NORMAL)
        updatememberButton.config(state = NORMAL)
        showmemberButton.config(state = NORMAL)
        deletememberButton.config(state = NORMAL)
            


    connectWindow = Toplevel()
    connectWindow.grab_set()
    connectWindow.geometry('470x250+730+230') # size
    connectWindow.title('Database Connection') 
    connectWindow.resizable(False,False)

    hostnameLabel = Label(connectWindow, text = 'Host Name', font =('arial',20,'bold'), fg = 'peru')
    hostnameLabel.grid(row = 0, column = 0, padx = 20)

    hostEntry = Entry(connectWindow, font=('roman', 15, 'bold'), bd = 2)
    hostEntry.grid(row = 0, column = 1, padx = 40, pady = 20)

    usernameLabel = Label(connectWindow, text = 'User Name', font =('arial',20,'bold'), fg = 'peru')
    usernameLabel.grid(row = 1, column = 0, padx = 20)    

    usernameEntry = Entry(connectWindow, font=('roman', 15, 'bold'), bd = 2)
    usernameEntry.grid(row = 1, column = 1, padx = 40, pady = 20)

    passwordLabel = Label(connectWindow, text = 'Password', font =('arial',20,'bold'), fg = 'peru')
    passwordLabel.grid(row = 2, column = 0, padx = 20)    

    passwordEntry = Entry(connectWindow, font=('roman', 15, 'bold'), bd = 2)
    passwordEntry.grid(row = 2, column = 1, padx = 40, pady = 20)

    connectButton = ttk.Button(connectWindow, text = 'CONNECT', command = connect)
    connectButton.grid(row = 3, columnspan = 2)



count = 0
text = ''
def slider():
  global text,count
  if count == len(title): # once reaches the lenght (number of letters)
    count = 0
    text = '' # will repeat
  text = text+title[count] #C
  sliderLabel.config(text = text)
  count+= 1
  sliderLabel.after(200,slider)

def clock():
  global date, currenttime
  date = time.strftime('%d/%m/%Y') # date
  currenttime = time.strftime('%H:%M:%S') # time
  datetimeLabel.config(text = f"   Date: {date}\nTime: {currenttime}")  
  datetimeLabel.after(1000,clock) # update something after some time!

# GUI Part : 
root = ttkthemes.ThemedTk() # One advantage of using this class is that we can apply theme on buttons.

root.get_themes()

root.set_theme('radiance')

root.geometry('1174x680+0+0')
root.resizable(False,False)
root.title('Community Management System')

datetimeLabel = Label(root,font=('times new roman',18,'bold'), fg = "peru")
datetimeLabel.place(x = 5, y = 5)
clock()

title = "Community Management System" # title[count] = C when count is 0
sliderLabel = Label(root,font=('arial',28,'italic bold'), width = 30, fg = "peru")
sliderLabel.place(x = 200, y = 0)
slider()

connectButton = ttk.Button(root, text = "Connect Database", command = connect_database)
connectButton.place(x= 980, y = 0)

# LEFT!!

leftFrame = Frame(root)
leftFrame.place(x = 50, y = 80, width = 300, height = 600)

logo_image = PhotoImage(file='community.png')
logo_Label = Label(leftFrame, image = logo_image)
logo_Label.grid(row = 0, column = 0) # grid will make it more easier (instead of putting x and y values)

addmemberButton = ttk.Button(leftFrame, text='Add Member', width = 25, state = DISABLED, command = add_member)
addmemberButton.grid(row = 1, column = 0, pady = 20)

searchmemberButton = ttk.Button(leftFrame, text='Search Member', width = 25, state = DISABLED, command = search_member)
searchmemberButton.grid(row = 2, column = 0, pady = 15)

deletememberButton = ttk.Button(leftFrame, text='Delete Member', width = 25, state = DISABLED, command = delete_member)
deletememberButton.grid(row = 3, column = 0, pady = 15)

updatememberButton = ttk.Button(leftFrame, text='Update Member', width = 25, state = DISABLED, command = update_member)
updatememberButton.grid(row = 4, column = 0, pady = 15)

showmemberButton = ttk.Button(leftFrame, text='Show Member', width = 25, state = DISABLED, command = show_member)
showmemberButton.grid(row = 5, column = 0, pady = 15)

exitButton = ttk.Button(leftFrame, text='Exit', width = 25, command = iexit)
exitButton.grid(row = 6, column = 0, pady = 15)

# RIGHT!!

rightFrame = Frame(root)
rightFrame.place(x = 350, y = 80, width = 820, height = 600)

scrollBarX = Scrollbar(rightFrame, orient = HORIZONTAL) #Horizontal Scrollbar
scrollBarY = Scrollbar(rightFrame, orient = VERTICAL) #Vertical Scrollbar


memberTable = ttk.Treeview(rightFrame,columns = ('ID', 'Name', 'Mobile No.', 'Email', 'Gender', 'Address', 'Age', 
                                   'Volunteer Hours','Activity','Volunteer Role',
                                   'Added Date','Added Time'), # Column Lists
                                   xscrollcommand = scrollBarX.set, yscrollcommand = scrollBarY.set) # scroll bar 


scrollBarX.config(command = memberTable.xview) # to actually view and make scrollbar function.
scrollBarY.config(command = memberTable.yview) # to actually view and make scrollbar function.

scrollBarX.pack(side = BOTTOM, fill = X)
scrollBarY.pack(side = RIGHT, fill = Y)

memberTable.pack(fill=BOTH, expand = 1) # Displays the table

memberTable.heading('ID', text = 'ID')
memberTable.heading('Name', text = 'Name')
memberTable.heading('Mobile No.', text = 'Mobile No.')
memberTable.heading('Email', text = 'Email')
memberTable.heading('Gender', text = 'Gender')
memberTable.heading('Address', text = 'Address')
memberTable.heading('Age', text = 'Age')
memberTable.heading('Volunteer Hours', text = 'Volunteer Hours')
memberTable.heading('Activity', text = 'Activity')
memberTable.heading('Volunteer Role', text = 'Volunteer Role')
memberTable.heading('Added Date', text = 'Added Date')
memberTable.heading('Added Time', text = 'Added Time')



memberTable.config(show = 'headings') # Displays the heading (column), in order.

root.mainloop() 
