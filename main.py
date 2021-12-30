# Railway Project
from tkinter import *
import tkinter
from PIL import ImageTk,Image
import sqlite3
from tkinter import messagebox 
from tkinter import ttk
from tkcalendar import Calendar, DateEntry

root = Tk() # Main Window

root.title("Railway Project")
root.geometry("1600x900")
# root.iconbitmap("Imgs\Img6.png")

# Creating a database or connect to one if it is already exists
conn = sqlite3.connect("RailwayData.db")
# Creating a cursor
c = conn.cursor()

# Creating Passenger Table
c.execute("""CREATE TABLE IF NOT EXISTS PASSENGER(
    FNAME VARCHAR NOT NULL,
    LNAME VARCHAR NOT NULL,
    EMAIL VARCHAR NOT NULL PRIMARY KEY,
    MOBILE VARCHAR NOT NULL,
    AGE VARCHAR NOT NULL,
    GENDER VARCHAR NOT NULL,
    CITY VARCHAR NOT NULL,
    PIN VARCHAR NOT NULL,
    PW VARCHAR NOT NULL
)
""")

# Creating Admin Table
c.execute("""CREATE TABLE IF NOT EXISTS ADMN(
    FNAME VARCHAR NOT NULL,
    LNAME VARCHAR NOT NULL,
    EMAIL VARCHAR NOT NULL PRIMARY KEY,
    MOBILE VARCHAR NOT NULL,
    AGE VARCHAR NOT NULL,
    GENDER VARCHAR NOT NULL,
    CITY VARCHAR NOT NULL,
    PIN VARCHAR NOT NULL,
    PW VARCHAR NOT NULL
)
""")

# Creating Tickets Table
c.execute("""CREATE TABLE IF NOT EXISTS TICKETS(
    TKTID VARCHAR NOT NULL PRIMARY KEY,
    PNAME VARCHAR NOT NULL,
    PEMAIL VARCHAR NOT NULL,
    TNO VARCHAR NOT NULL,
    SOURCE VARCHAR NOT NULL,
    DEST VARCHAR NOT NULL,
    TDATE DATE NOT NULL,
    TYP VARCHAR NOT NULL,
    NOTKTS VARCHAR NOT NULL,
    FARE VARCHAR NOT NULL
)""")

# Creating Trains Table
c.execute("""CREATE TABLE IF NOT EXISTS TRAINS(
    TNO VARCHAR NOT NULL PRIMARY KEY,
    TNAME VARCHAR NOT NULL,
    SOURCE VARCHAR NOT NULL,
    DEST VARCHAR NOT NULL,
    TDATE DATE NOT NULL,
    CAP NUMBER NOT NULL,
    DIST VARCHAR NOT NULL,
    FARE VARCHAR NOT NULL
)""")

# Creating Transaction Table
c.execute("""CREATE TABLE IF NOT EXISTS TRANSACT(
    TRNSID VARCHAR NOT NULL PRIMARY KEY,
    EMAIL VARCHAR,
    CNAME VARCHAR,
    CNO VARCHAR,
    TDATE DATE,
    AMOUNT VARCHAR
)""")

# Creating Requests Table
c.execute("""CREATE TABLE IF NOT EXISTS REQUESTS(
    TKTID VARCHAR NOT NULL PRIMARY KEY,
    PRIORITY VARCHAR NOT NULL,
    PNAME VARCHAR NOT NULL,
    PEMAIL VARCHAR NOT NULL,
    TNO VARCHAR NOT NULL,
    SOURCE VARCHAR NOT NULL,
    DEST VARCHAR NOT NULL,
    TDATE DATE NOT NULL,
    TYP VARCHAR NOT NULL,
    NOTKTS VARCHAR NOT NULL,
    FARE VARCHAR NOT NULL
)""")

# Commit Changes
conn.commit()

# Close Connection
conn.close()










# Booking History Window
def myBookingHistory(email):
    global mbh
    mbh = Tk()
    ph.iconify()
    mbh.title("Booking History")
    mbh.geometry("1600x900")

    def goBackph():
        ph.deiconify()
        mbh.destroy()

    helloLabel = Label(mbh, text="My Booking History")
    helloLabel.config(font=("Verdana",30))
    helloLabel.pack(pady=20)

    # Create a main frame
    main_frame = Frame(mbh)
    main_frame.pack(fill=BOTH, expand=1,padx=10)

    # Create a canvas
    my_canvas = Canvas(main_frame)
    my_canvas.pack(side=LEFT, fill=BOTH, expand=1)

    # Add a scrollbar to the canvas
    my_scrollbar = ttk.Scrollbar(main_frame, orient=VERTICAL,command=my_canvas.yview)
    my_scrollbar.pack(side=RIGHT, fill=Y)

    # Configure the canvas
    my_canvas.config(yscrollcommand=my_scrollbar.set)
    my_canvas.bind('<Configure>',lambda e : my_canvas.config(scrollregion = my_canvas.bbox("all")))

    # Add another frame inside the canvas
    second_frame = Frame(my_canvas)

    # Add that New frame to a window in the canvas
    my_canvas.create_window((0,0), window = second_frame, anchor="nw")

    # Creating a database or connect to one if it is already exists
    conn = sqlite3.connect("RailwayData.db") 

    # Creating a cursor
    c = conn.cursor()

    # Query the Database
    c.execute("SELECT * FROM TICKETS WHERE PEMAIL = ?",[email])
    myTravData = c.fetchall()

    # Commit Changes
    conn.commit()

    # Close Connection
    conn.close()

    if len(myTravData)==0:
        Label(second_frame,text="").grid(row=0,column=0,ipadx=290,pady=50)
        sampleLabel = Label(second_frame,text="No Travelling history found")
        sampleLabel.config(font=("Verdana",20))
        sampleLabel.grid(row=0,column=1)
        goBackah = Button(mbh, text = "Go Back", background = "black", foreground = "grey", command=goBackph)
        goBackah.config(font = ("Verdana", 16))
        goBackah.pack(ipadx=5,ipady=2,pady=20)
        return
    
    Label(second_frame,text="").grid(row=0,column=0,ipadx=50)
    sampleLabel=Label(second_frame,text="Ticket ID")
    sampleLabel.config(font=("Verdana",16))
    sampleLabel.grid(row=0,column=1,padx=20,pady=20)
    sampleLabel=Label(second_frame,text="Train Number")
    sampleLabel.config(font=("Verdana",16))
    sampleLabel.grid(row=0,column=2,padx=20)
    sampleLabel=Label(second_frame,text="From")
    sampleLabel.config(font=("Verdana",16))
    sampleLabel.grid(row=0,column=3,padx=20)
    sampleLabel=Label(second_frame,text="To")
    sampleLabel.config(font=("Verdana",16))
    sampleLabel.grid(row=0,column=4,padx=20)
    sampleLabel=Label(second_frame,text="Date")
    sampleLabel.config(font=("Verdana",16))
    sampleLabel.grid(row=0,column=5,padx=20)
    sampleLabel=Label(second_frame,text="Type")
    sampleLabel.config(font=("Verdana",16))
    sampleLabel.grid(row=0,column=6,padx=20)
    sampleLabel=Label(second_frame,text="No. of Tickets")
    sampleLabel.config(font=("Verdana",16))
    sampleLabel.grid(row=0,column=7,padx=20)
    sampleLabel=Label(second_frame,text="Fare")
    sampleLabel.config(font=("Verdana",16))
    sampleLabel.grid(row=0,column=8,padx=20)

    for i in range (len(myTravData)):
        for j in range (len(myTravData[i])):
            if j!=1 and j!=2:
                if j==0:
                    k=0
                else:
                    k=j-2
                sampleLabel=Label(second_frame,text=myTravData[i][j])
                sampleLabel.config(font=("Verdana",12))
                sampleLabel.grid(row=i+1,column=k+1,pady=10,padx=10)
    
    goBackah= Button(mbh, text = "Go Back", background = "black", foreground = "grey", command=goBackph)
    goBackah.config(font = ("Verdana", 16))
    goBackah.pack(ipadx=5,ipady=2,pady=20)

# goToPayment Window
def goToPayment(trainData, formDetails, passengerData, priorityScore):
    print(trainData)
    print(formDetails)
    print(passengerData)
    print(priorityScore)
    global gtp
    gtp = Tk()
    ppd.iconify()
    gtp.title("Payment")
    gtp.geometry("1600x900")

    def reqConfirmTicket():
        if name_gtp.get()=="" or number_gtp.get()=="" or expMon_gtp.get()=="" or expYr_gtp.get()=="" or cvv_gtp.get()=="" or mobile_gtp.get()=="" or otp_gtp.get() =="":
            errorLabel = Label(gtp,  text="Enter data in all input fields", fg = "red", bg = "black")
            errorLabel.config(font = ("Verdana", 12))
            errorLabel.grid(row=11,column=3,ipadx=20,ipady=16,pady=10)
            return

        if int(trainData[5]) < int(formDetails[1]):
            msgText = "Tickets are not available for this Train : ("
            messagebox.showinfo("Message",msgText)
            return

        tn = '100000'
        # Creating a database or connect to one if it is already exists
        conn = sqlite3.connect("RailwayData.db") 

        # Creating a cursor
        c = conn.cursor()
        
        # insert into table
        c.execute('INSERT INTO REQUESTS VALUES(:tkno,:pri,:pname,:pemail,:tno,:froms,:tos,:tdate,:typ,:notkts,:fare)',
        {
                'tkno': tn,
                'pri':priorityScore,
                'pname':passengerData[0],
                'pemail':passengerData[2],
                'tno':trainData[0],
                'froms':trainData[2],
                'tos':trainData[3],
                'tdate':trainData[4],
                'typ':formDetails[0],
                'notkts':formDetails[1],
                'fare':str(int(formDetails[1])*int(trainData[7]))
        }
        )

        c.execute("UPDATE REQUESTS SET TKTID=OID")

        # c.execute('UPDATE TRAINS SET CAP = ? WHERE TNO = ?',[str(int(trainData[5])-int(formDetails[1])),trainData[0]])

        c.execute('SELECT DATE()')
        currDate = c.fetchall()

        c.execute('INSERT INTO TRANSACT VALUES(:trsid,:email,:cname,:cno,:tdate,:amt)',
        {
            'trsid':tn,
            'email':passengerData[2],
            'cname':name_gtp.get(),
            'cno':number_gtp.get(),
            'tdate':currDate[0][0],
            'amt':str(int(formDetails[1])*int(trainData[7]))
        }
        )

        c.execute("UPDATE TRANSACT SET TRNSID=OID")

        # Commit Changes
        conn.commit()

        # Close Connection
        conn.close()

        msgText = "Congrats, Your booking is confirmed!\n Happy Journey : )"
        messagebox.showinfo("Message",msgText)
        ppd.destroy()

        pb.deiconify()
        gtp.destroy()
        pst.destroy()

    def goBackpst():
        ppd.deiconify()
        gtp.destroy()

    goBackToPLogin = Button(gtp, text = "<", background = "black", foreground = "grey", command=goBackpst)
    goBackToPLogin.config(font = ("Verdana", 20))
    goBackToPLogin.grid(row=0,column=0,ipadx=5,ipady=5)

    Label(gtp, text="").grid(row=1,column=1,ipadx=190)

    helloLabel = Label(gtp, text="Payment")
    helloLabel.config(font=("Verdana",30))
    helloLabel.grid(row=2,column=3,pady=40)

    nameLabel_gtp = Label(gtp, text="Card Holder Name")
    nameLabel_gtp.config(font = ("Verdana", 16))
    nameLabel_gtp.grid(row=3,column=2,pady=10,padx=10)

    numberLabel_gtp = Label(gtp, text="Card Number")
    numberLabel_gtp.config(font = ("Verdana", 16))
    numberLabel_gtp.grid(row=4,column=2,pady=10)

    expLabel_gtp = Label(gtp, text="Expiry")
    expLabel_gtp.config(font = ("Verdana", 16))
    expLabel_gtp.grid(row=5,column=2,pady=10)

    cvvLabel_gtp = Label(gtp, text="CVV")
    cvvLabel_gtp.config(font = ("Verdana", 16))
    cvvLabel_gtp.grid(row=6,column=2,pady=10)

    mobileLabel_gtp = Label(gtp, text="Mobile")
    mobileLabel_gtp.config(font = ("Verdana", 16))
    mobileLabel_gtp.grid(row=7,column=2,pady=10)

    otpLabel_gtp= Label(gtp, text="OTP")
    otpLabel_gtp.config(font = ("Verdana", 16))
    otpLabel_gtp.grid(row=8,column=2,pady=10)

    name_gtp = Entry(gtp, width=20)
    name_gtp.config(font = ("Verdana",16))
    name_gtp.grid(row=3,column=3)

    number_gtp = Entry(gtp, width=20)
    number_gtp.config(font = ("Verdana",16))
    number_gtp.grid(row=4,column=3)

    expMon = StringVar() 
    expMon_gtp = ttk.Combobox(gtp,width=18,textvariable = expMon)
    expMon_gtp['values']=('January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December')
    expMon_gtp.config(font=("Verdana",15))
    expMon_gtp.grid(row=5,column=3,ipady=2)
    expMon_gtp.current(0)

    expYr = StringVar() 
    expYr_gtp = ttk.Combobox(gtp,width=18,textvariable = expYr)
    expYr_gtp['values']=('2021','2022','2023','2024','2025','2026','2027','2028','2029','2030')
    expYr_gtp.config(font=("Verdana",15))
    expYr_gtp.grid(row=5,column=4,ipady=2,padx=2)
    expYr_gtp.current(0)

    cvv_gtp = Entry(gtp, width=20)
    cvv_gtp.config(font = ("Verdana",16))
    cvv_gtp.grid(row=6,column=3)

    mobile_gtp = Entry(gtp, width=20)
    mobile_gtp.config(font = ("Verdana",16))
    mobile_gtp.grid(row=7,column=3)

    otp_gtp = Entry(gtp, width=20)
    otp_gtp.config(font = ("Verdana",16))
    otp_gtp.grid(row=8,column=3)

    amount = Label(gtp, text="Amount to be paid  " + str(int(trainData[7])*int(formDetails[1])))
    amount.config(font = ("Verdana",16))
    amount.grid(row=9,column=3)

    buttonConfirm = Button(gtp, text = "Confirm", background = "black", foreground = "grey", command=reqConfirmTicket)
    buttonConfirm.config(font = ("Verdana", 15))
    buttonConfirm.grid(row = 10, column = 3, ipadx = 25, ipady=5, pady = 30)

