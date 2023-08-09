import time
from tkinter import *
from tkinter import ttk, messagebox, filedialog
import ttkthemes
import pymysql
import pandas


def datetime():
    global current_date, current_time

    current_date = time.strftime('%d/%m/%Y')
    current_time = time.strftime('%H:%M:%S')
    dateTimeLabel.config(text=f'Time: {current_time}\n    Date: {current_date}')
    dateTimeLabel.after(1000, datetime)


def slider():
    global count, s

    if count == len(str):
        pass

    titleLabel.config(text=f'{s}{str[count]}')
    s = s + str[count]
    count = count + 1
    titleLabel.after(1000, slider)


def connectdb():
    def connect():
        global mycursor, con

        try:
            con = pymysql.connect(host=hostEntry.get(), user=userEntry.get(), password=passwordEntry.get())
            mycursor = con.cursor()
        except:
            messagebox.showerror('Failed', 'Failed to connect to database!', parent=dbPage)
            return

        try:
            query = 'create database RegIt;'
            mycursor.execute(query)

            query = 'use RegIt;'
            mycursor.execute(query)

            query = 'create table VehicleInfo(Parking_Slot_No varchar(10), Vehicle_No varchar(15), Vehicle_Name varchar(50), Owner_Name varchar(50), Owner_Contact_No(15), Owner_Address varchar(100), Added_Date varchar(15), Added_Time varchar(15));'
            mycursor.execute(query)
            con.commit()
        except:
            query = 'use RegIt'
            mycursor.execute(query)

        messagebox.showinfo('Connected', 'Connection established!', parent=dbPage)
        dbPage.destroy()

        addVehicle.config(state=NORMAL)
        searchVehicle.config(state=NORMAL)
        updateVehicle.config(state=NORMAL)
        deleteVehicle.config(state=NORMAL)
        showVehicle.config(state=NORMAL)
        exportData.config(state=NORMAL)

    dbPage = Toplevel()
    dbPage.grab_set()
    dbPage.geometry('500x290+350+150')
    dbPage['background'] = '#2a2a2a'
    dbPage.title('Connect Database')
    dbPage.resizable(False, False)

    dbImage = PhotoImage(file='databaseImage.png')
    dbPage.iconphoto(False, dbImage)

    titleLabel = Label(dbPage, text='Database Details', font=('sans-serif', 24, 'bold'), bg='#2a2a2a', fg='#a6a6a6')
    titleLabel.place(x=115, y=10)

    detailsFrame = Frame(dbPage, bg='#2a2a2a')
    detailsFrame.place(x=40, y=80)

    hostName = Label(detailsFrame, text='Host Name', font=('sans-serif', 14, 'bold'), bg='#2a2a2a', fg='#a6a6a6')
    hostEntry = ttk.Entry(detailsFrame, width=43)
    hostName.grid(row=1, column=0, padx=10, pady=10)
    hostEntry.grid(row=1, column=1)

    userName = Label(detailsFrame, text='Username', font=('sans-serif', 14, 'bold'), bg='#2a2a2a', fg='#a6a6a6')
    userEntry = ttk.Entry(detailsFrame, width=43)
    userName.grid(row=2, column=0, padx=10, pady=10)
    userEntry.grid(row=2, column=1)

    password = Label(detailsFrame, text='Password', font=('sans-serif', 14, 'bold'), bg='#2a2a2a', fg='#a6a6a6')
    passwordEntry = ttk.Entry(detailsFrame, width=43, show='*')
    password.grid(row=3, column=0, padx=10, pady=10)
    passwordEntry.grid(row=3, column=1)

    connectButton = ttk.Button(detailsFrame, text='Connect', command=connect)
    connectButton.grid(row=4, columnspan=2, pady=15)


