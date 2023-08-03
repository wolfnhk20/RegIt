from tkinter import *
from tkinter import messagebox
from PIL import ImageTk


def login():
    if emailEntry.get() == '' or passwordEntry.get() == '':
        messagebox.showerror(title='Error', message='Fields cannot be empty!')
    elif emailEntry.get() == 'ayush@regit.in' and passwordEntry.get() == 'Ayush@1234':
        messagebox.showinfo(title='Success', message='Login Successful!')
        root.destroy()
        import VehicleReg
    else:
        messagebox.showerror('Failed', 'Invalid Login details!')


root = Tk()  # create a window
root.geometry('1280x720+0+0')  # set size & position of window
# root.resizable(False, False)
root.title('Login - RegIt')

# setting background image
# bg = ImageTk.PhotoImage(file='main_bg.jpg')  # load image in bg
# bgLabel = Label(root, image=bg)  # set image inside a Label
# bgLabel.place(x=0, y=0)  # place the Label containing Image on the window

# creating Frame and setting size
loginFrame = Frame(root)
loginFrame.place(x=320, y=86)

# setting logo for login screen
loginLogo = PhotoImage(file='loginLogo-removebg-preview.png')  # load logo image in loginLogo
logoLabel = Label(loginFrame, image=loginLogo)
logoLabel.grid(row=0, column=0, columnspan=2, pady=10)

# adding login details
emailImage = PhotoImage(file='email.png')
loginEmail = Label(loginFrame, image=emailImage, text='Username', compound=LEFT
                   , font=('times new roman', 32, 'bold'))
loginEmail.grid(row=1, column=0, padx=10, pady=10)
emailEntry = Entry(loginFrame, font=('montserrat', 16), bd=5, width=30)
emailEntry.grid(row=1, column=1, pady=10)

passwordImage = PhotoImage(file='padlock.png')
loginPassword = Label(loginFrame, image=passwordImage, text='Password', compound=LEFT
                   , font=('times new roman', 32, 'bold'))
loginPassword.grid(row=2, column=0, padx=10, pady=10)
passwordEntry = Entry(loginFrame, font=('montserrat', 16), bd=5, width=30, show='*')
passwordEntry.grid(row=2, column=1, pady=10)

loginButton = Button(loginFrame, text='Login'
                     , font=('times new roman', 16, 'bold'), width=15
                     , bg='cornflowerblue', fg='white'
                     , activebackground='cornflowerblue', activeforeground='white'
                     ,cursor='hand2', command=login)
loginButton.grid(row=3, column=1)

# root.attributes('-fullscreen', True)
root.mainloop()  # keeping the window running