# Priority Details 
def priorityDetails(trainData, formDetails, passengerData):
    global ppd
    ppd = Tk()
    pst.iconify()
    ppd.title("Priority Details")
    ppd.geometry("1600x900")
    global priorityScore
    priorityScore = 0

    def goBackpst():
        pst.deiconify()
        ppd.destroy()
    
    goBackToPLogin = Button(ppd, text = "<", background = "black", foreground = "grey", command=goBackpst)
    goBackToPLogin.config(font = ("Verdana", 20))
    goBackToPLogin.grid(row=0,column=0,ipadx=5,ipady=5)

    Label(ppd, text="").grid(row=1,column=1,ipadx=148)

    helloLabel = Label(ppd, text="Passenger Details")
    helloLabel.config(font=("Verdana",30))
    helloLabel.grid(row=2,column=3,pady=40)

    infoLabel = Label(ppd, text="Does any of the following categories apply to the passengers?(check the boxes if any)")
    infoLabel.config(font=("Verdana",15))
    infoLabel.grid(row=3,column=3,pady=40)

    def updateScore():
        global priorityScore
        priorityScore = 0
        if oldAgeStatus:
            priorityScore = priorityScore + 10
        if pwStatus :
            priorityScore = priorityScore + 20
        if hcStatus :
            priorityScore = priorityScore + 30

    global oldAgeStatus
    oldAgeStatus = False

    def changeStatus1(status):
        global oldAgeStatus
        oldAgeStatus = not status
        updateScore()

    c1 = Checkbutton(ppd, text='Old Aged (age > 60)',command=lambda:changeStatus1(oldAgeStatus))
    c1.config(font=("Verdana",15))
    c1.grid(row=4,column=3,pady=20)

    global hcStatus
    hcStatus = False

    def changeStatus2(status):
        global hcStatus
        hcStatus = not status
        updateScore()

    c2 = Checkbutton(ppd, text='Physically Challenged',command=lambda:changeStatus2(hcStatus))
    c2.config(font=("Verdana",15))
    c2.grid(row=5,column=3,pady=20)

    global pwStatus
    pwStatus = False

    def changeStatus3(status):
        global pwStatus
        pwStatus = not status
        updateScore()

    c3 = Checkbutton(ppd, text='Pregnant Woman',command=lambda:changeStatus3(pwStatus))
    c3.config(font=("Verdana",15))
    c3.grid(row=6,column=3,pady=20)

    Label(ppd, text=" ").grid(row=7, column=3)

    continueButton = Button(ppd, text = "Continue", background = "black", foreground = "grey", command=lambda:goToPayment(trainData, formDetails, passengerData, priorityScore))
    continueButton.config(font = ("Verdana", 20))
    continueButton.grid(row=8,column=3)

# Trains availabe
def showTrains(trainsData, formDetails, passengerData):
    global pst
    pst = Tk()
    pb.iconify()
    pst.title("Trains Available")
    pst.geometry("1600x900")

    def goBackpb():
        pb.deiconify()
        pst.destroy()

    helloLabel = Label(pst, text="Trains Available")
    helloLabel.config(font=("Verdana",30))
    helloLabel.pack(pady=20)

    # Create a main frame
    main_frame = Frame(pst)
    main_frame.pack(fill=BOTH, expand=1,padx=10)

    # Create a canvas
    my_canvas = Canvas(main_frame)
    my_canvas.pack(side=LEFT, fill=BOTH, expand=1)

    # Add a scrollbar to the canvas
    my_scrollbar = ttk.Scrollbar(main_frame, orient=VERTICAL,command=my_canvas.yview)
    my_scrollbar.pack(side=RIGHT, fill=Y)

    # Configure the canvas
    my_canvas.config(yscrollcommand=my_scrollbar.set)
    my_canvas.bind('<Configure>',lambda e : my_canvas.config(scrollregion = my_canvas.bbox("all")))

    # Add another frame inside the canvas
    second_frame = Frame(my_canvas)

    # Add that New frame to a window in the canvas
    my_canvas.create_window((0,0), window = second_frame, anchor="nw")

    if len(trainsData)==0:
        Label(second_frame,text="").grid(row=0,column=0,ipadx=200,pady=50)
        sampleLabel = Label(second_frame,text="Sorry, Currently no trains are available in this path : (")
        sampleLabel.config(font=("Verdana",20))
        sampleLabel.grid(row=0,column=1)
        goBackToPLogin = Button(pst, text = "Go Back", background = "black", foreground = "grey", command=goBackpb)
        goBackToPLogin.config(font = ("Verdana", 16))
        goBackToPLogin.pack(ipadx=5,ipady=2,pady=20)
        return

    for i in range(len(trainsData)):
        if formDetails[0] == 'AC First Class(1A)':
            trainsData[i][7] = str(int(trainsData[i][7])+60)
        elif formDetails[0] == 'Exec. Chair Car(EC)':
            trainsData[i][7] = str(int(trainsData[i][7])+70)
        elif formDetails[0] == 'AC 2 Tier(2A)':
            trainsData[i][7] = str(int(trainsData[i][7])+50)
        elif formDetails[0] == 'First Class(FC)':
            trainsData[i][7] = str(int(trainsData[i][7])+40)
        elif formDetails[0] == 'AC 3 Tier(3A)':
            trainsData[i][7] = str(int(trainsData[i][7])+40)
        elif formDetails[0] == 'AC 3 Economy(3E)':
            trainsData[i][7] = str(int(trainsData[i][7])+30)
        elif formDetails[0] == 'AC Chair Car(CC)':
            trainsData[i][7] = str(int(trainsData[i][7])+125)

    sampleLabel=Label(second_frame,text="Train No")
    sampleLabel.config(font=("Verdana",16))
    sampleLabel.grid(row=0,column=0,padx=30,pady=20)
    sampleLabel=Label(second_frame,text="Train Name")
    sampleLabel.config(font=("Verdana",16))
    sampleLabel.grid(row=0,column=1,padx=30)
    sampleLabel=Label(second_frame,text="From")
    sampleLabel.config(font=("Verdana",16))
    sampleLabel.grid(row=0,column=2,padx=30)
    sampleLabel=Label(second_frame,text="To")
    sampleLabel.config(font=("Verdana",16))
    sampleLabel.grid(row=0,column=3,padx=30)
    sampleLabel=Label(second_frame,text="Date")
    sampleLabel.config(font=("Verdana",16))
    sampleLabel.grid(row=0,column=4,padx=30)
    sampleLabel=Label(second_frame,text="Seats Available")
    sampleLabel.config(font=("Verdana",16))
    sampleLabel.grid(row=0,column=5,padx=30)
    sampleLabel=Label(second_frame,text="Distance")
    sampleLabel.config(font=("Verdana",16))
    sampleLabel.grid(row=0,column=6,padx=30)
    sampleLabel=Label(second_frame,text="Fare")
    sampleLabel.config(font=("Verdana",16))
    sampleLabel.grid(row=0,column=7,padx=30)

    for i in range (len(trainsData)):
        for j in range (len(trainsData[i])):
            sampleLabel=Label(second_frame,text=trainsData[i][j])
            sampleLabel.config(font=("Verdana",12))
            sampleLabel.grid(row=i+1,column=j,pady=10)
        sampleButton = Button(second_frame,text="Book Now",fg="white",bg="black",command=lambda:priorityDetails(trainsData[i-1],formDetails,passengerData))
        sampleButton.config(font=("Verdana",12))
        sampleButton.grid(row=i+1,column=len(trainsData[i]),ipadx=20,pady=10,padx=40)
    
    goBackToPLogin = Button(pst, text = "Go Back", background = "black", foreground = "grey", command=goBackpb)
    goBackToPLogin.config(font = ("Verdana", 16))
    goBackToPLogin.pack(ipadx=5,ipady=2,pady=20)