def addVehicle():
    def addtoDB():
        if parkingEntry.get == '' or vehiclenoEntry.get() == '' or vehicalnameEntry.get() == '' or ownernameEntry.get() == '' or ownerconEntry.get() == '' or owneraddrEntry.get() == '':
            messagebox.showerror('Failed', 'All fields are required!', parent=addFrame)
        else:
            query = f'insert into VehicleInfo values (%s, %s, %s, %s, %s, %s, %s, %s)'
            mycursor.execute(query, (
            parkingEntry.get(), vehiclenoEntry.get(), vehicalnameEntry.get(), ownernameEntry.get(), ownerconEntry.get(),
            owneraddrEntry.get(), current_date, current_time))
            con.commit()

            ans = messagebox.askyesno('Successful', 'Do you want to add more data?', parent=addFrame)
            if ans:
                parkingEntry.delete(0, END)
                vehiclenoEntry.delete(0, END)
                vehicalnameEntry.delete(0, END)
                ownernameEntry.delete(0, END)
                ownerconEntry.delete(0, END)
                owneraddrEntry.delete(0, END)
            else:
                addFrame.destroy()

            query = 'SELECT * FROM VEHICLEINFO;'
            mycursor.execute(query)
            fetched_data = mycursor.fetchall()
            dataTreeView.delete(*dataTreeView.get_children())

            for vehicle_data in fetched_data:
                dataTreeView.insert('', END, values=vehicle_data)

    addFrame = Toplevel()
    addFrame.title('Add Vehicle Details')
    addFrame['background'] = '#2a2a2a'
    addFrame.resizable(False, False)
    addFrame.grab_set()

    addImage = PhotoImage(file='addImage.png')
    addFrame.iconphoto(False, addImage)

    addLabel = Label(addFrame, text='Add Vehicle Details', font=('sans-serif', 18, 'bold'), bg='#2a2a2a', fg='#a6a6a6')
    addLabel.grid(row=0, columnspan=2, padx=10, pady=20)

    parkingSlot = Label(addFrame, text='Parking Slot No.', font=('sans-serif', 12, 'bold'), bg='#2a2a2a', fg='#a6a6a6')
    vehicleno = Label(addFrame, text='Vehicle No.', font=('sans-serif', 12, 'bold'), bg='#2a2a2a', fg='#a6a6a6')
    vehiclename = Label(addFrame, text='Vehicle Name', font=('sans-serif', 12, 'bold'), bg='#2a2a2a', fg='#a6a6a6')
    ownername = Label(addFrame, text='Owner Name', font=('sans-serif', 12, 'bold'), bg='#2a2a2a', fg='#a6a6a6')
    ownercon = Label(addFrame, text='Owner Contact No.', font=('sans-serif', 12, 'bold'), bg='#2a2a2a', fg='#a6a6a6')
    owneraddr = Label(addFrame, text='Owner Address', font=('sans-serif', 12, 'bold'), bg='#2a2a2a', fg='#a6a6a6')
    parkingEntry = ttk.Entry(addFrame, width=25)
    vehiclenoEntry = ttk.Entry(addFrame, width=25)
    vehicalnameEntry = ttk.Entry(addFrame, width=25)
    ownernameEntry = ttk.Entry(addFrame, width=25)
    ownerconEntry = ttk.Entry(addFrame, width=25)
    owneraddrEntry = ttk.Entry(addFrame, width=25)

    parkingSlot.grid(row=1, column=0, padx=10, pady=20, sticky=W)
    parkingEntry.grid(row=1, column=1, padx=20, pady=20)
    vehicleno.grid(row=2, column=0, padx=10, pady=20, sticky=W)
    vehiclenoEntry.grid(row=2, column=1, padx=20, pady=20)
    vehiclename.grid(row=3, column=0, padx=10, pady=20, sticky=W)
    vehicalnameEntry.grid(row=3, column=1, padx=20, pady=20)
    ownername.grid(row=4, column=0, padx=10, pady=20, sticky=W)
    ownernameEntry.grid(row=4, column=1, padx=10, pady=20)
    ownercon.grid(row=5, column=0, padx=10, pady=20, sticky=W)
    ownerconEntry.grid(row=5, column=1, padx=20, pady=20)
    owneraddr.grid(row=6, column=0, padx=10, pady=20, sticky=W)
    owneraddrEntry.grid(row=6, column=1, padx=20, pady=20)

    addButton = ttk.Button(addFrame, text='Add Details', width=15, command=addtoDB)
    addButton.grid(row=7, columnspan=2, padx=10, pady=20)


