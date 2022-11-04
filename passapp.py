import random
from tkinter import Checkbutton, Label,LabelFrame,Button, PhotoImage, Radiobutton, Tk,Entry,IntVar,CENTER
import pyperclip
import pymysql

conn = pymysql.connect(host="sql12.freemysqlhosting.net",user="sql12540395",password="Th5YTnw4FX",port=3306,database="sql12540395")
c = conn.cursor()
#c.execute("create table passlog(sno int primary key not null auto_increment, softname varchar(50),password varchar(256))")
#c.execute("show tables")
def intodb():
    c.execute("insert into passlog(softname,password) values(%s,%s)",(softname,passw))
    conn.commit()
    print ([i for i in c.fetchall()])

window = Tk()
window.title("PASSWORD MANAGER")
p1 = PhotoImage(file="lock.png")
window.iconphoto(False,p1)
passw=""
#this func is defined when the user selects no for generating random pass
def logpass():
    def logOrCopy1():
        if rvar.get()==1:
            print ("Enter into database")
            intodb()
        elif rvar.get()==2:
            pyperclip.copy(passw)
            print ("Successfully Copied!")
        else:
            print("Invalid")
    #passw=entry.get()
    for widget in window.winfo_children():
                    widget.destroy()
    labelframe = LabelFrame(
                    window,
                    relief = "raised",
                    height = 400,
                    borderwidth=10,
                    width = 400
                    )
    labelframe.pack(padx=5,pady=5)

    label=Label(labelframe,text="Choose",font=("Lucida Sans",15))
    label.pack(padx=10,pady=10)
    rvar = IntVar()
    r1 = Radiobutton(labelframe,text= "Log the password", variable=rvar,command=logOrCopy1,font = ("Lucida Sans",10), value =1)
    r2 = Radiobutton(labelframe,text="Copy the password",variable=rvar,command=logOrCopy1,value=2,font =("Lucida Sans",10))
    r1.pack(anchor=CENTER,padx=10,pady=10)
    r2.pack(anchor=CENTER,pady=10,padx=10)
    btn = Button(labelframe,text="Go Back To Main Menu",command=mainmenu,font=("Lucida Sans",7))
    btn.pack(padx=5,pady=5)


def create():
    def softnamebtn():
        def yesno():
            def genpass():
                def logOrCopy():
                    def logOrCopy1():
                        if rvar.get()==1:
                            intodb()
                        elif rvar.get()==2:
                            pyperclip.copy(passw)
                            print ("Successfully Copied!")
                        else:
                            print("Invalid")

                    if rvar.get()==1:
                       intodb()
                    elif rvar.get()==2:
                        pyperclip.copy(passw)
                        print ("Successfully Copied!")
                    else:
                        print("Invalid")
                genpasslen = int(entry.get())
                for widget in window.winfo_children():
                    widget.destroy()
                global passw
                passw=""
                for i in range(genpasslen):
                    passw+=chr(random.randint(33,126))
                print (passw)
                labelframe = LabelFrame(
                    window,
                    relief = "raised",
                    height = 400,
                    borderwidth=10,
                    width = 400
                    )
                labelframe.pack(padx=5,pady=5)

                label = Label(labelframe,text="Choose",font=("Lucida Sans",15))
                label.pack(padx=10,pady=10)

                rvar = IntVar()
                r1 = Radiobutton(labelframe,text= "Log the password", variable=rvar,command=logOrCopy,font = ("Lucida Sans",10), value =1)
                r2 = Radiobutton(labelframe,text="Copy the password",variable=rvar,command=logOrCopy,value=2,font =("Lucida Sans",10))
                r1.pack(anchor=CENTER,padx=10,pady=10)
                r2.pack(anchor=CENTER,pady=10,padx=10)
                btn = Button(labelframe,text="Go Back To Main Menu",command=mainmenu,font=("Lucida Sans",7))
                btn.pack(padx=5,pady=5)

            if var.get()==1:
                print ("Random Pass")
                for widget in window.winfo_children():
                    widget.destroy()


                labelframe = LabelFrame(
                    window,
                    relief = "raised",
                    height = 400,
                    borderwidth=10,
                    width = 400
                    )
                labelframe.pack(padx=5,pady=5)

                label = Label(labelframe,text="Enter the length for the randomly generated password : ",font=("Lucida Sans",15))
                label.pack(padx=10,pady=10)
                entry = Entry(labelframe,font = ("Lucida Sans",10))
                entry.pack(padx=10,pady=10)
                btn = Button(labelframe,text="Submit",font = ("Lucida Sans",10), command=genpass)
                btn.pack(padx=10,pady=10)

            elif var.get()==2:
                for widget in window.winfo_children():
                    widget.destroy()
                labelframe = LabelFrame(
                    window,
                    relief = "raised",
                    height = 400,
                    borderwidth=10,
                    width = 400
                    )
                labelframe.pack(padx=5,pady=5)
                label = Label(labelframe,text="Enter Your Password",font=("Lucida Sans",15))
                label.pack(padx=10,pady=10)
                entry = Entry(labelframe, font=("Lucida Sans",10))
                entry.pack(padx=10,pady=10)
                btn = Button(labelframe,text = "Submit", font=("Lucida Sans",9),command=logpass)
                btn.pack(padx=5,pady=5)


            else:
                print ("Invalid Operation")
        global softname
        softname = entry.get()
        #print (softname)
        #window.destroy()
        for widget in window.winfo_children():
            widget.destroy()

        labelframe = LabelFrame(
        window,
        relief = "raised",
        height = 400,
        borderwidth=10,
        width = 400
        )
        labelframe.pack(padx=5,pady=5)

        label = Label(labelframe,font = ("Lucida Sans",15),text="Do you want a randomly generated password? ")
        label.pack(padx=10,pady=10,anchor=CENTER)

        var = IntVar()
        r1 = Radiobutton(labelframe,text= "Yes", variable=var,font = ("Lucida Sans",10), value =1,command=yesno)
        r2 = Radiobutton(labelframe,text="No",variable=var, value=2,command=yesno,font =("Lucida Sans",10))
        r1.pack(anchor=CENTER,padx=5,pady=5)
        r2.pack(anchor=CENTER,pady=5,padx=5)

    for widget in window.winfo_children():
        widget.destroy()

    labelframe = LabelFrame(
        window,
        relief = "raised",
        height = 400,
        borderwidth=10,
        width = 400
        )
    labelframe.pack(padx=5,pady=5)

    label = Label(
            labelframe,
            text = "Enter the name of the software: ",
            font = ("Lucida Sans",15)
            )
    label.pack(padx=10,pady=10)
    entry = Entry(
            labelframe,
            )
    entry.pack(padx=10,pady=10)
    btn = Button(
            labelframe,
            text = "Submit",
            font = ("Lucida Sans",10),
            command = softnamebtn
            )
    btn.pack(padx=5,pady=5)

def mainmenu():
    for widget in window.winfo_children():
        widget.destroy()
    labelframe = LabelFrame(
        window,
        relief = "raised",
        height = 400,
        borderwidth=10,
        width = 400
        )
    labelframe.pack(padx=5,pady=5)

    label = Label(
        labelframe,
        text = "PASSWORD MANAGER",
        font = ("Lucida Sans",15)
        )
    label.pack(padx=10,pady=10)
    btn = Button(
        labelframe,
        text = "Create",
        font = ("Lucida Sans",10),
        command = create
        )

    btn.pack(padx=10,pady=10)

mainmenu()

window.mainloop()