# Passenger Ticket Booking
def passengerBookTicket(passengerData):
    global pb
    pb = Tk()
    ph.iconify()
    pb.title("Ticket Booking")
    pb.geometry("1600x900")

    def goBackph():
        ph.deiconify()
        pb.destroy()

    def searchForTrains():
        if fromEntry_pb.get() == "" or toEntry_pb.get() == "" or date_pb.get() =="" or tktEntry_pb.get() == "":
            errorLabel = Label(pb,  text="Enter data in all input fields", fg = "red", bg = "black")
            errorLabel.config(font = ("Verdana", 12))
            errorLabel.grid(row=7,column=3,ipadx=20,ipady=16,pady=10)
            return
        # Creating a database or connect to one if it is already exists
        conn = sqlite3.connect("RailwayData.db") 

        # Creating a cursor
        c = conn.cursor()

        # Query the Database
        det = []
        c.execute("SELECT * FROM TRAINS WHERE SOURCE = ? AND DEST = ? AND TDATE = ?",[fromEntry_pb.get(),toEntry_pb.get(),date_pb.get()])
        det = c.fetchall()

        # Commit Changes
        conn.commit()

        # Close Connection
        conn.close()

        formDetails = [tktEntry_pb.get(),noTkts_pb.get()]

        trainDet = []
        for i in range(len(det)):
            tempList = []
            for j in range(len(det[i])):
                tempList.append(det[i][j])
            trainDet.append(tempList)

        showTrains(trainDet, formDetails, passengerData)

    goBackToPLogin = Button(pb, text = "<", background = "black", foreground = "grey", command=goBackph)
    goBackToPLogin.config(font = ("Verdana", 20))
    goBackToPLogin.grid(row=0,column=0,ipadx=5,ipady=5)

    Label(pb, text=" ").grid(row=1,column=1,ipadx=250,pady=60)

    helloLabel = Label(pb, text="Ticket Booking")
    helloLabel.config(font=("Verdana",25))
    helloLabel.grid(row=1,column=3,pady=20)

    fromLabel_pb = Label(pb,text="From")
    fromLabel_pb.config(font=("Verdana",15))
    fromLabel_pb.grid(row=2,column=2,pady=10,padx=10)

    from_val = StringVar() 
    fromEntry_pb = ttk.Combobox(pb,width=18,textvariable = from_val)
    fromEntry_pb['values']=('Hyderabad','Mumbai','Delhi','Banglore','Chennai','Kolkata','Bhopal','Vishakapatnam')
    fromEntry_pb.config(font=("Verdana",15))
    fromEntry_pb.grid(row=2,column=3,ipady=2,pady=10) 
    fromEntry_pb.current(0)

    toLabel_pb = Label(pb,text="To")
    toLabel_pb.config(font=("Verdana",15))
    toLabel_pb.grid(row=3,column=2,pady=10)

    to_val = StringVar() 
    toEntry_pb = ttk.Combobox(pb,width=18,textvariable = to_val)
    toEntry_pb['values']=('Hyderabad','Mumbai','Delhi','Banglore','Chennai','Kolkata','Bhopal','Vishakapatnam')
    toEntry_pb.config(font=("Verdana",15))
    toEntry_pb.grid(row=3,column=3,ipady=2,pady=10) 
    toEntry_pb.current(1)

    dateLabel_pb = Label(pb,text="Date")
    dateLabel_pb.config(font=("Verdana",15))
    dateLabel_pb.grid(row=4,column=2,pady=10)

    date_pb=DateEntry(pb,date_pattern='dd/mm/y',width=18, background='black',foreground='grey', borderwidth=2)
    date_pb.config(font = ("Verdana", 16))
    date_pb.grid(row=4,column=3,ipady=2,pady=10)

    typeLabel_pb = Label(pb,text="Type")
    typeLabel_pb.config(font=("Verdana",15))
    typeLabel_pb.grid(row=5,column=2,pady=10)

    tktType = StringVar()
    tktEntry_pb = ttk.Combobox(pb,width=18,textvariable = tktType)
    tktEntry_pb['values']=('AC First Class(1A)','Exec. Chair Car(EC)','AC 2 Tier(2A)','First Class(FC)','AC 3 Tier(3A)','AC 3 Economy(3E)','AC Chair Car(CC)')
    tktEntry_pb.config(font=("Verdana",15))
    tktEntry_pb.grid(row=5,column=3,ipady=2,pady=10) 
    tktEntry_pb.current(0)

    noTktsLabel_pb = Label(pb, text="No of Tickets")
    noTktsLabel_pb.config(font=("Verdana",15))
    noTktsLabel_pb.grid(row=6,column=2,pady=10)

    noTkts_pb = Entry(pb, width=20)
    noTkts_pb.config(font=("Verdana",16))
    noTkts_pb.grid(row=6,column=3,pady=10,padx=5)

    noTkts_pb.insert(0,"1")

    buttonSearch = Button(pb, text = "Search", background = "black", foreground = "grey", command=searchForTrains)
    buttonSearch.config(font = ("Verdana", 15))
    buttonSearch.grid(row = 7, column = 3, ipadx = 25, ipady=5, pady = 30)

# Passenger Edit Account Window
def passengerEditAccount(passengerData):
    global pea
    pea = Tk()
    ph.iconify()
    pea.title("Passenger Edit Account")
    pea.geometry("1600x900")

    def goBackph():
        ph.deiconify()
        pea.destroy()

    def updatePassenger():
        # Creating a database or connect to one if it is already exists
        conn = sqlite3.connect("RailwayData.db") 

        # Creating a cursor
        c = conn.cursor()

        # Update a record in the DataBase
        c.execute("""UPDATE PASSENGER SET
        FNAME=?,
        LNAME=?,
        MOBILE=?,
        AGE=?,
        GENDER=?,
        CITY=?,
        PIN=?,
        PW=?
        WHERE EMAIL = ?""",
        [
            firstName_pea.get(),
            lastName_pea.get(),
            mobile_pea.get(),
            age_pea.get(),
            genderValues.get(),
            city_pea.get(),
            pincode_pea.get(),
            password_pea.get(),
            passengerData[2]
        ]
        )

        # Commit Changes
        conn.commit()

        # Close Connection
        conn.close()

        msgText = "Hello " + firstName_pea.get() + ", Your Account has been successfully updated.\nLogin again to see the updates : )"
        messagebox.showinfo("Message",msgText)

        pea.destroy()
        ph.destroy()
        passengerLogin()

    goBackToPLogin = Button(pea, text = "<", background = "black", foreground = "grey", command=goBackph)
    goBackToPLogin.config(font = ("Verdana", 20))
    goBackToPLogin.grid(row=0,column=0,ipadx=5,ipady=5)

    Label(pea, text=" ").grid(row=1,column=1,ipadx=200,pady=60)

    helloLabel = Label(pea, text="Edit Your Account Info")
    helloLabel.config(font=("Verdana",30))
    helloLabel.grid(row=1,column=3,pady=30)

    firstNameLabel_pea = Label(pea, text="First Name")
    firstNameLabel_pea.config(font = ("Verdana", 16))
    firstNameLabel_pea.grid(row=2,column=2,pady=10)

    lastNameLabel_pea = Label(pea, text="Last Name")
    lastNameLabel_pea.config(font = ("Verdana", 16))
    lastNameLabel_pea.grid(row=3,column=2,pady=10)

    mobileLabel_pea = Label(pea, text="Mobile")
    mobileLabel_pea.config(font = ("Verdana", 16))
    mobileLabel_pea.grid(row=4,column=2,pady=10)

    ageLabel_pea = Label(pea, text="Age")
    ageLabel_pea.config(font = ("Verdana", 16))
    ageLabel_pea.grid(row=5,column=2,pady=10)

    genderLabel_pea = Label(pea, text="Gender")
    genderLabel_pea.config(font = ("Verdana", 16))
    genderLabel_pea.grid(row=6,column=2,pady=10)

    cityLabel_pea = Label(pea, text="City")
    cityLabel_pea.config(font = ("Verdana", 16))
    cityLabel_pea.grid(row=7,column=2,pady=10)

    pincode_pea = Label(pea, text="PIN Code")
    pincode_pea.config(font = ("Verdana", 16))
    pincode_pea.grid(row=8,column=2,pady=10)
    
    passwordLabel_pea = Label(pea, text="Password")
    passwordLabel_pea.config(font = ("Verdana", 16))
    passwordLabel_pea.grid(row=9,column=2,pady=10)

    firstName_pea = Entry(pea, width=20)
    firstName_pea.config(font = ("Verdana",16))
    firstName_pea.grid(row=2,column=3,ipadx=20,ipady=5,pady=8)

    lastName_pea = Entry(pea, width=20)
    lastName_pea.config(font = ("Verdana",16))
    lastName_pea.grid(row=3,column=3,ipadx=20,ipady=5,pady=8)

    mobile_pea = Entry(pea, width=20)
    mobile_pea.config(font = ("Verdana",16))
    mobile_pea.grid(row=4,column=3,ipadx=20,ipady=5,pady=8)

    age_pea = Entry(pea, width=20)
    age_pea.config(font = ("Verdana",16))
    age_pea.grid(row=5,column=3,ipadx=20,ipady=5,pady=8)

    gender_pea = StringVar() 
    genderValues = ttk.Combobox(pea,width=22,textvariable = gender_pea)
    genderValues['values']=('Male','Female')
    genderValues.config(font=("Verdana",15))
    genderValues.grid(row=6,column=3,ipady=2) 
    genderValues.current()

    city_pea = Entry(pea, width=20)
    city_pea.config(font = ("Verdana",16))
    city_pea.grid(row=7,column=3,ipadx=20,ipady=5,pady=8)

    pincode_pea = Entry(pea, width=20)
    pincode_pea.config(font = ("Verdana",16))
    pincode_pea.grid(row=8,column=3,ipadx=20,ipady=5,pady=8)

    password_pea = Entry(pea, width=20,show="*")
    password_pea.config(font = ("Verdana",16))
    password_pea.grid(row=9,column=3,ipadx=20,ipady=5,pady=8)

    firstName_pea.insert(0, passengerData[0])
    lastName_pea.insert(0, passengerData[1])
    mobile_pea.insert(0, passengerData[3])
    age_pea.insert(0, passengerData[4])
    genderValues.insert(0,passengerData[5])
    city_pea.insert(0, passengerData[6])
    pincode_pea.insert(0, passengerData[7])
    password_pea.insert(0, passengerData[8])
    
    Label(pea,text=" ").grid(row=13,column=2)
    saveButton = Button(pea, text = "Save", background = "black", foreground = "grey",command=updatePassenger)
    saveButton.config(font = ("Verdana", 16))
    saveButton.grid(row=10, column=3, ipadx=120, ipady=8, pady=30)

# Passenger MyAccount Window
def passengerMyAccount(passengerData):
    global pma
    pma = Tk()
    ph.iconify()
    pma.title("Passenger Account")
    pma.geometry("1600x900")

    def goBackph():
        ph.deiconify()
        pma.destroy()

    goBackToPLogin = Button(pma, text = "<", background = "black", foreground = "grey", pady = "0", command=goBackph)
    goBackToPLogin.config(font = ("Verdana", 20))
    goBackToPLogin.grid(row=0,column=0,ipadx=5,ipady=5)

    Label(pma, text=" ").grid(row=0,column=1,ipadx=140)

    helloLabel = Label(pma, text="Your Account Info")
    helloLabel.config(font=("Verdana",30))
    helloLabel.grid(row=1,column=3,pady=30)

    firstName_pma = Label(pma, text = "First Name", fg = "grey", bg = "black")
    firstName_pma.config(font = ("Verdana", 20))
    firstName_pma.grid(row=2,column=2,pady=10,padx=30,ipadx=40,ipady=10)

    lastName_pma = Label(pma, text = "Last Name", fg = "grey", bg = "black")
    lastName_pma.config(font = ("Verdana", 20))
    lastName_pma.grid(row=3,column=2,pady=10,padx=30,ipadx=42,ipady=10)

    email_pma = Label(pma, text = "Email", fg = "grey", bg = "black")
    email_pma.config(font = ("Verdana", 20))
    email_pma.grid(row=4,column=2,pady=10,padx=30,ipadx=78,ipady=10)

    mobile_pma = Label(pma, text = "Mobile", fg = "grey", bg = "black")
    mobile_pma.config(font = ("Verdana", 20))
    mobile_pma.grid(row=5,column=2,pady=10,padx=30,ipadx=70,ipady=10)

    age_pma = Label(pma, text = "Age", fg = "grey", bg = "black")
    age_pma.config(font = ("Verdana", 20))
    age_pma.grid(row=6,column=2,pady=10,padx=30,ipadx=88,ipady=10)

    gender_pma = Label(pma, text = "Gender", fg = "grey", bg = "black")
    gender_pma.config(font = ("Verdana", 20))
    gender_pma.grid(row=7,column=2,pady=10,padx=30,ipadx=66,ipady=10)

    city_pma = Label(pma, text = "City", fg = "grey", bg = "black")
    city_pma.config(font = ("Verdana", 20))
    city_pma.grid(row=8,column=2,pady=10,padx=30,ipadx=88,ipady=10)

    pin_pma = Label(pma, text = "PIN Code", fg = "grey", bg = "black")
    pin_pma.config(font = ("Verdana", 20))
    pin_pma.grid(row=9,column=2,pady=10,padx=30,ipadx=52,ipady=10)

    firstName_pma = Label(pma,text=passengerData[0])
    firstName_pma.config(font = ("Verdana", 20))
    firstName_pma.grid(row=2,column=3,pady=10)

    lastName_pma = Label(pma,text=passengerData[1])
    lastName_pma.config(font = ("Verdana", 20))
    lastName_pma.grid(row=3,column=3,pady=10)

    email_pma = Label(pma,text=passengerData[2])
    email_pma.config(font = ("Verdana", 20))
    email_pma.grid(row=4,column=3,pady=10)

    mobile_pma = Label(pma,text=passengerData[3])
    mobile_pma.config(font = ("Verdana", 20))
    mobile_pma.grid(row=5,column=3,pady=10)

    age_pma = Label(pma,text=passengerData[4])
    age_pma.config(font = ("Verdana", 20))
    age_pma.grid(row=6,column=3,pady=10)

    gender_pma = Label(pma,text=passengerData[5])
    gender_pma.config(font = ("Verdana", 20))
    gender_pma.grid(row=7,column=3,pady=10)

    city_pma = Label(pma,text=passengerData[6])
    city_pma.config(font = ("Verdana", 20))
    city_pma.grid(row=8,column=3,pady=10)

    pin_pma = Label(pma,text=passengerData[7])
    pin_pma.config(font = ("Verdana", 20))
    pin_pma.grid(row=9,column=3,pady=10)