def searchVehicle():
    def searchDB():
        query = 'select * from vehicleinfo where parking_slot_no = %s or vehicle_no = %s or vehicle_name = %s or owner_name = %s or owner_contact_no = %s or owner_address = %s or added_date = %s;'
        mycursor.execute(query, (parkingEntry.get(), vehiclenoEntry.get(), vehicalnameEntry.get(), ownernameEntry.get(), ownerconEntry.get(), owneraddrEntry.get(), added_dateEntry.get()))

        fetched_data = mycursor.fetchall()
        dataTreeView.delete(*dataTreeView.get_children())
        for vehicle_data in fetched_data:
            dataTreeView.insert('', END, values=vehicle_data)


    searchFrame = Toplevel()
    searchFrame.title('Search Vehicle Details')
    searchFrame['background'] = '#2a2a2a'
    searchFrame.resizable(False, False)
    searchFrame.grab_set()

    searchImage = PhotoImage(file='searchImage.png')
    searchFrame.iconphoto(False, searchImage)

    searchLabel = Label(searchFrame, text='Search Vehicle Details', font=('sans-serif', 18, 'bold'), bg='#2a2a2a', fg='#a6a6a6')
    searchLabel.grid(row=0, columnspan=2, padx=10, pady=20)

    parkingSlot = Label(searchFrame, text='Parking Slot No.', font=('sans-serif', 12, 'bold'), bg='#2a2a2a', fg='#a6a6a6')
    vehicleno = Label(searchFrame, text='Vehicle No.', font=('sans-serif', 12, 'bold'), bg='#2a2a2a', fg='#a6a6a6')
    vehiclename = Label(searchFrame, text='Vehicle Name', font=('sans-serif', 12, 'bold'), bg='#2a2a2a', fg='#a6a6a6')
    ownername = Label(searchFrame, text='Owner Name', font=('sans-serif', 12, 'bold'), bg='#2a2a2a', fg='#a6a6a6')
    ownercon = Label(searchFrame, text='Owner Contact No.', font=('sans-serif', 12, 'bold'), bg='#2a2a2a', fg='#a6a6a6')
    owneraddr = Label(searchFrame, text='Owner Address', font=('sans-serif', 12, 'bold'), bg='#2a2a2a', fg='#a6a6a6')
    added_date = Label(searchFrame, text="Added Date", font=('sans-serif', 12, 'bold'), bg='#2a2a2a', fg='#a6a6a6')
    parkingEntry = ttk.Entry(searchFrame, width=25)
    vehiclenoEntry = ttk.Entry(searchFrame, width=25)
    vehicalnameEntry = ttk.Entry(searchFrame, width=25)
    ownernameEntry = ttk.Entry(searchFrame, width=25)
    ownerconEntry = ttk.Entry(searchFrame, width=25)
    owneraddrEntry = ttk.Entry(searchFrame, width=25)
    added_dateEntry = ttk.Entry(searchFrame, width=25)

    parkingSlot.grid(row=1, column=0, padx=10, pady=20, sticky=W)
    parkingEntry.grid(row=1, column=1, padx=20, pady=20)
    vehicleno.grid(row=2, column=0, padx=10, pady=20, sticky=W)
    vehiclenoEntry.grid(row=2, column=1, padx=20, pady=20)
    vehiclename.grid(row=3, column=0, padx=10, pady=20, sticky=W)
    vehicalnameEntry.grid(row=3, column=1, padx=20, pady=20)
    ownername.grid(row=4, column=0, padx=10, pady=20, sticky=W)
    ownernameEntry.grid(row=4, column=1, padx=10, pady=20)
    ownercon.grid(row=5, column=0, padx=10, pady=20, sticky=W)
    ownerconEntry.grid(row=5, column=1, padx=20, pady=20)
    owneraddr.grid(row=6, column=0, padx=10, pady=20, sticky=W)
    owneraddrEntry.grid(row=6, column=1, padx=20, pady=20)
    added_date.grid(row=7, column=0, padx=10, pady=20, sticky=W)
    added_dateEntry.grid(row=7, column=1, padx=20, pady=20)

    searchButton = ttk.Button(searchFrame, text='Search Details', width=15, command=searchDB)
    searchButton.grid(row=8, columnspan=2, padx=10, pady=20)


