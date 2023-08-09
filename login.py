from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
from tkinter import ttk
import ttkthemes


def login():
    if emailEntry.get() == '' or passwordEntry.get() == '':
        messagebox.showerror(title='Error', message='Fields cannot be empty!')
    elif emailEntry.get() == 'ayush@regit.in' and passwordEntry.get() == 'Ayush@1234':
        messagebox.showinfo(title='Success', message='Login Successful!')
        root.destroy()
        import VehicleReg
    else:
        messagebox.showerror('Failed', 'Invalid Login details!')


def slider():
    global count, s
    titleLabel.config(text=f'{s}{str[count]}')
    s = s + str[count]
    count = count + 1
    titleLabel.after(1000, slider)


# GUI
root = ttkthemes.ThemedTk(theme='equilux')  # create a window
root.geometry('1230x620+20+10')  # set size & position of window
root.resizable(False, False)
root.title('Login - RegIt')
root['background'] = '#2a2a2a'
menu_image = PhotoImage(file='menu_icon.png')
root.iconphoto(False, menu_image)

# setting background image
# bg = ImageTk.PhotoImage(file='main_bg.jpg')  # load image in bg
# bgLabel = Label(root, image=bg)  # set image inside a Label
# bgLabel.place(x=0, y=0)  # place the Label containing Image on the window

str = 'RegIt'
s = ""
count = 0

titleLabel = Label(root
                   , font=('sans-serif', 40, 'bold italic'), bg='#2a2a2a', fg='#a6a6a6')
titleLabel.place(x=545, y=0)
slider()

# creating Frame and setting size
loginFrame = Frame(root)
loginFrame.place(x=290, y=66)
loginFrame['background'] = '#2a2a2a'

# setting logo for login screen
loginLogo = PhotoImage(file='loginLogo-removebg-preview.png')  # load logo image in loginLogo
logoLabel = Label(loginFrame, image=loginLogo, bg='#2a2a2a', fg='#a6a6a6')
logoLabel.grid(row=0, column=0, columnspan=2, pady=10)

# adding login details
emailImage = PhotoImage(file='email.png')
loginEmail = Label(loginFrame, image=emailImage, text='Username', compound=LEFT
                   , font=('sans-serif', 32, 'bold'), bg='#2a2a2a', fg='#a6a6a6')
loginEmail.grid(row=1, column=0, padx=10, pady=10)
emailEntry = ttk.Entry(loginFrame, font=('sans-serif', 16), width=30)
emailEntry.grid(row=1, column=1, pady=10)

passwordImage = PhotoImage(file='padlock.png')
loginPassword = Label(loginFrame, image=passwordImage, text='Password', compound=LEFT
                   , font=('sans-serif', 32, 'bold'), bg='#2a2a2a', fg='#a6a6a6')
loginPassword.grid(row=2, column=0, padx=10, pady=10)
passwordEntry = ttk.Entry(loginFrame, font=('montserrat', 16), width=30, show='*')
passwordEntry.grid(row=2, column=1, pady=10)

loginButtonStyle = ttk.Style()
loginButton = ttk.Button(loginFrame, text='Login'
                         , cursor='hand2', command=login, width=10, style='login.TButton')
loginButton.grid(row=3, columnspan=2, pady=10)

loginButtonStyle.configure('login.TButton', font=(None, 14))

root.mainloop()  # keeping the window running