# Passenger Home Window
def passengerHome(email):
    global ph
    ph = Tk()
    pl.destroy()
    ph.title("Passenger Home")
    ph.geometry("1600x900")

    def goBackpl():
        passengerLogin()
        ph.destroy()

    
    goBackToPLogin = Button(ph, text = "<", background = "black", foreground = "grey", pady = "0", command=goBackpl)
    goBackToPLogin.config(font = ("Verdana", 20))
    goBackToPLogin.grid(row=0,column=0,ipadx=5,ipady=5)
    Label(ph,text=" ").grid(row=0,column=1,ipadx=100)

    # Creating a database or connect to one if it is already exists
    conn = sqlite3.connect("RailwayData.db") 

    # Creating a cursor
    c = conn.cursor()

    # Query the Database
    det = []
    c.execute("SELECT * FROM PASSENGER WHERE EMAIL = ?",[email])
    det = c.fetchall()

    # Commit Changes
    conn.commit()

    # Close Connection
    conn.close()

    passengerData = det[0]
    fName = passengerData[0]

    def onLeave1(event):
        myAcc.config (bg = 'black',fg='grey')

    def onEnter1(event):
        myAcc.config (bg = 'grey',fg = 'black')

    def onLeave2(event):
        editAcc.config (bg = 'black',fg='grey')

    def onEnter2(event):
        editAcc.config (bg = 'grey',fg = 'black')

    def onLeave3(event):
        bookTkt.config (bg = 'black',fg='grey')

    def onEnter3(event):
        bookTkt.config (bg = 'grey',fg = 'black')

    def onLeave4(event):
        bookHist.config (bg = 'black',fg='grey')

    def onEnter4(event):
        bookHist.config (bg = 'grey',fg = 'black')

    def onLeave5(event):
        logout.config (bg = 'black',fg='grey')

    def onEnter5(event):
        logout.config (bg = 'grey',fg = 'black')
    
    welcome=Label(ph, text = "Hello! " + fName, foreground = "black", pady = 50)
    welcome.config(font = ("Verdana", 20))
    welcome.grid(row=1,column=2,ipadx=0)

    myAcc = Button(ph, text="My Account", background = "black", foreground = "grey", pady = 20, command = lambda:passengerMyAccount(passengerData))
    myAcc.config(font = ("Verdana", 20))
    myAcc.grid(row=2,column=2,ipadx = 145, ipady = 40, pady=20)
    myAcc.bind ('<Enter>', onEnter1)
    myAcc.bind ('<Leave>', onLeave1)

    Label(ph,text=" ").grid(row=2,column=3,ipadx=12)

    editAcc = Button(ph, text="Edit Account", background = "black", foreground = "grey", pady = 20, command = lambda:passengerEditAccount(passengerData))
    editAcc.config(font = ("Verdana", 20))
    editAcc.grid(row=2,column=4,ipadx = 130, ipady = 40, pady=20)
    editAcc.bind ('<Enter>', onEnter2)
    editAcc.bind ('<Leave>', onLeave2)

    bookTkt = Button(ph, text="Book Tickets", background = "black", foreground = "grey", pady = 20, command = lambda:passengerBookTicket(passengerData))
    bookTkt.config(font = ("Verdana", 20))
    bookTkt.grid(row=3,column=2,ipadx = 135, ipady = 40, pady=20)
    bookTkt.bind ('<Enter>', onEnter3)
    bookTkt.bind ('<Leave>', onLeave3)

    Label(ph,text=" ").grid(row=2,column=3,ipadx=12)

    bookHist = Button(ph, text="Booking History", background = "black", foreground = "grey", pady = 20, command = lambda:myBookingHistory(passengerData[2]))
    bookHist.config(font = ("Verdana", 20))
    bookHist.grid(row=3,column=4,ipadx = 110, ipady = 40, pady=20)
    bookHist.bind ('<Enter>', onEnter4)
    bookHist.bind ('<Leave>', onLeave4)

    logout = Button(ph,text="Logout", background = "black", foreground = "grey", command=goBackpl)
    logout.config(font = ("Verdana",18))
    logout.grid(row=0,column=5,ipadx=20,ipady=8,padx=150)
    logout.bind ('<Enter>', onEnter5)
    logout.bind ('<Leave>', onLeave5)














# Admin Show Transaction Window
def showRequests():
    global stn
    stn = Tk()
    ah.iconify()
    stn.title("Transactions")
    stn.geometry("1600x900")

    def goBackah():
        ah.deiconify()
        stn.destroy()

    helloLabel = Label(stn, text="Transactions")
    helloLabel.config(font=("Verdana",30))
    helloLabel.pack(pady=20)

    # Create a main frame
    main_frame = Frame(stn)
    main_frame.pack(fill=BOTH, expand=1,padx=10)

    # Create a canvas
    my_canvas = Canvas(main_frame)
    my_canvas.pack(side=LEFT, fill=BOTH, expand=1)

    # Add a scrollbar to the canvas
    my_scrollbar = ttk.Scrollbar(main_frame, orient=VERTICAL,command=my_canvas.yview)
    my_scrollbar.pack(side=RIGHT, fill=Y)

    # Configure the canvas
    my_canvas.config(yscrollcommand=my_scrollbar.set)
    my_canvas.bind('<Configure>',lambda e : my_canvas.config(scrollregion = my_canvas.bbox("all")))

    # Add another frame inside the canvas
    second_frame = Frame(my_canvas)

    # Add that New frame to a window in the canvas
    my_canvas.create_window((0,0), window = second_frame, anchor="nw")

    # Creating a database or connect to one if it is already exists
    conn = sqlite3.connect("RailwayData.db") 

    # Creating a cursor
    c = conn.cursor()

    # Query the Database
    c.execute("SELECT * FROM TRANSACT")
    transactionData = c.fetchall()

    # Commit Changes
    conn.commit()

    # Close Connection
    conn.close()

    if len(transactionData)==0:
        Label(second_frame,text="").grid(row=0,column=0,ipadx=290,pady=50)
        sampleLabel = Label(second_frame,text="No transaction was found")
        sampleLabel.config(font=("Verdana",20))
        sampleLabel.grid(row=0,column=1)
        goBackah = Button(stn, text = "Go Back", background = "black", foreground = "grey", command=goBackah)
        goBackah.config(font = ("Verdana", 16))
        goBackah.pack(ipadx=5,ipady=2,pady=20)
        return
    
    Label(second_frame,text="").grid(row=0,column=0,ipadx=50)
    sampleLabel=Label(second_frame,text="Transaction ID")
    sampleLabel.config(font=("Verdana",16))
    sampleLabel.grid(row=0,column=1,padx=20,pady=20)
    sampleLabel=Label(second_frame,text="Passenger Email")
    sampleLabel.config(font=("Verdana",16))
    sampleLabel.grid(row=0,column=2,padx=20)
    sampleLabel=Label(second_frame,text="Card User Name")
    sampleLabel.config(font=("Verdana",16))
    sampleLabel.grid(row=0,column=3,padx=20)
    sampleLabel=Label(second_frame,text="Card Number")
    sampleLabel.config(font=("Verdana",16))
    sampleLabel.grid(row=0,column=4,padx=20)
    sampleLabel=Label(second_frame,text="Transaction Date")
    sampleLabel.config(font=("Verdana",16))
    sampleLabel.grid(row=0,column=5,padx=20)
    sampleLabel=Label(second_frame,text="Amount")
    sampleLabel.config(font=("Verdana",16))
    sampleLabel.grid(row=0,column=6,padx=20)

    for i in range (len(transactionData)):
        for j in range (len(transactionData[i])):
            sampleLabel=Label(second_frame,text=transactionData[i][j])
            sampleLabel.config(font=("Verdana",12))
            sampleLabel.grid(row=i+1,column=j+1,pady=10,padx=20)
    
    goBackah= Button(stn, text = "Go Back", background = "black", foreground = "grey", command=goBackah)
    goBackah.config(font = ("Verdana", 16))
    goBackah.pack(ipadx=5,ipady=2,pady=20)

# Admin Show Ticket Window
def showTicket():
    global st
    st = Tk()
    ah.iconify()
    st.title("Tickets")
    st.geometry("1600x900")

    def goBackah():
        ah.deiconify()
        st.destroy()

    helloLabel = Label(st, text="Tickets")
    helloLabel.config(font=("Verdana",30))
    helloLabel.pack(pady=20)

    # Create a main frame
    main_frame = Frame(st)
    main_frame.pack(fill=BOTH, expand=1,padx=10)

    # Create a canvas
    my_canvas = Canvas(main_frame)
    my_canvas.pack(side=LEFT, fill=BOTH, expand=1)

    # Add a scrollbar to the canvas
    my_scrollbar = ttk.Scrollbar(main_frame, orient=VERTICAL,command=my_canvas.yview)
    my_scrollbar.pack(side=RIGHT, fill=Y)

    # Configure the canvas
    my_canvas.config(yscrollcommand=my_scrollbar.set)
    my_canvas.bind('<Configure>',lambda e : my_canvas.config(scrollregion = my_canvas.bbox("all")))

    # Add another frame inside the canvas
    second_frame = Frame(my_canvas)

    # Add that New frame to a window in the canvas
    my_canvas.create_window((0,0), window = second_frame, anchor="nw")

    # Creating a database or connect to one if it is already exists
    conn = sqlite3.connect("RailwayData.db") 

    # Creating a cursor
    c = conn.cursor()

    # Query the Database
    c.execute("SELECT * FROM TICKETS")
    ticketData = c.fetchall()

    # Commit Changes
    conn.commit()

    # Close Connection
    conn.close()

    if len(ticketData)==0:
        Label(second_frame,text="").grid(row=0,column=0,ipadx=310,pady=50)
        sampleLabel = Label(second_frame,text="No ticket was found")
        sampleLabel.config(font=("Verdana",20))
        sampleLabel.grid(row=0,column=1)
        goBackah = Button(st, text = "Go Back", background = "black", foreground = "grey", command=goBackah)
        goBackah.config(font = ("Verdana", 16))
        goBackah.pack(ipadx=5,ipady=2,pady=20)
        return
    
    Label(second_frame,text="").grid(row=0,column=0)
    sampleLabel=Label(second_frame,text="Ticket ID")
    sampleLabel.config(font=("Verdana",16))
    sampleLabel.grid(row=0,column=1,padx=20,pady=20)
    sampleLabel=Label(second_frame,text="Pass. Name")
    sampleLabel.config(font=("Verdana",16))
    sampleLabel.grid(row=0,column=2,padx=20)
    sampleLabel=Label(second_frame,text="Passenger Email")
    sampleLabel.config(font=("Verdana",16))
    sampleLabel.grid(row=0,column=3,padx=20)
    sampleLabel=Label(second_frame,text="Train No.")
    sampleLabel.config(font=("Verdana",16))
    sampleLabel.grid(row=0,column=4,padx=20)
    sampleLabel=Label(second_frame,text="From")
    sampleLabel.config(font=("Verdana",16))
    sampleLabel.grid(row=0,column=5,padx=20)
    sampleLabel=Label(second_frame,text="To")
    sampleLabel.config(font=("Verdana",16))
    sampleLabel.grid(row=0,column=6,padx=20)
    sampleLabel=Label(second_frame,text="Date")
    sampleLabel.config(font=("Verdana",16))
    sampleLabel.grid(row=0,column=7,padx=20)
    sampleLabel=Label(second_frame,text="Type")
    sampleLabel.config(font=("Verdana",16))
    sampleLabel.grid(row=0,column=8,padx=20)
    sampleLabel=Label(second_frame,text="No. of Tkts")
    sampleLabel.config(font=("Verdana",16))
    sampleLabel.grid(row=0,column=9,padx=20)
    sampleLabel=Label(second_frame,text="Fare")
    sampleLabel.config(font=("Verdana",16))
    sampleLabel.grid(row=0,column=10,padx=20)

    for i in range (len(ticketData)):
        for j in range (len(ticketData[i])):
            sampleLabel=Label(second_frame,text=ticketData[i][j])
            sampleLabel.config(font=("Verdana",12))
            sampleLabel.grid(row=i+1,column=j+1,pady=10,padx=5)
    
    goBackah= Button(st, text = "Go Back", background = "black", foreground = "grey", command=goBackah)
    goBackah.config(font = ("Verdana", 16))
    goBackah.pack(ipadx=5,ipady=2,pady=20)