def deletefromDB():
    selected = dataTreeView.focus()
    deleteItems = dataTreeView.item(selected)
    deleteItemsID = deleteItems['values'][0]

    result = messagebox.askyesno('Confirmation', 'Do you want to delete this record?')

    if result:
        query = 'delete from vehicleinfo where parking_slot_no = %s'
        mycursor.execute(query, deleteItemsID)
        con.commit()
        messagebox.showinfo('Deleted', 'Record successfully deleted!')

        dataTreeView.delete(*dataTreeView.get_children())
        query = 'select * from vehicleinfo;'
        mycursor.execute(query)
        fetched_data = mycursor.fetchall()
        for vehicledata in fetched_data:
            dataTreeView.insert('', END, values=vehicledata)


def showVehicles():
    dataTreeView.delete(*dataTreeView.get_children())
    query = 'select * from vehicleinfo;'
    mycursor.execute(query)
    fetched_data = mycursor.fetchall()
    for vehicledata in fetched_data:
        dataTreeView.insert('', END, values=vehicledata)


def updateVehicle():
    def updatetoDB():
        result = messagebox.askyesno('Confirmation', 'Do you want to update selected record?', parent=updateFrame)

        if result:
            query = 'update vehicleinfo set parking_slot_no = %s, vehicle_no = %s, vehicle_name = %s, owner_name = %s, owner_contact_no = %s, owner_address = %s, added_date = %s, added_time = %s where parking_slot_no = %s;'
            mycursor.execute(query, (parkingEntry.get(), vehiclenoEntry.get(), vehicalnameEntry.get(), ownernameEntry.get(), ownerconEntry.get(), owneraddrEntry.get(), current_date, current_time, parkingEntry.get()))
            con.commit()
            messagebox.showinfo('Success', 'Data updated successfully!', parent=updateFrame)
            updateFrame.destroy()

            dataTreeView.delete(*dataTreeView.get_children())
            query = 'select * from vehicleinfo;'
            mycursor.execute(query)
            fetched_data = mycursor.fetchall()
            for vehicledata in fetched_data:
                dataTreeView.insert('', END, values=vehicledata)


    updateFrame = Toplevel()
    updateFrame.title('Update Vehicle Details')
    updateFrame['background'] = '#2a2a2a'
    updateFrame.resizable(False, False)
    updateFrame.grab_set()

    updateImage = PhotoImage(file='updateImage.png')
    updateFrame.iconphoto(False, updateImage)

    updateLabel = Label(updateFrame, text='Update Vehicle Details', font=('sans-serif', 18, 'bold'), bg='#2a2a2a', fg='#a6a6a6')
    updateLabel.grid(row=0, columnspan=2, padx=10, pady=20)

    parkingSlot = Label(updateFrame, text='Parking Slot No.', font=('sans-serif', 12, 'bold'), bg='#2a2a2a', fg='#a6a6a6')
    vehicleno = Label(updateFrame, text='Vehicle No.', font=('sans-serif', 12, 'bold'), bg='#2a2a2a', fg='#a6a6a6')
    vehiclename = Label(updateFrame, text='Vehicle Name', font=('sans-serif', 12, 'bold'), bg='#2a2a2a', fg='#a6a6a6')
    ownername = Label(updateFrame, text='Owner Name', font=('sans-serif', 12, 'bold'), bg='#2a2a2a', fg='#a6a6a6')
    ownercon = Label(updateFrame, text='Owner Contact No.', font=('sans-serif', 12, 'bold'), bg='#2a2a2a', fg='#a6a6a6')
    owneraddr = Label(updateFrame, text='Owner Address', font=('sans-serif', 12, 'bold'), bg='#2a2a2a', fg='#a6a6a6')
    parkingEntry = ttk.Entry(updateFrame, width=25)
    vehiclenoEntry = ttk.Entry(updateFrame, width=25)
    vehicalnameEntry = ttk.Entry(updateFrame, width=25)
    ownernameEntry = ttk.Entry(updateFrame, width=25)
    ownerconEntry = ttk.Entry(updateFrame, width=25)
    owneraddrEntry = ttk.Entry(updateFrame, width=25)

    parkingSlot.grid(row=1, column=0, padx=10, pady=20, sticky=W)
    parkingEntry.grid(row=1, column=1, padx=20, pady=20)
    vehicleno.grid(row=2, column=0, padx=10, pady=20, sticky=W)
    vehiclenoEntry.grid(row=2, column=1, padx=20, pady=20)
    vehiclename.grid(row=3, column=0, padx=10, pady=20, sticky=W)
    vehicalnameEntry.grid(row=3, column=1, padx=20, pady=20)
    ownername.grid(row=4, column=0, padx=10, pady=20, sticky=W)
    ownernameEntry.grid(row=4, column=1, padx=10, pady=20)
    ownercon.grid(row=5, column=0, padx=10, pady=20, sticky=W)
    ownerconEntry.grid(row=5, column=1, padx=20, pady=20)
    owneraddr.grid(row=6, column=0, padx=10, pady=20, sticky=W)
    owneraddrEntry.grid(row=6, column=1, padx=20, pady=20)

    updateButton = ttk.Button(updateFrame, text='Update Details', width=15, command=updatetoDB)
    updateButton.grid(row=7, columnspan=2, padx=10, pady=20)

    focus = dataTreeView.focus()
    vehicle_data = dataTreeView.item(focus)
    vehicledatalist = vehicle_data['values']

    parkingEntry.insert(0, vehicledatalist[0])
    vehiclenoEntry.insert(0, vehicledatalist[1])
    vehicalnameEntry.insert(0, vehicledatalist[2])
    ownernameEntry.insert(0, vehicledatalist[3])
    ownerconEntry.insert(0, vehicledatalist[4])
    owneraddrEntry.insert(0, vehicledatalist[5])

