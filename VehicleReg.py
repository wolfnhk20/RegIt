from tkinter import *
from PIL import ImageTk
from tkinter import messagebox
import time
import ttkthemes


def datetime():
    current_date = time.strftime('%d/%m/%Y')
    current_time = time.strftime('%H:%M:%S')
    dateTimeLabel.config(text=f'Time: {current_time}\n    Date: {current_date}')
    dateTimeLabel.after(1000, datetime)


def slider():
    global count, s

    # if count == len(str):
    #     count = 0
    #     s = ''

    titleLabel.config(text=f'{s}{str[count]}')
    s = s + str[count]
    count = count + 1
    titleLabel.after(200, slider)


# GUI
root = Tk()
root.geometry('1280x720+0+0')
# root.attributes('-fullscreen', True)
root.title('RegIt')

dateTimeLabel = Label(root, font=('arial', 16, 'bold'))
dateTimeLabel.grid(row=0, column=0, padx=10, pady=10)
datetime()

str = 'RegIt'
s = ""
count = 0

titleLabel = Label(root
                   , font=('arial', 40, 'bold italic'), fg='red')
titleLabel.place(x=570, y=0)
slider()

c2d = Button(text='Connect Database', width=20, bg='grey', font=('arial', 10, 'bold')
             , activebackground='grey')
c2d.place(x=1050, y=25)

operationFrame = Frame(root)
operationFrame.place(x=320, y=86)

root.mainloop()