# Admin Passegers` List Window
def showPassenger():
    global sp
    sp = Tk()
    ah.iconify()
    sp.title("Passengers` List")
    sp.geometry("1600x900")

    def goBackah():
        ah.deiconify()
        sp.destroy()

    helloLabel = Label(sp, text="Passengers")
    helloLabel.config(font=("Verdana",30))
    helloLabel.pack(pady=20)

    # Create a main frame
    main_frame = Frame(sp)
    main_frame.pack(fill=BOTH, expand=1,padx=10)

    # Create a canvas
    my_canvas = Canvas(main_frame)
    my_canvas.pack(side=LEFT, fill=BOTH, expand=1)

    # Add a scrollbar to the canvas
    my_scrollbar = ttk.Scrollbar(main_frame, orient=VERTICAL,command=my_canvas.yview)
    my_scrollbar.pack(side=RIGHT, fill=Y)

    # Configure the canvas
    my_canvas.config(yscrollcommand=my_scrollbar.set)
    my_canvas.bind('<Configure>',lambda e : my_canvas.config(scrollregion = my_canvas.bbox("all")))

    # Add another frame inside the canvas
    second_frame = Frame(my_canvas)

    # Add that New frame to a window in the canvas
    my_canvas.create_window((0,0), window = second_frame, anchor="nw")

    # Creating a database or connect to one if it is already exists
    conn = sqlite3.connect("RailwayData.db") 

    # Creating a cursor
    c = conn.cursor()

    # Query the Database
    c.execute("SELECT * FROM PASSENGER")
    passengerData = c.fetchall()

    # Commit Changes
    conn.commit()

    # Close Connection
    conn.close()

    if len(passengerData)==0:
        Label(second_frame,text="").grid(row=0,column=0,ipadx=310,pady=50)
        sampleLabel = Label(second_frame,text="No account was found")
        sampleLabel.config(font=("Verdana",20))
        sampleLabel.grid(row=0,column=1)
        goBackah = Button(sp, text = "Go Back", background = "black", foreground = "grey", command=goBackah)
        goBackah.config(font = ("Verdana", 16))
        goBackah.pack(ipadx=5,ipady=2,pady=20)
        return
    
    Label(second_frame,text="").grid(row=0,column=0,ipadx=25)
    sampleLabel=Label(second_frame,text="First Name")
    sampleLabel.config(font=("Verdana",16))
    sampleLabel.grid(row=0,column=1,padx=30,pady=20)
    sampleLabel=Label(second_frame,text="Last Name")
    sampleLabel.config(font=("Verdana",16))
    sampleLabel.grid(row=0,column=2,padx=30)
    sampleLabel=Label(second_frame,text="Email")
    sampleLabel.config(font=("Verdana",16))
    sampleLabel.grid(row=0,column=3,padx=30)
    sampleLabel=Label(second_frame,text="Mobile")
    sampleLabel.config(font=("Verdana",16))
    sampleLabel.grid(row=0,column=4,padx=30)
    sampleLabel=Label(second_frame,text="Age")
    sampleLabel.config(font=("Verdana",16))
    sampleLabel.grid(row=0,column=5,padx=30)
    sampleLabel=Label(second_frame,text="Gender")
    sampleLabel.config(font=("Verdana",16))
    sampleLabel.grid(row=0,column=6,padx=30)
    sampleLabel=Label(second_frame,text="City")
    sampleLabel.config(font=("Verdana",16))
    sampleLabel.grid(row=0,column=7,padx=30)
    sampleLabel=Label(second_frame,text="PIN")
    sampleLabel.config(font=("Verdana",16))
    sampleLabel.grid(row=0,column=8,padx=30)

    for i in range (len(passengerData)):
        for j in range (len(passengerData[i])-1):
            sampleLabel=Label(second_frame,text=passengerData[i][j])
            sampleLabel.config(font=("Verdana",12))
            sampleLabel.grid(row=i+1,column=j+1,pady=10,padx=10)
    
    goBackah= Button(sp, text = "Go Back", background = "black", foreground = "grey", command=goBackah)
    goBackah.config(font = ("Verdana", 16))
    goBackah.pack(ipadx=5,ipady=2,pady=20)

# Admin Add Train
def addTrain():
    global aat
    aat = Tk()
    ah.iconify()
    aat.title("Admin Add Train")
    aat.geometry("1600x900")

    def goBackah():
        ah.deiconify()
        aat.destroy()

    def addTrainVerification():

        if tname_aat.get() == "" or source_aat.get() == "" or dest_aat.get() == "" or date_aat.get() == "" or cap_aat.get() == "" or dist_aat.get() == "" or fare_aat.get() == "":
            errorLabel = Label(aat,  text="Enter data in all input fields", fg = "red", bg = "black")
            errorLabel.config(font = ("Verdana", 12))
            errorLabel.grid(row=10,column=3,ipadx=20,ipady=16,pady=10)
            return

        if source_aat.get() == dest_aat.get():
            errorLabel = Label(aat,  text="Invalid Stations input", fg = "red", bg = "black")
            errorLabel.config(font = ("Verdana", 12))
            errorLabel.grid(row=10,column=3,ipadx=20,ipady=16,pady=10)
            return


        tn = '10000'

        # Creating a database or connect to one if it is already exists
        conn = sqlite3.connect("RailwayData.db") 

        # Creating a cursor
        c = conn.cursor()
        
        # insert into table
        c.execute("INSERT INTO TRAINS VALUES(:tno,:tname,:src,:dst,:tdate,:capa,:ds,:fr)",
            {
                'tno': tn,
                'tname':tname_aat.get(),
                'src':source_aat.get(),
                'dst':dest_aat.get(),
                'tdate':date_aat.get(),
                'capa':cap_aat.get(),
                'ds':dist_aat.get(),
                'fr':fare_aat.get()
            }
        )

        c.execute("UPDATE TRAINS SET TNO=OID")

        # Commit Changes
        conn.commit()

        # Close Connection
        conn.close()

        msgText = "Congrats, Train has been successfully added : )"
        messagebox.showinfo("Message",msgText)

        ah.deiconify()
        aat.destroy()

    goBackToAHome = Button(aat, text = "<", background = "black", foreground = "grey", command=goBackah)
    goBackToAHome.config(font = ("Verdana", 20))
    goBackToAHome.grid(row=0,column=0,ipadx=5,ipady=5)

    Label(aat, text=" ").grid(row=1,column=1,ipadx=200,pady=60)

    helloLabel = Label(aat, text="Add Train")
    helloLabel.config(font=("Verdana",30))
    helloLabel.grid(row=1,column=3,pady=20,columnspan=20)

    tnamel_aat = Label(aat,text="Train Name")
    tnamel_aat.config(font = ("Verdana", 16))
    tnamel_aat.grid(row=2,column=2,pady=10, padx=30)

    sourcel_aat = Label(aat,text="From")
    sourcel_aat.config(font = ("Verdana", 16))
    sourcel_aat.grid(row=3,column=2,pady=10)

    destl_aat = Label(aat,text="To")
    destl_aat.config(font = ("Verdana", 16))
    destl_aat.grid(row=4,column=2,pady=10)

    datel_aat = Label(aat,text="Date")
    datel_aat.config(font = ("Verdana", 16))
    datel_aat.grid(row=5,column=2,pady=10)

    capl_aat = Label(aat,text="Capacity")
    capl_aat.config(font = ("Verdana", 16))
    capl_aat.grid(row=6,column=2,pady=10)

    distl_aat = Label(aat,text="Distance")
    distl_aat.config(font = ("Verdana", 16))
    distl_aat.grid(row=7,column=2,pady=10)

    farel_aat = Label(aat,text="Fare")
    farel_aat.config(font = ("Verdana", 16))
    farel_aat.grid(row=8,column=2,pady=10)

    tname_aat = Entry(aat, width=20)
    tname_aat.config(font = ("Verdana", 16))
    tname_aat.grid(row=2,column=3,pady=10)

    source = StringVar() 
    source_aat = ttk.Combobox(aat,width=18,textvariable = source)
    source_aat['values']=('Hyderabad','Mumbai','Delhi','Banglore','Chennai','Kolkata','Bhopal','Vishakapatnam')
    source_aat.config(font=("Verdana",15))
    source_aat.grid(row=3,column=3,ipady=2) 
    source_aat.current(0)

    destination = StringVar() 
    dest_aat = ttk.Combobox(aat,width=18,textvariable = destination)
    dest_aat['values']=('Hyderabad','Mumbai','Delhi','Banglore','Chennai','Kolkata','Bhopal','Vishakapatnam')
    dest_aat.config(font=("Verdana",15))
    dest_aat.grid(row=4,column=3,ipady=2) 
    dest_aat.current(1)

    date_aat = DateEntry(aat,date_pattern='dd/mm/y',width=18, background='black',foreground='grey', borderwidth=2)
    date_aat.config(font = ("Verdana", 16))
    date_aat.grid(row=5,column=3,ipady=2,pady=10)

    cap_aat = Entry(aat, width=20)
    cap_aat.config(font = ("Verdana", 16))
    cap_aat.grid(row=6,column=3,pady=10)

    dist_aat = Entry(aat, width=20)
    dist_aat.config(font = ("Verdana", 16))
    dist_aat.grid(row=7,column=3,pady=10)

    fare_aat = Entry(aat, width=20)
    fare_aat.config(font = ("Verdana", 16))
    fare_aat.grid(row=8,column=3,pady=10)

    addButton = Button(aat, text = "Add Train", background = "black", foreground = "grey", command=addTrainVerification)
    addButton.config(font = ("Verdana", 16))
    addButton.grid(row=9, column=3, ipadx=80, ipady=6, pady=30)