def exportVehicleData():
    url = filedialog.asksaveasfilename(defaultextension='.csv')
    index = dataTreeView.get_children()
    datalist = []
    for vdata in index:
        content = dataTreeView.item(vdata)
        vlist = content['values']
        datalist.append(vlist)

    table = pandas.DataFrame(datalist, columns=['Parking_Slot_No', 'Vehicle_No', 'Vehicle_Name', 'Owner_Name', 'Owner_Contact_No', 'Owner_Address', 'Added_Date', 'Added_Time'])
    table.to_csv(url, index=False)
    messagebox.showinfo('Success', 'Data exported successfully!')


# GUI
root = ttkthemes.ThemedTk(theme='equilux')

root.geometry('1230x620+20+10')
# root.attributes('-fullscreen', True)
root.title('RegIt')
root.resizable(False, False)
root['background'] = '#2a2a2a'

menu_image = PhotoImage(file='menu_icon.png')
root.iconphoto(False, menu_image)

dateTimeLabel = Label(root, font=('sans-serif', 16, 'bold'), bg='#2a2a2a', fg='#a6a6a6')
dateTimeLabel.grid(row=0, column=0, padx=10, pady=10)
datetime()

str = 'RegIt'
s = ""
count = 0
titleLabel = Label(root, font=('sans-serif', 40, 'bold italic'), bg='#2a2a2a', fg='#a6a6a6')
titleLabel.place(x=570, y=0)
slider()

