import smtplib
from tkinter import *
import getpass
smtp_object = smtplib.SMTP('smtp.gmail.com',587)
smtp_object.ehlo()
smtp_object.starttls()
class MyWindow:
    def __init__(self, win):
        self.lbl1=Label(win, text='Email:')
        self.lbl2=Label(win, text='Password:')
        self.lbl3=Label(win, text='Email address of person you want to send the email to:')
        self.t1=Entry(bd=3)
        self.t2=Entry()
        self.t3=Entry()
        self.b2 = Button(win, text='Send email:',command = self.sendEmail)
        self.lbl1.place(x=100, y=50)
        self.t1.place(x=200, y=50)
        self.lbl2.place(x=100, y=100)
        self.t2.place(x=200, y=100)
        self.lbl3.place(x=100, y=200)
        self.t3.place(x=450, y=200)
        self.b1=Button(win, text='Login', command=self.login)
        self.b1.place(x=100, y=150)
        self.b2.place(x = 100, y = 250)
    def login(self):
        global from_address 
        from_address = str(self.t1.get())
        password = str(self.t2.get())
        smtp_object.login(from_address,password)
    def sendEmail(self):
        subject = 'hi'
        message = 'hi'
        to_address = self.t3.get()
        msg = 'Subject: '+subject+'\n'+message
        smtp_object.sendmail(from_address,to_address,msg)
        
window=Tk()
mywin=MyWindow(window)
window.title('Hello Python')
window.geometry("500x400+10+10")
window.mainloop()