# Admin Edit Account Window
def adminEditAccount(adminData):
    global pea
    aea = Tk()
    ah.iconify()
    aea.title("Admin Edit Account")
    aea.geometry("1600x900")

    def goBackah():
        ah.deiconify()
        aea.destroy()

    def updateAdmin():
        # Creating a database or connect to one if it is already exists
        conn = sqlite3.connect("RailwayData.db") 

        # Creating a cursor
        c = conn.cursor()

        # Update a record in the DataBase
        c.execute("""UPDATE ADMN SET
        FNAME=?,
        LNAME=?,
        MOBILE=?,
        AGE=?,
        GENDER=?,
        CITY=?,
        PIN=?,
        PW=?
        WHERE EMAIL = ?""",
        [
            firstName_aea.get(),
            lastName_aea.get(),
            mobile_aea.get(),
            age_aea.get(),
            genderValues.get(),
            city_aea.get(),
            pincode_aea.get(),
            password_aea.get(),
            adminData[2]
        ]
        )

        # Commit Changes
        conn.commit()

        # Close Connection
        conn.close()

        msgText = "Hello " + firstName_aea.get() + ", Your Account has been successfully updated.\nLogin again to see the updates : )"
        messagebox.showinfo("Message",msgText)

        aea.destroy()
        ah.destroy()
        adminLogin()

    goBackToAHome = Button(aea, text = "<", background = "black", foreground = "grey", command=goBackah)
    goBackToAHome.config(font = ("Verdana", 20))
    goBackToAHome.grid(row=0,column=0,ipadx=5,ipady=5)

    Label(aea, text=" ").grid(row=1,column=1,ipadx=200,pady=60)

    helloLabel = Label(aea, text="Edit Your Account Info")
    helloLabel.config(font=("Verdana",30))
    helloLabel.grid(row=1,column=3,pady=30)

    firstNameLabel_aea = Label(aea, text="First Name")
    firstNameLabel_aea.config(font = ("Verdana", 16))
    firstNameLabel_aea.grid(row=2,column=2,pady=10)

    lastNameLabel_aea = Label(aea, text="Last Name")
    lastNameLabel_aea.config(font = ("Verdana", 16))
    lastNameLabel_aea.grid(row=3,column=2,pady=10)

    mobileLabel_aea = Label(aea, text="Mobile")
    mobileLabel_aea.config(font = ("Verdana", 16))
    mobileLabel_aea.grid(row=4,column=2,pady=10)

    ageLabel_aea = Label(aea, text="Age")
    ageLabel_aea.config(font = ("Verdana", 16))
    ageLabel_aea.grid(row=5,column=2,pady=10)

    genderLabel_pea = Label(aea, text="Gender")
    genderLabel_pea.config(font = ("Verdana", 16))
    genderLabel_pea.grid(row=6,column=2,pady=10)

    cityLabel_aea = Label(aea, text="City")
    cityLabel_aea.config(font = ("Verdana", 16))
    cityLabel_aea.grid(row=7,column=2,pady=10)

    pincode_aea = Label(aea, text="PIN Code")
    pincode_aea.config(font = ("Verdana", 16))
    pincode_aea.grid(row=8,column=2,pady=10)
    
    passwordLabel_aea = Label(aea, text="Password")
    passwordLabel_aea.config(font = ("Verdana", 16))
    passwordLabel_aea.grid(row=9,column=2,pady=10)

    firstName_aea = Entry(aea, width=20)
    firstName_aea.config(font = ("Verdana",16))
    firstName_aea.grid(row=2,column=3,ipadx=20,ipady=5,pady=8)

    lastName_aea = Entry(aea, width=20)
    lastName_aea.config(font = ("Verdana",16))
    lastName_aea.grid(row=3,column=3,ipadx=20,ipady=5,pady=8)

    mobile_aea = Entry(aea, width=20)
    mobile_aea.config(font = ("Verdana",16))
    mobile_aea.grid(row=4,column=3,ipadx=20,ipady=5,pady=8)

    age_aea = Entry(aea, width=20)
    age_aea.config(font = ("Verdana",16))
    age_aea.grid(row=5,column=3,ipadx=20,ipady=5,pady=8)

    gender_aea = StringVar() 
    genderValues = ttk.Combobox(aea,width=22,textvariable = gender_aea)
    genderValues['values']=('Male','Female')
    genderValues.config(font=("Verdana",15))
    genderValues.grid(row=6,column=3,ipady=2) 
    genderValues.current()

    city_aea = Entry(aea, width=20)
    city_aea.config(font = ("Verdana",16))
    city_aea.grid(row=7,column=3,ipadx=20,ipady=5,pady=8)

    pincode_aea = Entry(aea, width=20)
    pincode_aea.config(font = ("Verdana",16))
    pincode_aea.grid(row=8,column=3,ipadx=20,ipady=5,pady=8)

    password_aea = Entry(aea, width=20,show="*")
    password_aea.config(font = ("Verdana",16))
    password_aea.grid(row=9,column=3,ipadx=20,ipady=5,pady=8)

    firstName_aea.insert(0, adminData[0])
    lastName_aea.insert(0, adminData[1])
    mobile_aea.insert(0, adminData[3])
    age_aea.insert(0, adminData[4])
    genderValues.insert(0,adminData[5])
    city_aea.insert(0, adminData[6])
    pincode_aea.insert(0, adminData[7])
    password_aea.insert(0, adminData[8])
    
    Label(aea,text=" ").grid(row=13,column=2)
    saveButton = Button(aea, text = "Save", background = "black", foreground = "grey",command=updateAdmin)
    saveButton.config(font = ("Verdana", 16))
    saveButton.grid(row=10, column=3, ipadx=120, ipady=8, pady=30)

# Admin MyAccount Window
def adminMyAccount(adminData):
    global ama
    ama = Tk()
    ah.iconify()
    ama.title("Admin Account")
    ama.geometry("1600x900")

    def goBackah():
        ah.deiconify()
        ama.destroy()

    goBackToALogin = Button(ama, text = "<", background = "black", foreground = "grey", pady = "0", command=goBackah)
    goBackToALogin.config(font = ("Verdana", 20))
    goBackToALogin.grid(row=0,column=0,ipadx=5,ipady=5)

    Label(ama, text=" ").grid(row=0,column=1,ipadx=140)

    helloLabel = Label(ama, text="Your Account Info")
    helloLabel.config(font=("Verdana",30))
    helloLabel.grid(row=1,column=3,pady=30)

    firstName_ama = Label(ama, text = "First Name", fg = "grey", bg = "black")
    firstName_ama.config(font = ("Verdana", 20))
    firstName_ama.grid(row=2,column=2,pady=10,padx=30,ipadx=40,ipady=10)

    lastName_ama = Label(ama, text = "Last Name", fg = "grey", bg = "black")
    lastName_ama.config(font = ("Verdana", 20))
    lastName_ama.grid(row=3,column=2,pady=10,padx=30,ipadx=42,ipady=10)

    email_ama = Label(ama, text = "Email", fg = "grey", bg = "black")
    email_ama.config(font = ("Verdana", 20))
    email_ama.grid(row=4,column=2,pady=10,padx=30,ipadx=78,ipady=10)

    mobile_ama = Label(ama, text = "Mobile", fg = "grey", bg = "black")
    mobile_ama.config(font = ("Verdana", 20))
    mobile_ama.grid(row=5,column=2,pady=10,padx=30,ipadx=70,ipady=10)

    age_ama = Label(ama, text = "Age", fg = "grey", bg = "black")
    age_ama.config(font = ("Verdana", 20))
    age_ama.grid(row=6,column=2,pady=10,padx=30,ipadx=88,ipady=10)

    gender_ama = Label(ama, text = "Gender", fg = "grey", bg = "black")
    gender_ama.config(font = ("Verdana", 20))
    gender_ama.grid(row=7,column=2,pady=10,padx=30,ipadx=66,ipady=10)

    city_ama = Label(ama, text = "City", fg = "grey", bg = "black")
    city_ama.config(font = ("Verdana", 20))
    city_ama.grid(row=8,column=2,pady=10,padx=30,ipadx=88,ipady=10)

    pin_ama = Label(ama, text = "PIN Code", fg = "grey", bg = "black")
    pin_ama.config(font = ("Verdana", 20))
    pin_ama.grid(row=9,column=2,pady=10,padx=30,ipadx=52,ipady=10)

    firstName_ama = Label(ama,text=adminData[0])
    firstName_ama.config(font = ("Verdana", 20))
    firstName_ama.grid(row=2,column=3,pady=10)

    lastName_ama = Label(ama,text=adminData[1])
    lastName_ama.config(font = ("Verdana", 20))
    lastName_ama.grid(row=3,column=3,pady=10)

    email_ama = Label(ama,text=adminData[2])
    email_ama.config(font = ("Verdana", 20))
    email_ama.grid(row=4,column=3,pady=10)

    mobile_ama = Label(ama,text=adminData[3])
    mobile_ama.config(font = ("Verdana", 20))
    mobile_ama.grid(row=5,column=3,pady=10)

    age_ama = Label(ama,text=adminData[4])
    age_ama.config(font = ("Verdana", 20))
    age_ama.grid(row=6,column=3,pady=10)

    gender_ama = Label(ama,text=adminData[5])
    gender_ama.config(font = ("Verdana", 20))
    gender_ama.grid(row=7,column=3,pady=10)

    city_ama = Label(ama,text=adminData[6])
    city_ama.config(font = ("Verdana", 20))
    city_ama.grid(row=8,column=3,pady=10)

    pin_ama = Label(ama,text=adminData[7])
    pin_ama.config(font = ("Verdana", 20))
    pin_ama.grid(row=9,column=3,pady=10)