c2d = ttk.Button(text='Connect Database', width=20, command=connectdb)
c2d.place(x=1050, y=25)

# left frame
operationFrame = Frame(root)
operationFrame.place(x=30, y=96)
operationFrame['background'] = '#2a2a2a'

operationImage = PhotoImage(file='operation.png')
operationImageLabel = Label(operationFrame, image=operationImage, bg='#2a2a2a')
operationImageLabel.grid(row=0, column=0, pady=10)

# operation buttons
addVehicle = ttk.Button(operationFrame, text='Add Vehicle', width=25, state=DISABLED, command=addVehicle)
addVehicle.grid(row=1, column=0, pady=15)

searchVehicle = ttk.Button(operationFrame, text='Search Vehicle', width=25, state=DISABLED, command=searchVehicle)
searchVehicle.grid(row=2, column=0, pady=15)

updateVehicle = ttk.Button(operationFrame, text='Update Vehicle', width=25, state=DISABLED, command=updateVehicle)
updateVehicle.grid(row=3, column=0, pady=15)

deleteVehicle = ttk.Button(operationFrame, text='Delete Vehicle', width=25, state=DISABLED, command=deletefromDB)
deleteVehicle.grid(row=4, column=0, pady=15)

showVehicle = ttk.Button(operationFrame, text='Show Vehicles', width=25, state=DISABLED, command=showVehicles)
showVehicle.grid(row=5, column=0, pady=15)

exportData = ttk.Button(operationFrame, text='Export Data', width=25, state=DISABLED, command=exportVehicleData)
exportData.grid(row=6, column=0, pady=15)

dataFrame = Frame(root)
dataFrame.place(x=295, y=115, width=900, height=475)
dataFrame['background'] = '#2a2a2a'

horizontalScroll = ttk.Scrollbar(dataFrame, orient=HORIZONTAL)
verticalScroll = ttk.Scrollbar(dataFrame, orient=VERTICAL)

dataTreeView = ttk.Treeview(dataFrame, columns=('Parking_Slot_No', 'Vehicle_No', 'Vehicle_Name', 'Owner_Name'
                                                , 'Owner_Contact_No', 'Owner_Address', 'Added_Date', 'Added_Time')
                            , xscrollcommand=horizontalScroll.set, yscrollcommand=verticalScroll.set)

horizontalScroll.config(command=dataTreeView.xview)
verticalScroll.config(command=dataTreeView.yview)

horizontalScroll.pack(side=BOTTOM, fill=X)
verticalScroll.pack(side=RIGHT, fill=Y)

dataTreeView.pack(fill=BOTH, expand=1)

dataTreeView.heading('Parking_Slot_No', text='Parking Slot No.')
dataTreeView.heading('Vehicle_No', text='Vehicle No.')
dataTreeView.heading('Vehicle_Name', text='Vehicle Name')
dataTreeView.heading('Owner_Name', text='Owner Name')
dataTreeView.heading('Owner_Contact_No', text='Owner Contact No.')
dataTreeView.heading('Owner_Address', text='Owner Address')
dataTreeView.heading('Added_Date', text='Added Date')
dataTreeView.heading('Added_Time', text='Added_Time')

dataTreeView.config(show='headings')

dataTreeView.column('Parking_Slot_No', anchor=CENTER)
dataTreeView.column('Vehicle_No', anchor=CENTER)
dataTreeView.column('Vehicle_Name', anchor=CENTER)
dataTreeView.column('Owner_Name', anchor=CENTER)
dataTreeView.column('Owner_Contact_No', anchor=CENTER)
dataTreeView.column('Owner_Address', anchor=CENTER)
dataTreeView.column('Added_Date', anchor=CENTER)
dataTreeView.column('Added_Time', anchor=CENTER)

style = ttk.Style()
style.configure(dataTreeView, rowheight=300)

root.mainloop()