# Admin Home Window
def adminHome(email):
    global ah
    ah = Tk()
    al.destroy()
    ah.title("Admin Home")
    ah.geometry("1600x900")

    def goBackal():
        adminLogin()
        ah.destroy()

    
    goBackToPLogin = Button(ah, text = "<", background = "black", foreground = "grey", pady = "0", command=goBackal)
    goBackToPLogin.config(font = ("Verdana", 20))
    goBackToPLogin.grid(row=0,column=0,ipadx=5,ipady=5)

    Label(ah,text=" ").grid(row=0,column=1,ipadx=100)

    # Creating a database or connect to one if it is already exists
    conn = sqlite3.connect("RailwayData.db") 

    # Creating a cursor
    c = conn.cursor()

    # Query the Database
    det = []
    c.execute("SELECT * FROM ADMN WHERE EMAIL = ?",[email])
    det = c.fetchall()

    # Commit Changes
    conn.commit()

    # Close Connection
    conn.close()

    adminData = det[0]
    fName = adminData[0]

    def onLeave1(event):
        myAcc.config (bg = 'black',fg='grey')

    def onEnter1(event):
        myAcc.config (bg = 'grey',fg = 'black')

    def onLeave2(event):
        editAcc.config (bg = 'black',fg='grey')

    def onEnter2(event):
        editAcc.config (bg = 'grey',fg = 'black')

    def onLeave3(event):
        passengerList.config (bg = 'black',fg='grey')

    def onEnter3(event):
        passengerList.config (bg = 'grey',fg = 'black')

    def onLeave4(event):
        ticketsBooked.config (bg = 'black',fg='grey')

    def onEnter4(event):
        ticketsBooked.config (bg = 'grey',fg = 'black')

    def onLeave5(event):
        transaction.config (bg = 'black',fg='grey')

    def onEnter5(event):
        transaction.config (bg = 'grey',fg = 'black')

    def onLeave6(event):
        addTn.config (bg = 'black',fg='grey')

    def onEnter6(event):
        addTn.config (bg = 'grey',fg = 'black')

    def onLeave7(event):
        logout.config (bg = 'black',fg='grey')

    def onEnter7(event):
        logout.config (bg = 'grey',fg = 'black')
    
    
    welcome=Label(ah, text = "Hello! " + fName, foreground = "black", pady = 32)
    welcome.config(font = ("Verdana", 20))
    welcome.grid(row=1,column=2,ipadx=0)

    myAcc = Button(ah, text="My Account", background = "black", foreground = "grey", pady = 20, command = lambda:adminMyAccount(adminData))
    myAcc.config(font = ("Verdana", 20))
    myAcc.grid(row=2,column=2,ipadx = 145, ipady = 40, pady=20)
    myAcc.bind ('<Enter>', onEnter1)
    myAcc.bind ('<Leave>', onLeave1)

    Label(ah,text=" ").grid(row=2,column=3,ipadx=12)

    editAcc = Button(ah, text="Edit Account", background = "black", foreground = "grey", pady = 20, command = lambda:adminEditAccount(adminData))
    editAcc.config(font = ("Verdana", 20))
    editAcc.grid(row=2,column=4,ipadx = 130, ipady = 40, pady=20)
    editAcc.bind ('<Enter>', onEnter2)
    editAcc.bind ('<Leave>', onLeave2)

    passengerList = Button(ah, text="Passengers` List", background = "black", foreground = "grey", pady = 20, command = showPassenger)
    passengerList.config(font = ("Verdana", 20))
    passengerList.grid(row=3,column=2,ipadx = 111, ipady = 40, pady=20)
    passengerList.bind ('<Enter>', onEnter3)
    passengerList.bind ('<Leave>', onLeave3)

    Label(ah,text=" ").grid(row=2,column=3,ipadx=12)

    ticketsBooked = Button(ah, text="Tickets Booked", background = "black", foreground = "grey", pady = 20, command = showTicket)
    ticketsBooked.config(font = ("Verdana", 20))
    ticketsBooked.grid(row=3,column=4,ipadx = 110, ipady = 40, pady=20)
    ticketsBooked.bind ('<Enter>', onEnter4)
    ticketsBooked.bind ('<Leave>', onLeave4)

    transaction = Button(ah, text="Transactions", background = "black", foreground = "grey", pady = 20, command=showRequests)
    transaction.config(font = ("Verdana", 20))
    transaction.grid(row=4,column=2,ipadx = 140, ipady = 40, pady=20)
    transaction.bind ('<Enter>', onEnter5)
    transaction.bind ('<Leave>', onLeave5)

    addTn = Button(ah, text="Add Train", background = "black", foreground = "grey", pady = 20, command = addTrain)
    addTn.config(font = ("Verdana", 20))
    addTn.grid(row=4,column=4,ipadx = 148, ipady = 40, pady=20)
    addTn.bind ('<Enter>', onEnter6)
    addTn.bind ('<Leave>', onLeave6)

    logout = Button(ah,text="Logout", background = "black", foreground = "grey", command=goBackal)
    logout.config(font = ("Verdana",18))
    logout.grid(row=0,column=5,ipadx=20,ipady=8,padx=144)
    logout.bind ('<Enter>', onEnter7)
    logout.bind ('<Leave>', onLeave7)

# Passenger Signup Window
def passengerSignup():
    global ps
    ps = Tk()
    pl.iconify()
    ps.title("Passenger Signup")
    ps.geometry("1600x900")

    def passengerSignupVerification():

        invalidMessage1 = Label(ps, text="Email is already in use", fg = "red", bg = "black")
        invalidMessage1.config(font = ("verdana", 16))
        invalidMessage2 = Label(ps, text="Enter data in all input fields", fg = "red", bg = "black")
        invalidMessage2.config(font = ("verdana", 16))

        if firstName_ps.get() == "" or  lastName_ps.get() == "" or  email_ps.get() == "" or  mobile_ps.get() == "" or  age_ps.get() == "" or  city_ps.get() == "" or pincode_ps.get() == "" or password_ps.get() == "":  
             invalidMessage2.grid(row=16,column=3,ipadx=40,ipady=16)
             return

        # Creating a database or connect to one if it is already exists
        conn = sqlite3.connect("RailwayData.db") 

        # Creating a cursor
        c = conn.cursor()

        # Query the Database
        pid = []
        c.execute("SELECT OID FROM PASSENGER WHERE EMAIL = ?",[email_ps.get()])
        pid = c.fetchall()

        if len(pid) > 0:
            email_ps.delete(0,END)
            invalidMessage1.grid(row=16,column=3,ipadx=50,ipady=16)
            return
        
        # insert into table
        c.execute("INSERT INTO PASSENGER VALUES(:fName,:lName,:email,:mobile,:age,:gender,:city,:pin,:pwd)",
            {
                'fName':firstName_ps.get(),
                'lName':lastName_ps.get(),
                'email':email_ps.get(),
                'mobile':mobile_ps.get(),
                'age':age_ps.get(),
                'gender':genderValues.get(),
                'city':city_ps.get(),
                'pin':pincode_ps.get(),
                'pwd':password_ps.get()
            }
        )

        # Commit Changes
        conn.commit()

        # Close Connection
        conn.close()

        msgText = "Congrats " + firstName_ps.get() + ", Your Account has been successfully created : )"
        messagebox.showinfo("Message",msgText)
        pl.deiconify()
        ps.destroy()

    def goBackpl():
        pl.deiconify()
        ps.destroy()

    
    goBackToPLogin = Button(ps, text = "<", background = "black", foreground = "grey", pady = "0", command=goBackpl)
    goBackToPLogin.config(font = ("Verdana", 20))
    goBackToPLogin.grid(row=0,column=0,ipadx=5,ipady=5)

    Label(ps, text = " ").grid(row=0,column=1,padx=200)

    signupHead = Label(ps, text = "Passenger Signup", fg = "black", pady = 10)
    signupHead.config(font = ("Verdana", 36))
    signupHead.grid(row=3,column=3)

    Label(ps, text = " ").grid(row=4,column=2)

    firstNameLabel_ps = Label(ps, text="First Name")
    firstNameLabel_ps.config(font = ("Verdana", 16))
    firstNameLabel_ps.grid(row=5,column=2,pady=9)

    lastNameLabel_ps = Label(ps, text="Last Name")
    lastNameLabel_ps.config(font = ("Verdana", 16))
    lastNameLabel_ps.grid(row=6,column=2,pady=9)

    emailLabel_ps = Label(ps, text="Email")
    emailLabel_ps.config(font = ("Verdana", 16))
    emailLabel_ps.grid(row=7,column=2,pady=9)

    mobileLabel_ps = Label(ps, text="Mobile")
    mobileLabel_ps.config(font = ("Verdana", 16))
    mobileLabel_ps.grid(row=8,column=2,pady=9)

    age_ps = Label(ps, text="Age")
    age_ps.config(font = ("Verdana", 16))
    age_ps.grid(row=9,column=2,pady=9)

    gender_ps = Label(ps, text="Gender")
    gender_ps.config(font = ("Verdana", 16))
    gender_ps.grid(row=10,column=2,pady=9)

    cityLabel_ps = Label(ps, text="City")
    cityLabel_ps.config(font = ("Verdana", 16))
    cityLabel_ps.grid(row=11,column=2,pady=9)

    pincode_ps = Label(ps, text="PIN Code")
    pincode_ps.config(font = ("Verdana", 16))
    pincode_ps.grid(row=12,column=2,pady=9)
    
    passwordLabel_ps = Label(ps, text="Password")
    passwordLabel_ps.config(font = ("Verdana", 16))
    passwordLabel_ps.grid(row=13,column=2,pady=9)


    firstName_ps = Entry(ps, width=20)
    firstName_ps.config(font = ("Verdana",16))
    firstName_ps.grid(row=5,column=3)

    lastName_ps = Entry(ps, width=20)
    lastName_ps.config(font = ("Verdana",16))
    lastName_ps.grid(row=6,column=3)

    email_ps = Entry(ps, width=20)
    email_ps.config(font = ("Verdana",16))
    email_ps.grid(row=7,column=3)

    mobile_ps = Entry(ps, width=20)
    mobile_ps.config(font = ("Verdana",16))
    mobile_ps.grid(row=8,column=3)

    age_ps = Entry(ps, width=20)
    age_ps.config(font = ("Verdana",16))
    age_ps.grid(row=9,column=3)

    gender_ps = StringVar() 
    genderValues = ttk.Combobox(ps,width=18,textvariable = gender_ps)
    genderValues['values']=('Male','Female')
    genderValues.config(font=("Verdana",15))
    genderValues.grid(row=10,column=3,ipady=2) 
    genderValues.current()

    city_ps = Entry(ps, width=20)
    city_ps.config(font = ("Verdana",16))
    city_ps.grid(row=11,column=3)

    pincode_ps = Entry(ps, width=20)
    pincode_ps.config(font = ("Verdana",16))
    pincode_ps.grid(row=12,column=3)

    password_ps = Entry(ps, width=20, show="*")
    password_ps.config(font = ("Verdana",16))
    password_ps.grid(row=13,column=3)

    Label(ps,text=" ").grid(row=14,column=2)
    signupButton_ps = Button(ps, text = "Signup", background = "black", foreground = "grey",command=passengerSignupVerification)
    signupButton_ps.config(font = ("Verdana", 16))
    signupButton_ps.grid(row=15, column=3, ipadx=100, ipady=10, pady=10)
    
# Admin Signup Window
def adminSignup():
    global ads
    ads = Tk()
    al.iconify()
    ads.title("Admin Signup")
    ads.geometry("1600x900")

    def adminSignupVerification():
    
        invalidMessage1 = Label(ads, text="Email is already in use", fg = "red", bg = "black")
        invalidMessage1.config(font = ("verdana", 16))
        invalidMessage2 = Label(ads, text="Enter data in all input fields", fg = "red", bg = "black")
        invalidMessage2.config(font = ("verdana", 16))

        if firstName_as.get() == "" or  lastName_as.get() == "" or  email_as.get() == "" or  mobile_as.get() == "" or  age_as.get() == "" or  city_as.get() == "" or pincode_as.get() == "" or password_as.get() == "":  
             invalidMessage2.grid(row=16,column=3,ipadx=40,ipady=16)
             return

        # Creating a database or connect to one if it is already exists
        conn = sqlite3.connect("RailwayData.db") 

        # Creating a cursor
        c = conn.cursor()

        # Query the Database
        pid = []
        c.execute("SELECT OID FROM ADMN WHERE EMAIL = ?",[email_as.get()])
        pid = c.fetchall()

        if len(pid) > 0:
            email_as.delete(0,END)
            invalidMessage1.grid(row=16,column=3,ipadx=50,ipady=16)
            return
        
        # insert into table
        c.execute("INSERT INTO ADMN VALUES(:fName,:lName,:email,:mobile,:age,:gender,:city,:pin,:pwd)",
            {
                'fName':firstName_as.get(),
                'lName':lastName_as.get(),
                'email':email_as.get(),
                'mobile':mobile_as.get(),
                'age':age_as.get(),
                'gender':genderValues.get(),
                'city':city_as.get(),
                'pin':pincode_as.get(),
                'pwd':password_as.get()
            }
        )

        # Commit Changes
        conn.commit()

        # Close Connection
        conn.close()

        msgText = "Congrats " + firstName_as.get() + ", Your Account has been successfully created : )"
        messagebox.showinfo("Message",msgText)
        al.deiconify()
        ads.destroy()
    
    def goBackal():
        al.deiconify()
        ads.destroy()

    goBackToALogin = Button(ads, text = "<", background = "black", foreground = "grey", pady = "0", command=goBackal)
    goBackToALogin.config(font = ("Verdana", 20))
    goBackToALogin.grid(row=0,column=0,ipadx=5,ipady=5)
    
    Label(ads, text = " ").grid(row=0,column=1,padx=220)

    signupHead = Label(ads, text = "Admin Signup", fg = "black", pady = 10)
    signupHead.config(font = ("Verdana", 36))
    signupHead.grid(row=3,column=3)

    Label(ads, text = " ").grid(row=4,column=2)

    firstNameLabel_as = Label(ads, text="First Name")
    firstNameLabel_as.config(font = ("Verdana", 16))
    firstNameLabel_as.grid(row=5,column=2,pady=9)

    lastNameLabel_as = Label(ads, text="Last Name")
    lastNameLabel_as.config(font = ("Verdana", 16))
    lastNameLabel_as.grid(row=6,column=2,pady=9)

    emailLabel_as = Label(ads, text="Email")
    emailLabel_as.config(font = ("Verdana", 16))
    emailLabel_as.grid(row=7,column=2,pady=9)

    mobileLabel_as = Label(ads, text="Mobile")
    mobileLabel_as.config(font = ("Verdana", 16))
    mobileLabel_as.grid(row=8,column=2,pady=9)

    age_as = Label(ads, text="Age")
    age_as.config(font = ("Verdana", 16))
    age_as.grid(row=9,column=2,pady=9)

    gender_as = Label(ads, text="Gender")
    gender_as.config(font = ("Verdana", 16))
    gender_as.grid(row=10,column=2,pady=9)

    cityLabel_as = Label(ads, text="City")
    cityLabel_as.config(font = ("Verdana", 16))
    cityLabel_as.grid(row=11,column=2,pady=9)

    pincode_as = Label(ads, text="PIN Code")
    pincode_as.config(font = ("Verdana", 16))
    pincode_as.grid(row=12,column=2,pady=9)
    
    passwordLabel_as = Label(ads, text="Password")
    passwordLabel_as.config(font = ("Verdana", 16))
    passwordLabel_as.grid(row=13,column=2)


    firstName_as = Entry(ads, width=20)
    firstName_as.config(font = ("Verdana",16))
    firstName_as.grid(row=5,column=3)

    lastName_as = Entry(ads, width=20)
    lastName_as.config(font = ("Verdana",16))
    lastName_as.grid(row=6,column=3)

    email_as = Entry(ads, width=20)
    email_as.config(font = ("Verdana",16))
    email_as.grid(row=7,column=3)

    mobile_as = Entry(ads, width=20)
    mobile_as.config(font = ("Verdana",16))
    mobile_as.grid(row=8,column=3)

    age_as = Entry(ads, width=20)
    age_as.config(font = ("Verdana",16))
    age_as.grid(row=9,column=3)

    gender_ps = StringVar() 
    genderValues = ttk.Combobox(ads,width=18,textvariable = gender_ps)
    genderValues['values']=('Male','Female')
    genderValues.config(font=("Verdana",15))
    genderValues.grid(row=10,column=3,ipady=2) 
    genderValues.current()

    city_as = Entry(ads, width=20)
    city_as.config(font = ("Verdana",16))
    city_as.grid(row=11,column=3)

    pincode_as = Entry(ads, width=20)
    pincode_as.config(font = ("Verdana",16))
    pincode_as.grid(row=12,column=3)

    password_as = Entry(ads, width=20, show="*")
    password_as.config(font = ("Verdana",16))
    password_as.grid(row=13,column=3)

    Label(ads,text=" ").grid(row=14,column=2)
    signupButton_as = Button(ads, text = "Signup", background = "black", foreground = "grey",command=adminSignupVerification)
    signupButton_as.config(font = ("Verdana", 16))
    signupButton_as.grid(row=15, column=3, ipadx=100, ipady=10, pady=20)

# Passenger Login Window
def passengerLogin():
    # pl is the new window
    global pl
    pl = Tk()
    root.iconify()
    pl.title("Passenger Login")
    pl.geometry("1600x900")

    # Function to check whether the Email and Password matches or not
    def passengerLoginVerification():

        email = email_pl.get()
        invalidMessage = Label(pl, text="Incorrect Email/Password", fg = "red", bg = "black")
        invalidMessage.config(font = ("verdana", 16))

        # Creating a database or connect to one if it is already exists
        conn = sqlite3.connect("RailwayData.db") 

        # Creating a cursor
        c = conn.cursor()

        # Query the Database
        pid = []
        c.execute("SELECT OID FROM PASSENGER WHERE EMAIL = ? and PW = ?",[email_pl.get(),password_pl.get()])
        pid = c.fetchall()

        # Commit Changes
        conn.commit()

        # Close Connection
        conn.close()

        email_pl.delete(0,END)
        password_pl.delete(0,END)
        if len(pid) == 0:
            invalidMessage.grid(row=15,column=1,ipady=16,ipadx=40)
        else:
            passengerHome(email)

    def onLeave1(event):
        loginButton_pl.config (bg = 'black',fg='grey')

    def onEnter1(event):
        loginButton_pl.config (bg = 'grey',fg = 'black')

    def onLeave2(event):
        signupButton_pl.config (bg = 'black',fg='grey')

    def onEnter2(event):
        signupButton_pl.config (bg = 'grey',fg = 'black')
        
    Label(pl,text=" ").grid(row=0,column=0,ipadx=250,ipady=20)

    loginHead = Label(pl, text = "Passenger Login", foreground = "black", pady = 30)
    loginHead.config(font = ("Verdana", 44))
    loginHead.grid(row=1,column=1)

    Label(pl,text=" ").grid(row=2,column=1)
    emailLabel_pl = Label(pl,text = "Email")
    emailLabel_pl.config(font = ("Verdana", 20))
    emailLabel_pl.grid(row=3,column=1)

    Label(pl,text=" ").grid(row=4,column=1)
    email_pl = Entry(pl,width=25)
    email_pl.config(font=("Verdana",16))
    email_pl.grid(row=5,column=1,ipadx=40,ipady=10)
    
    Label(pl,text=" ").grid(row=6,column=1)
    passwordLabel_pl = Label(pl,text = "Password")
    passwordLabel_pl.config(font = ("Verdana", 20))
    passwordLabel_pl.grid(row=7,column=1)
    
    Label(pl,text=" ").grid(row=8,column=1)
    password_pl = Entry(pl, width=25, show='*')
    password_pl.config(font=("Verdana",16))
    password_pl.grid(row=9,column=1,ipadx=40,ipady=10)

    Label(pl,text=" ").grid(row=10,column=1,pady=20)
    loginButton_pl = Button(pl, text = "Login", background = "black", foreground = "grey", pady = "0", command=passengerLoginVerification)
    loginButton_pl.config(font = ("Verdana", 20))
    loginButton_pl.grid(row=11,column=1,ipadx=164,ipady=10)
    loginButton_pl.bind ('<Enter>', onEnter1)
    loginButton_pl.bind ('<Leave>', onLeave1)

    Label(pl,text=" ").grid(row=12,column=1)
    signupButton_pl = Button(pl, text = "Signup", background = "black", foreground = "grey", pady = "0", command=passengerSignup)
    signupButton_pl.config(font = ("Verdana", 20))
    signupButton_pl.grid(row=13,column=1,ipadx=155,ipady=10)
    signupButton_pl.bind ('<Enter>', onEnter2)
    signupButton_pl.bind ('<Leave>', onLeave2)
    Label(pl,text=" ").grid(row=14,column=1)

# Admin Login Window
def adminLogin():
    global al
    al = Tk()
    root.iconify()
    al.title("Admin Login")
    al.geometry("1600x900")

    # Function to check whether the Email and Password matches or not
    def adminLoginVerification():

        email = email_al.get()
        invalidMessage = Label(al, text="Incorrect Email/Password", fg = "red", bg = "black")
        invalidMessage.config(font = ("verdana", 16))

        # Creating a database or connect to one if it is already exists
        conn = sqlite3.connect("RailwayData.db") 

        # Creating a cursor
        c = conn.cursor()

        # Query the Database
        pid = []
        c.execute("SELECT OID FROM ADMN WHERE EMAIL = ? and PW = ?",[email_al.get(),password_al.get()])
        pid = c.fetchall()

        # Commit Changes
        conn.commit()

        # Close Connection
        conn.close()

        email_al.delete(0,END)
        password_al.delete(0,END)
        if len(pid) == 0:
            invalidMessage.grid(row=15,column=1,ipady=16,ipadx=40)
        else:
            adminHome(email)
        
    Label(al,text=" ").grid(row=0,column=0,ipadx=280,ipady=20)

    def onLeave1(event):
        loginButton_al.config (bg = 'black',fg='grey')

    def onEnter1(event):
        loginButton_al.config (bg = 'grey',fg = 'black')

    def onLeave2(event):
        signupButton_al.config (bg = 'black',fg='grey')

    def onEnter2(event):
        signupButton_al.config (bg = 'grey',fg = 'black')
        

    loginHead = Label(al, text = "Admin Login", foreground = "black", pady = 30)
    loginHead.config(font = ("Verdana", 44))
    loginHead.grid(row=1,column=1)

    Label(al,text=" ").grid(row=2,column=1)
    emailLabel_al = Label(al,text = "Email")
    emailLabel_al.config(font = ("Verdana", 20))
    emailLabel_al.grid(row=3,column=1)

    Label(al,text=" ").grid(row=4,column=1)
    email_al = Entry(al, width=25)
    email_al.config(font=("Verdana",16))
    email_al.grid(row=5,column=1,ipadx=40,ipady=10)
    
    Label(al,text=" ").grid(row=6,column=1)
    passwordLabel_al = Label(al,text = "Password")
    passwordLabel_al.config(font = ("Verdana", 20))
    passwordLabel_al.grid(row=7,column=1)
    
    Label(al,text=" ").grid(row=8,column=1)
    password_al = Entry(al, width=25)
    password_al.config(font=("Verdana",16),show="*")
    password_al.grid(row=9,column=1,pady=20,ipadx=40,ipady=10)

    Label(al,text=" ").grid(row=10,column=1)
    loginButton_al = Button(al, text = "Login", background = "black", foreground = "grey", pady = "0", command=adminLoginVerification)
    loginButton_al.config(font = ("Verdana", 20))
    loginButton_al.grid(row=11,column=1,ipadx=164,ipady=10)
    loginButton_al.bind ('<Enter>', onEnter1)
    loginButton_al.bind ('<Leave>', onLeave1)

    Label(al,text=" ").grid(row=12,column=1)
    signupButton_al = Button(al, text = "Signup", background = "black", foreground = "grey", pady = "0", command=adminSignup)
    signupButton_al.config(font = ("Verdana", 20))
    signupButton_al.grid(row=13,column=1,ipadx=155,ipady=10)
    Label(al,text=" ").grid(row=14,column=1)
    signupButton_al.bind ('<Enter>', onEnter2)
    signupButton_al.bind ('<Leave>', onLeave2)

# Root Window
# Welcome Label

def onLeave1(event):
    buttonPassenger.config (bg = 'black',fg='grey',font=("Verdana",20))

def onEnter1(event):
    buttonPassenger.config (bg = 'grey',fg = 'black',font=("Verdana",22))

def onLeave2(event):
    buttonAdmin.config (bg = 'black',fg='grey',font=("Verdana",20))

def onEnter2(event):
    buttonAdmin.config (bg = 'grey',fg = 'black',font=("Verdana",22))

Label(root, text="").pack(pady=20)
welcome=Label(root, text = "Welcome to \nRailway Ticketing", foreground = "black", pady = 30)
welcome.config(font = ("Verdana", 44))
welcome.pack()

spaceLabel1 = Label(root,text=" ")
spaceLabel1.pack(pady=30)

# Login buttons
buttonPassenger = Button(root, text = "Login as a Passenger", background = "black", foreground = "grey", pady = 20, command = passengerLogin)
buttonPassenger.config(font = ("Verdana", 20))
buttonPassenger.pack(ipadx = 74, ipady = 20)
buttonPassenger.bind ('<Enter>', onEnter1)
buttonPassenger.bind ('<Leave>', onLeave1)

spaceLabel2=Label(root, text = " ")
spaceLabel2.pack()

buttonAdmin=Button(root, text = "Login as a Admin", background = "black", foreground = "grey", pady = 20, command = adminLogin)
buttonAdmin.config(font = ("Verdana", 20))
buttonAdmin.pack(ipadx = 100, ipady = 20)
buttonAdmin.bind ('<Enter>', onEnter2)
buttonAdmin.bind ('<Leave>', onLeave2)

root.mainloop() 